from mcrt.geometry import Ray, subtract3
from mcrt.material import Material
from random import random

from PIL import Image


class Scene:
    def __init__(self):
        self.objects = []

    def add(self, obj, color, material):
        self.objects.append((obj, color, material))

    def intersect(self, ray, bounces):
        found = False
        min_f = 0
        found_color = (0, 0, 0)

        for obj, color, _material in self.objects:
            intersect, f = obj.intersect(ray)

            if not intersect:
                continue

            if (not found) or (f < min_f):
                found = True
                min_f = f
                found_color = color

        return found_color


class Renderer:
    def __init__(self, scene):
        self.scene = scene
        self.image_w = 240
        self.image_h = 180

        self.bounces = 5

        self.samples_per_pixel = 5

        self.camera = (0, 0, -1)
        self.screen = (0, 0, 0)
        self.projection_w = 1.00
        self.projection_h = 0.75

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
                    yoffset = (y - (self.image_h / 2)) * step_w + step_w*random()
                    xoffset = (x - (self.image_w / 2)) * step_h + step_h*random()

                    pixel = (xoffset, yoffset, self.screen[2])

                    ray.direction = subtract3(pixel, self.camera)

                    r, g, b = self.scene.intersect(ray, self.bounces)
                    result_r += r
                    result_g += g
                    result_b += b


                data.append((
                    int(result_r / self.samples_per_pixel),
                    int(result_g / self.samples_per_pixel),
                    int(result_b / self.samples_per_pixel)
                ))

        img.putdata(data)
        img.show()
