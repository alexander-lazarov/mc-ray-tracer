from mcrt.render import Scene, Renderer
from mcrt.geometry import Triangle, Plane
from mcrt.material import Material


side_0 = Plane((-2, -2, 5), (2, -2, 5), (2, 2, 5))
side_1 = Plane((-2, -2, 5), (-2, 2, 5), (-2, 2, 0.))
side_2 = Plane((2, 2, 5), (-2, 2, 5), (-2, 2, 0.))
side_3 = Plane((2, 2, 5), (2, -2, 5), (2, 2, 0.))
side_4 = Plane((-2, -2, 5), (2, -2, 5), (-2, -2, 0.))

tri = Triangle((-0.2, -0.2, 3), (-0.2, 3, 3), (-0.1, -0.2, 3))

scene = Scene()

scene.lightsource((-1.5, -1.5, 0))
scene.add(side_0, (1., 0., 0.), Material.MATERIAL_DIFFUSE)
scene.add(side_1, (0., 1., 0.), Material.MATERIAL_DIFFUSE)
scene.add(side_2, (0., 0., 1.), Material.MATERIAL_DIFFUSE)
scene.add(side_3, (0., 1., 1.), Material.MATERIAL_DIFFUSE)
scene.add(side_4, (0., 1., 1.), Material.MATERIAL_DIFFUSE)
# scene.add(tri, (0., 1., 1.), Material.MATERIAL_DIFFUSE)

renderer = Renderer(scene)
renderer.render()
