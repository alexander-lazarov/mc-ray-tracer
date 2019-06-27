from mcrt.render import Scene, Renderer
from mcrt.geometry import Triangle, Plane
from mcrt.material import Material

triangle = Triangle((-2, -2, 5), (2, -2, 5), (2, 2, 5))
triangle2 = Triangle((-2, -2, 5), (-2, 2, 5), (2, 2, 5))

side_1 = Plane((-2, -2, 5), (-2, 2, 5), (-2, 2, 0))
side_2 = Plane((2, 2, 5), (-2, 2, 5), (-2, 2, 0))
side_3 = Plane((2, 2, 5), (2, -2, 5), (2, 2, 0))
side_4 = Plane((-2, -2, 5), (2, -2, 5), (-2, -2, 0))

scene = Scene()
scene.add(triangle2, (0, 255, 0), Material.MATERIAL_LIGHTSOURCE)
scene.add(triangle, (255, 0, 0), Material.MATERIAL_LIGHTSOURCE)
scene.add(side_1, (255, 0, 255), Material.MATERIAL_LIGHTSOURCE)
scene.add(side_2, (0, 255, 255), Material.MATERIAL_LIGHTSOURCE)
scene.add(side_3, (0, 255, 255), Material.MATERIAL_LIGHTSOURCE)
scene.add(side_4, (0, 255, 255), Material.MATERIAL_LIGHTSOURCE)

renderer = Renderer(scene)
renderer.render()
