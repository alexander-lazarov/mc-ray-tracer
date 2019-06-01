from mcrt.geometry import Ray, subtract3
from PIL import Image

class Scene:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def intersect(self, ray):
        for obj in self.objects:
           intersect, _ =  obj.intersect(ray)

           if intersect:
               return True

        return False


class Renderer:
    def __init__(self, scene):
        self.scene = scene
        self.image_w = 640
        self.image_h = 480

        self.camera = (0, 0, -1)
        self.screen = (0, 0, 0)
        self.screen_w = 1.00
        self.screen_h = 0.75

    def render(self):
        img = Image.new("RGB", (self.image_w, self.image_h))

        data = []

        for y in range(self.image_h):
            for x in range(self.image_w):
                xoffset = (x - (self.image_w / 2)) * (self.screen_w / self.image_w)
                yoffset = (y - (self.image_h / 2)) * (self.screen_h / self.image_h)

                pixel = (xoffset,
                        yoffset,
                        self.screen[2]
                        )

                ray = Ray(self.camera, subtract3(pixel, self.camera))

                if self.scene.intersect(ray):
                    data.append((255, 255, 255))
                else:
                    data.append((0, 0, 0))

        img.putdata(data)
        img.show()
