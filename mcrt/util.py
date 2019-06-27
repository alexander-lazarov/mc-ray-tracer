from random import random
from mcrt.geometry import dot3
from math import pi, sqrt


def random_hemisphere(n):
    x, y, z = random(), random() ,random()

    radius = sqrt(x ** 2 + y ** 2 + z ** 2)

    x /= radius
    y /= radius
    z /= radius


    if dot3(n, (x, y, z)) > 0:
        return (x, y, z)
    else:
        return (-x, -y, -z)
