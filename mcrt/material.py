class Material:
    MATERIAL_MIRROR = 1
    MATERIAL_DIFFUSE = 2

    def __init__(self, color, material_type):
        self.color = color
        self.material_type = material_type
