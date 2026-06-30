import math

def dot_product(v1, v2):
    if len(v1) != len(v2):
        return None

    return sum(a * b for a, b in zip(v1, v2))

def magnitude(v):
    return math.sqrt(sum(x**2 for x in v))

def unit_vector(v):
    mag = magnitude(v)

    if mag == 0:
        return None

    return [x / mag for x in v]