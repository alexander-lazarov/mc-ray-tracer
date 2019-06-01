import unittest
import numpy as np
from mcrt.geometry import Triangle, Ray


class RayTests(unittest.TestCase):
    def test_t_value(self):
        ray = Ray(np.array([0, 0, 0]), np.array([1, 1, 1]))
        self.assertTrue(
                np.allclose(ray.value(0.5), np.array([0.5, 0.5, 0.5])))

    def test_intersect_true(self):
        ray = Ray(np.array([0, 0, 0]), np.array([1, 1, 1]))
        plane = np.array([1, 1, 1, -1])

        does_intersect, t = ray.intersect(plane)
        self.assertTrue(does_intersect)

    def test_itersect_false(self):
        ray = Ray(np.array([0, 0, 0]), np.array([1, 1, 0]))
        plane = np.array([1, -1, 0, 0])

        does_intersect, _ = ray.intersect(plane)
        self.assertFalse(does_intersect)


class TriangleTests(unittest.TestCase):
    def test_plane(self):
        triangle = Triangle(
                np.array([1, 0, 0]),
                np.array([0, 1, 0]),
                np.array([0, 0, 1]))

        self.assertTrue(
                np.allclose(triangle.plane(), np.array([1, 1, 1, -1])))

    def test_is_inside_1(self):
        triangle = Triangle(
                np.array([1, 0, 0]),
                np.array([1, 1, 0]),
                np.array([1, 0, 1]))

        point = np.array([1, 0, 0])

        self.assertTrue(triangle.is_inside(point))

    def test_is_inside_2(self):
        triangle = Triangle(
                np.array([1, 0, 0]),
                np.array([1, 1, 0]),
                np.array([1, 0, 1]))

        point = np.array([1, -1, -1])

        self.assertFalse(triangle.is_inside(point))

    def test_intersect_1(self):
        triangle = Triangle(
                np.array([1, 0, 0]),
                np.array([0, 1, 0]),
                np.array([0, 0, 1]))

        ray = Ray(np.array([0, 0, 0]), np.array([1, 1, 1]))

        does_intersect, t = triangle.intersect(ray)

        self.assertTrue(does_intersect)

    def test_intersect_2(self):
        triangle = Triangle(
                np.array([1, 0, 0]),
                np.array([0, 1, 0]),
                np.array([0, 0, 1]))

        ray = Ray(np.array([1, 1, 1]), np.array([0, 0, 0]))
        does_intersect, t = triangle.intersect(ray)

        self.assertFalse(does_intersect)

    def test_intersect_3(self):
        triangle = Triangle(
                np.array([1, 0, 0]),
                np.array([0, 1, 0]),
                np.array([0, 0, 1]))
        ray = Ray(np.array([0.5, 0, 0]), np.array([0, -1, 1]))

        does_intersect, t = triangle.intersect(ray)

        self.assertFalse(does_intersect)
