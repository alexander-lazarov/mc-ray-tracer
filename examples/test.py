from mcrt.render import Scene, Renderer
from mcrt.geometry import Triangle

triangle = Triangle((0.1, 0, 1), (0, 0.3, 1), (0, 0, 1))
triangle2 = Triangle((0.2, 3, 0), (0, 0, 1), (0, 0, 2))

scene = Scene()
scene.add(triangle)
scene.add(triangle2)

renderer = Renderer(scene)
renderer.render()
