import unittest
from mcrt.geometry import Triangle, Ray, equal3, equal4, unit3


class Unit3Tests(unittest.TestCase):
    def test_unit3(self):
        v = (1, 1, 1)
        r = (0.5773502691896258, 0.5773502691896258, 0.5773502691896258)

        self.assertTrue(
            equal3(unit3(v), r)
        )


class RayTests(unittest.TestCase):
    def test_t_value(self):
        ray = Ray((0, 0, 0), (1, 1, 1))
        self.assertTrue(
                equal3(ray.value(0.5), (0.5, 0.5, 0.5)))

    def test_intersect_true(self):
        ray = Ray((0, 0, 0), (1, 1, 1))
        plane = (1, 1, 1, -1)

        does_intersect, t = ray.intersect(plane)
        self.assertTrue(does_intersect)

    def test_itersect_false(self):
        ray = Ray((0, 0, 0), (1, 1, 0))
        plane = (1, -1, 0, 0)

        does_intersect, _ = ray.intersect(plane)
        self.assertFalse(does_intersect)


class TriangleTests(unittest.TestCase):
    def test_plane(self):
        triangle = Triangle(
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1))

        self.assertTrue(
                equal4(triangle.plane, (1, 1, 1, -1)))

    def test_is_inside_1(self):
        triangle = Triangle(
                (1, 0, 0),
                (1, 1, 0),
                (1, 0, 1))

        point = (1, 0, 0)

        self.assertTrue(triangle.is_inside(point))

    def test_is_inside_2(self):
        triangle = Triangle(
                (1, 0, 0),
                (1, 1, 0),
                (1, 0, 1))

        point = (1, -1, -1)

        self.assertFalse(triangle.is_inside(point))

    def test_intersect_1(self):
        triangle = Triangle(
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1))

        ray = Ray((0, 0, 0), (1, 1, 1))

        does_intersect, t = triangle.intersect(ray)

        self.assertTrue(does_intersect)

    def test_intersect_2(self):
        triangle = Triangle(
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1))

        ray = Ray((1, 1, 1), (0, 0, 0))
        does_intersect, t = triangle.intersect(ray)

        self.assertFalse(does_intersect)

    def test_intersect_3(self):
        triangle = Triangle(
                (1, 0, 0),
                (0, 1, 0),
                (0, 0, 1))
        ray = Ray((0.5, 0, 0), (0, -1, 1))

        does_intersect, t = triangle.intersect(ray)

        self.assertFalse(does_intersect)
