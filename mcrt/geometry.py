import numpy as np


def are_on_same_side(p1, p2, a, b):
    """
    Checks if p1 and p2 are on the same side of ab
    """
    ab = b - a
    cp1 = np.cross(ab, p1 - a)
    cp2 = np.cross(ab, p2 - a)

    return np.dot(cp1, cp2) >= 0


class Ray:
    """
    Represents a ray in the 3d space in the form:
    Origin * Direction * t
    """
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def value(self, t):
        """
        Returns the coordinates of a point on the ray for a given parameter
        value t
        """
        return self.origin + t * self.direction

    def intersect(self, plane):
        """
        Finds intersection of a ray with a plane
        Returns three things:
            - True if intersection exists, otherwise False
            - the value of t of the intersection point, if exists
        """
        tcoeff = np.dot(self.direction, plane[0:3])

        if np.allclose(tcoeff, 0):
            # The plane is parallel ot the direction of the vector, so
            # no intersection
            return False, None

        freecoeff = -np.dot(self.origin, plane[0:3]) - plane[3]
        t = freecoeff / tcoeff

        return True, t


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def plane(self):
        """
        Returns the plane the triangle is laying on
        """
        v1 = self.b - self.a
        v2 = self.c - self.a

        cp = np.cross(v1, v2)
        a, b, c = cp
        d = -np.dot(cp, self.a)

        return np.array([a, b, c, d])

    def is_inside(self, p):
        """
        Checks if a point is inside or on the boundary of the triangle.

        The point must be on the same plane as the triangle, otherwise the
        result is not defined.
        """
        return are_on_same_side(p, self.a, self.b, self.c) and \
            are_on_same_side(p, self.b, self.a, self.c) and \
            are_on_same_side(p, self.c, self.a, self.b)

    def intersect(self, ray):
        """
        Checks if a ray intersects the triangle. Has two return values:
            - does_intersect - if the ray intersects the triangle (bool)
            - t - the t parameter value for the ray. It is guaranteed
                to be > 0 if does_intersect is True
        """
        plane = self.plane()

        does_intersect, t = ray.intersect(plane)

        if (not does_intersect) or t < 0:
            return False, None

        intersection = ray.value(t)

        if self.is_inside(intersection):
            return True, t
        else:
            return False, None
