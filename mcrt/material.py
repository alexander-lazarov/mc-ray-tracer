class Material:
    MATERIAL_LIGHTSOURCE = 1
    MATERIAL_MIRROR = 2
    MATERIAL_DIFFUSE = 3

    def __init__(self, color, material_type):
        self.color = color
        self.material_type = material_type
