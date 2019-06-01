from mcrt.render import Scene, Renderer
from mcrt.geometry import Triangle

triangle = Triangle((0.1, 0, 1), (0, 0.3, 1), (0, 0, 1))

scene = Scene()
scene.add(triangle)

renderer = Renderer(scene)
renderer.render()

