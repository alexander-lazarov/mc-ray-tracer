from mcrt.geometry import Ray, add3, subtract3, unit3, dot3, product3
from mcrt.material import Material
from mcrt.util import random_hemisphere

from random import random
from math import pow, sqrt

from PIL import Image


class Scene:
    def __init__(self):
        self.objects = []

    def add(self, obj, color, material):
        self.objects.append((obj, color, material))

    def lightsource(self, lightsource_position):
        self.lightsource = lightsource_position

    def is_directly_illuminated(self, point):
        dir = subtract3(self.lightsource, point)
        d = sqrt(dot3(dir, dir))
        ray = Ray(point, unit3(dir))

        found = False

        for obj, _, _ in self.objects:
            intersect, t = obj.intersect(ray)

            if intersect and t < d:
                return False

        return True


    def intersect(self, ray, bounces):
        found = False
        min_t = 0
        found_color = (0, 0, 0)
        found_obj = None

        for obj, color, material in self.objects:
            intersect, t = obj.intersect(ray)

            if not intersect:
                continue

            if (not found) or (t < min_t):
                found = True
                min_t = t
                found_color = color
                found_material = material
                found_obj = obj

        if not found:
            return (0, 0, 0)
        else:
            intersection = ray.value(min_t)

            if found_material == Material.MATERIAL_DIFFUSE:
                if self.is_directly_illuminated(intersection):
                    cos = abs(dot3(ray.direction, found_obj.normal))

                    direct = product3(found_color, cos * 0.8)
                else:
                    direct = (0, 0, 0)

                if bounces > 0:
                    next_ray = Ray(
                        intersection, random_hemisphere(found_obj.normal))
                    indirect = product3(
                        self.intersect(next_ray, bounces - 1), 0.8)
                else:
                    indirect = (0, 0, 0)

                return add3(direct, indirect)
            elif found_material == Material.MATERIAL_MIRROR:
                # TODO
                return (0, 0, 0)


class Renderer:
    def __init__(self, scene):
        self.scene = scene
        self.image_w = 320
        self.image_h = 240

        self.bounces = 40

        self.samples_per_pixel = 3

        self.camera = (0.2, 0.2, -1)
        self.screen = (0, 0, 0)
        self.projection_w = 1.00 / 0.5
        self.projection_h = 0.75 / 0.5

        self.gamma = 1.25

    def render(self):
        img = Image.new("RGB", (self.image_w, self.image_h))

        data = []
        ray = Ray(self.camera, (1, 1, 1))

        step_w = self.projection_h / self.image_h
        step_h = self.projection_w / self.image_w

        for y in range(self.image_h):
            for x in range(self.image_w):
                result_r = 0.
                result_g = 0.
                result_b = 0.

                for _ in range(self.samples_per_pixel):
                    yoffset = (y - (self.image_h / 2)) * step_w + \
                        step_w*random()
                    xoffset = (x - (self.image_w / 2)) * step_h + \
                        step_h*random()

                    pixel = (xoffset, yoffset, self.screen[2])

                    ray.direction = unit3(subtract3(pixel, self.camera))

                    r, g, b = self.scene.intersect(ray, self.bounces)
                    result_r += r
                    result_g += g
                    result_b += b

                data.append((
                    int(255 * pow(result_r / self.samples_per_pixel, self.gamma)),
                    int(255 * pow(result_g / self.samples_per_pixel, self.gamma)),
                    int(255 * pow(result_b / self.samples_per_pixel, self.gamma))
                ))

        img.putdata(data)
        img.show()

        fname = f"sample_{self.image_w}x{self.image_h}_" \
                f"{self.samples_per_pixel}_{self.bounces}.png"
        img.save(fname)
