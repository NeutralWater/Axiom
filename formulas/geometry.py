import math

# ==========================
# 2D Geometry
# ==========================

def circle_area(r):
    return math.pi * r ** 2

def rectangle_area(l, w):
    return l * w

def triangle_area(b, h):
    return 0.5 * b * h

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

def parallelogram_area(b, h):
    return b * h

def ellipse_area(a, b):
    return math.pi * a * b

def sector_area(r, theta):
    return 0.5 * r ** 2 * math.radians(theta)

def circle_circumference(r):
    return 2 * math.pi * r

def rectangle_perimeter(l, w):
    return 2 * (l + w)

def triangle_perimeter(a, b, c):
    return a + b + c

def pythagorean(a, b):
    return math.sqrt(a ** 2 + b ** 2)

# ==========================
# 3D Volumes
# ==========================

def sphere_volume(r):
    return (4 / 3) * math.pi * r ** 3

def cylinder_volume(r, h):
    return math.pi * r ** 2 * h

def cone_volume(r, h):
    return (1 / 3) * math.pi * r ** 2 * h

def prism_volume(base_area, h):
    return base_area * h

def pyramid_volume(base_area, h):
    return (1 / 3) * base_area * h

def torus_volume(R, r):
    return 2 * math.pi ** 2 * R * r ** 2

def ellipsoid_volume(a, b, c):
    return (4 / 3) * math.pi * a * b * c

def frustum_volume(r1, r2, h):
    return (1 / 3) * math.pi * h * (r1 ** 2 + r1 * r2 + r2 ** 2)

# ==========================
# 3D Surface Areas
# ==========================

def sphere_surface_area(r):
    return 4 * math.pi * r ** 2

def cylinder_surface_area(r, h):
    return 2 * math.pi * r * (r + h)

def cone_surface_area(r, h):
    return math.pi * r * (r + math.sqrt(r ** 2 + h ** 2))

def prism_surface_area(base_perimeter, base_area, h):
    return base_perimeter * h + 2 * base_area

def pyramid_surface_area(base_perimeter, base_area, slant_height):
    return base_area + 0.5 * base_perimeter * slant_height

def torus_surface_area(R, r):
    return 4 * math.pi ** 2 * R * r

def ellipsoid_surface_area(a, b, c):
    p = 1.6075
    return (
        4
        * math.pi
        * (
            (
                (a ** p) * (b ** p)
                + (a ** p) * (c ** p)
                + (b ** p) * (c ** p)
            )
            / 3
        )
        ** (1 / p)
    )

def frustum_surface_area(r1, r2, h):
    slant_height = math.sqrt((r2 - r1) ** 2 + h ** 2)
    return math.pi * (r1 + r2) * slant_height + math.pi * (r1 ** 2 + r2 ** 2)