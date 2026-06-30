from formula_display.core import *

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