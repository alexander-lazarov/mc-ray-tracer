EPSILON = 1e-7


def dot3(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross3(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def subtract3(a, b):
    return (a[0] - b[0],
            a[1] - b[1],
            a[2] - b[2])


def add3(a, b):
    return (a[0] + b[0],
            a[1] + b[1],
            a[2] + b[2])


def equal3(a, b):
    return abs(a[0] - b[0]) < EPSILON and \
        abs(a[1] - b[1]) < EPSILON and \
        abs(a[2] - b[2]) < EPSILON


def equal4(a, b):
    return abs(a[0] - b[0]) < EPSILON and \
        abs(a[1] - b[1]) < EPSILON and \
        abs(a[2] - b[2]) < EPSILON and \
        abs(a[3] - b[3]) < EPSILON


def product3(a, n):
    return (a[0] * n, a[1] * n, a[2] * n)


def are_on_same_side(p1, p2, a, b):
    """
    Checks if p1 and p2 are on the same side of ab
    """
    ab = subtract3(b, a)
    cp1 = cross3(ab, subtract3(p1, a))
    cp2 = cross3(ab, subtract3(p2, a))

    return dot3(cp1, cp2) >= 0


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
        return (self.origin[0] + t * self.direction[0],
                self.origin[1] + t * self.direction[1],
                self.origin[2] + t * self.direction[2])

    def intersect(self, plane):
        """
        Finds intersection of a ray with a plane
        Returns three things:
            - True if intersection exists, otherwise False
            - the value of t of the intersection point, if exists
        """
        tcoeff = dot3(self.direction, plane[0:3])

        if abs(tcoeff) < EPSILON:
            # The plane is parallel ot the direction of the vector, so
            # no intersection
            return False, None

        freecoeff = - dot3(self.origin, plane) - plane[3]

        t = freecoeff / tcoeff

        return True, t

class Plane:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.plane = self.plane()

    def plane(self):
        """
        Returns the plane the triangle is laying on
        """
        v1 = subtract3(self.b, self.a)
        v2 = subtract3(self.c, self.a)

        cp = cross3(v1, v2)
        a, b, c = cp
        d = -dot3(cp, self.a)

        return (a, b, c, d)

    def intersect(self, ray):
        """
        Checks if a ray intersects the triangle. Has two return values:
            - does_intersect - if the ray intersects the triangle (bool)
            - t - the t parameter value for the ray. It is guaranteed
                to be > 0 if does_intersect is True
        """
        does_intersect, t = ray.intersect(self.plane)

        if (not does_intersect) or t < 0:
            return False, None

        intersection = ray.value(t)

        return True, t

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        self.plane = self.plane()

    def plane(self):
        """
        Returns the plane the triangle is laying on
        """
        v1 = subtract3(self.b, self.a)
        v2 = subtract3(self.c, self.a)

        cp = cross3(v1, v2)
        a, b, c = cp
        d = -dot3(cp, self.a)

        return (a, b, c, d)

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
        does_intersect, t = ray.intersect(self.plane)

        if (not does_intersect) or t < 0:
            return False, None

        intersection = ray.value(t)

        if self.is_inside(intersection):
            return True, t
        else:
            return False, None
