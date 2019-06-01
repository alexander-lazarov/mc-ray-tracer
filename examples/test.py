from mcrt.render import Scene, Renderer
from mcrt.geometry import Triangle

triangle = Triangle((0.1, 0, 1), (0, 0.3, 1), (0, 0, 1))
triangle2 = Triangle((0.2, 3, 0), (10, 0, 1), (0, 0, 2))

scene = Scene()
scene.add(triangle2, (0, 255, 0))
scene.add(triangle, (255, 0, 0))

renderer = Renderer(scene)
renderer.render()
