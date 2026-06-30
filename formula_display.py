def make_formula(formula, variables, units=None, topic=None, notes=None):
    return {
        "formula": formula,
        "variables": variables,
        "units": units,
        "topic": topic,
        "notes": notes
    }


def display_formula(data):
    print("\nFormula Used:")
    print(data["formula"])

    print("\nVariables:")
    for var, desc in data["variables"].items():
        print(f"{var} = {desc}")

    if data.get("units"):
        print("\nUnits:")
        print(data["units"])

    if data.get("topic"):
        print("\nTopic:")
        print(data["topic"])

    if data.get("notes"):
        print("\nNotes:")
        print(data["notes"])


# ==========================
# Algebra
# ==========================

def quadratic():
    return make_formula(
        "x = (-b ± √(b² - 4ac)) / (2a)",
        {
            "x": "solution",
            "a": "quadratic coefficient",
            "b": "linear coefficient",
            "c": "constant term"
        },
        topic="Quadratic Formula"
    )


def discriminant():
    return make_formula(
        "Δ = b² - 4ac",
        {
            "Δ": "discriminant",
            "a": "quadratic coefficient",
            "b": "linear coefficient",
            "c": "constant term"
        },
        topic="Discriminant"
    )


def slope():
    return make_formula(
        "m = (y₂ - y₁) / (x₂ - x₁)",
        {
            "m": "slope",
            "x₁, y₁": "first point",
            "x₂, y₂": "second point"
        },
        topic="Slope Formula",
        notes="A vertical line has undefined slope."
    )


def midpoint():
    return make_formula(
        "M = ((x₁ + x₂)/2, (y₁ + y₂)/2)",
        {
            "M": "midpoint",
            "x₁, y₁": "first point",
            "x₂, y₂": "second point"
        },
        topic="Midpoint Formula"
    )


def distance():
    return make_formula(
        "d = √((x₂ - x₁)² + (y₂ - y₁)²)",
        {
            "d": "distance between two points",
            "x₁, y₁": "first point",
            "x₂, y₂": "second point"
        },
        topic="Distance Formula"
    )


def point_slope():
    return make_formula(
        "y - y₁ = m(x - x₁)",
        {
            "m": "slope",
            "x₁, y₁": "known point on the line",
            "x, y": "general point on the line"
        },
        topic="Point-Slope Form"
    )


def slope_intercept():
    return make_formula(
        "y = mx + b",
        {
            "m": "slope",
            "b": "y-intercept",
            "x, y": "coordinates on the line"
        },
        topic="Slope-Intercept Form"
    )


# ==========================
# Calculus
# ==========================

def derivative():
    return make_formula(
        "d/dx[f(x)]",
        {
            "f(x)": "function",
            "x": "variable",
            "d/dx": "differentiate with respect to x"
        },
        topic="Derivative"
    )


def power_rule():
    return make_formula(
        "d/dx(xⁿ) = nxⁿ⁻¹",
        {
            "x": "variable",
            "n": "exponent"
        },
        topic="Power Rule"
    )


def integral():
    return make_formula(
        "∫f(x) dx",
        {
            "f(x)": "function being integrated",
            "dx": "integrate with respect to x"
        },
        topic="Indefinite Integral"
    )


def definite_integral():
    return make_formula(
        "∫ₐᵇ f(x) dx",
        {
            "a": "lower bound",
            "b": "upper bound",
            "f(x)": "function being integrated"
        },
        topic="Definite Integral"
    )


def limit():
    return make_formula(
        "lim(x→a) f(x)",
        {
            "a": "value x approaches",
            "f(x)": "function"
        },
        topic="Limit"
    )


# ==========================
# Geometry
# ==========================

def circle_area():
    return make_formula(
        "A = πr²",
        {
            "A": "area",
            "r": "radius"
        },
        units="square units",
        topic="Circle Area"
    )


def circle_circumference():
    return make_formula(
        "C = 2πr",
        {
            "C": "circumference",
            "r": "radius"
        },
        units="units",
        topic="Circle Circumference"
    )


def rectangle_area():
    return make_formula(
        "A = lw",
        {
            "A": "area",
            "l": "length",
            "w": "width"
        },
        units="square units",
        topic="Rectangle Area"
    )


def triangle_area():
    return make_formula(
        "A = ½bh",
        {
            "A": "area",
            "b": "base",
            "h": "height"
        },
        units="square units",
        topic="Triangle Area"
    )


# ==========================
# Physics
# ==========================

def force():
    return make_formula(
        "F = ma",
        {
            "F": "force",
            "m": "mass",
            "a": "acceleration"
        },
        units="newtons",
        topic="Newton's Second Law"
    )


def kinetic_energy():
    return make_formula(
        "KE = ½mv²",
        {
            "KE": "kinetic energy",
            "m": "mass",
            "v": "velocity"
        },
        units="joules",
        topic="Kinetic Energy"
    )


def momentum():
    return make_formula(
        "p = mv",
        {
            "p": "momentum",
            "m": "mass",
            "v": "velocity"
        },
        units="kg·m/s",
        topic="Momentum"
    )