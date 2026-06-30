from formula_display import *

# ==========================
# 2D Geometry
# ==========================

def circle_area():
    return make_formula(
        "A = πr²",
        {"A": "area", "r": "radius"},
        units="square units",
        topic="Circle Area"
    )

def rectangle_area():
    return make_formula(
        "A = lw",
        {"A": "area", "l": "length", "w": "width"},
        units="square units",
        topic="Rectangle Area"
    )

def triangle_area():
    return make_formula(
        "A = ½bh",
        {"A": "area", "b": "base", "h": "height"},
        units="square units",
        topic="Triangle Area"
    )

def trapezoid_area():
    return make_formula(
        "A = ½(a + b)h",
        {"A": "area", "a": "first base", "b": "second base", "h": "height"},
        units="square units",
        topic="Trapezoid Area"
    )

def parallelogram_area():
    return make_formula(
        "A = bh",
        {"A": "area", "b": "base", "h": "height"},
        units="square units",
        topic="Parallelogram Area"
    )

def ellipse_area():
    return make_formula(
        "A = πab",
        {"A": "area", "a": "semi-major axis", "b": "semi-minor axis"},
        units="square units",
        topic="Ellipse Area"
    )

def sector_area():
    return make_formula(
        "A = ½r²θ",
        {"A": "area", "r": "radius", "θ": "central angle in radians"},
        units="square units",
        topic="Sector Area"
    )

def circle_circumference():
    return make_formula(
        "C = 2πr",
        {"C": "circumference", "r": "radius"},
        units="units",
        topic="Circle Circumference"
    )

def rectangle_perimeter():
    return make_formula(
        "P = 2(l + w)",
        {"P": "perimeter", "l": "length", "w": "width"},
        units="units",
        topic="Rectangle Perimeter"
    )

def triangle_perimeter():
    return make_formula(
        "P = a + b + c",
        {"P": "perimeter", "a": "first side", "b": "second side", "c": "third side"},
        units="units",
        topic="Triangle Perimeter"
    )

def pythagorean():
    return make_formula(
        "c = √(a² + b²)",
        {"a": "first leg", "b": "second leg", "c": "hypotenuse"},
        units="units",
        topic="Pythagorean Theorem"
    )


# ==========================
# 3D Volumes
# ==========================

def sphere_volume():
    return make_formula(
        "V = 4/3πr³",
        {"V": "volume", "r": "radius"},
        units="cubic units",
        topic="Sphere Volume"
    )

def cylinder_volume():
    return make_formula(
        "V = πr²h",
        {"V": "volume", "r": "radius", "h": "height"},
        units="cubic units",
        topic="Cylinder Volume"
    )

def cone_volume():
    return make_formula(
        "V = 1/3πr²h",
        {"V": "volume", "r": "radius", "h": "height"},
        units="cubic units",
        topic="Cone Volume"
    )

def prism_volume():
    return make_formula(
        "V = Bh",
        {"V": "volume", "B": "area of the base", "h": "height"},
        units="cubic units",
        topic="Prism Volume"
    )

def pyramid_volume():
    return make_formula(
        "V = ⅓Bh",
        {"V": "volume", "B": "area of the base", "h": "height"},
        units="cubic units",
        topic="Pyramid Volume"
    )

def torus_volume():
    return make_formula(
        "V = 2π²Rr²",
        {"V": "volume", "R": "major radius", "r": "minor radius"},
        units="cubic units",
        topic="Torus Volume"
    )

def ellipsoid_volume():
    return make_formula(
        "V = 4/3πabc",
        {"V": "volume", "a": "semi-axis a", "b": "semi-axis b", "c": "semi-axis c"},
        units="cubic units",
        topic="Ellipsoid Volume"
    )

def frustum_volume():
    return make_formula(
        "V = ⅓πh(r₁² + r₁r₂ + r₂²)",
        {"V": "volume", "h": "height", "r₁": "bottom radius", "r₂": "top radius"},
        units="cubic units",
        topic="Frustum Volume"
    )


# ==========================
# 3D Surface Areas
# ==========================

def sphere_surface_area():
    return make_formula(
        "A = 4πr²",
        {"A": "surface area", "r": "radius"},
        units="square units",
        topic="Sphere Surface Area"
    )

def cylinder_surface_area():
    return make_formula(
        "A = 2πr(r + h)",
        {"A": "surface area", "r": "radius", "h": "height"},
        units="square units",
        topic="Cylinder Surface Area"
    )

def cone_surface_area():
    return make_formula(
        "A = πr(r + √(r² + h²))",
        {"A": "surface area", "r": "radius", "h": "height"},
        units="square units",
        topic="Cone Surface Area"
    )

def prism_surface_area():
    return make_formula(
        "A = Ph + 2B",
        {"A": "surface area", "P": "perimeter of the base", "h": "height", "B": "area of the base"},
        units="square units",
        topic="Prism Surface Area"
    )

def pyramid_surface_area():
    return make_formula(
        "A = B + ½Pl",
        {"A": "surface area", "B": "area of the base", "P": "perimeter of the base", "l": "slant height"},
        units="square units",
        topic="Pyramid Surface Area"
    )

def torus_surface_area():
    return make_formula(
        "A = 4π²Rr",
        {"A": "surface area", "R": "major radius", "r": "minor radius"},
        units="square units",
        topic="Torus Surface Area"
    )

def ellipsoid_surface_area():
    return make_formula(
        "A ≈ 4π((aᵖbᵖ + aᵖcᵖ + bᵖcᵖ)/3)^(1/p)",
        {"A": "surface area", "a": "semi-axis a", "b": "semi-axis b", "c": "semi-axis c", "p": "approximation constant, usually 1.6075"},
        units="square units",
        topic="Ellipsoid Surface Area"
    )

def frustum_surface_area():
    return make_formula(
        "A = π(r₁ + r₂)l + π(r₁² + r₂²)",
        {"A": "surface area", "r₁": "bottom radius", "r₂": "top radius", "l": "slant height"},
        units="square units",
        topic="Frustum Surface Area"
    )
