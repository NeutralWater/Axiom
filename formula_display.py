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

def second_derivative():
    return make_formula(
        "d²/dx²[f(x)]",
        {
            "f(x)": "function",
            "x": "variable",
            "d²/dx²": "differentiate twice with respect to x"
        },
        topic="Second Derivative"
    )

def indefinite_integral():
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

def critical_points():
    return make_formula(
        "f'(x) = 0",
        {
            "f'(x)": "first derivative of the function",
            "x": "variable"
        },
        topic="Critical Points"
    )

def tangent_line():
    return make_formula(
        "y - f(a) = f'(a)(x - a)",
        {
            "f(a)": "function value at point a",
            "f'(a)": "derivative at point a",
            "x, y": "coordinates on the tangent line",
            "a": "point of tangency"
        },
        topic="Tangent Line"
    )
def normal_line():
    return make_formula(
        "y - f(a) = -1/f'(a)(x - a)",
        {
            "f(a)": "function value at point a",
            "-1/f'(a)": "negative reciprocal of the derivative at point a",
            "x, y": "coordinates on the normal line",
            "a": "point of tangency"
        },
        topic="Normal Line"
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

# ==========================
# Converisons
# ==========================

def fahrenheit_to_celsius():
    return make_formula(
        "C = (F - 32) * 5/9",
        {
            "C": "temperature in Celsius",
            "F": "temperature in Fahrenheit"
        },
        units="°C",
        topic="Fahrenheit to Celsius Conversion"
    )

def celsius_to_fahrenheit():
    return make_formula(
        "F = (C * 9/5) + 32",
        {
            "F": "temperature in Fahrenheit",
            "C": "temperature in Celsius"
        },
        units="°F",
        topic="Celsius to Fahrenheit Conversion"
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

def rectangle_perimeter():
    return make_formula(
        "P = 2(l + w)",
        {
            "P": "perimeter",
            "l": "length",
            "w": "width"
        },
        units="units",
        topic="Rectangle Perimeter"
    )


def pythagorean():
    return make_formula(
        "c = √(a² + b²)",
        {
            "a": "first leg",
            "b": "second leg",
            "c": "hypotenuse"
        },
        units="units",
        topic="Pythagorean Theorem"
    )


# ==========================
# Physics
# ==========================

def work():
    return make_formula(
        "W = Fd",
        {
            "W": "work",
            "F": "force",
            "d": "distance"
        },
        units="joules",
        topic="Work"
    )


# ==========================
# Statistics
# ==========================

def mean():
    return make_formula(
        "Mean = Σx / n",
        {
            "Σx": "sum of all values",
            "n": "number of values"
        },
        topic="Arithmetic Mean"
    )


def range():
    return make_formula(
        "Range = Maximum − Minimum",
        {
            "Maximum": "largest value",
            "Minimum": "smallest value"
        },
        topic="Range"
    )


def simple_interest():
    return make_formula(
        "I = Prt",
        {
            "I": "interest",
            "P": "principal",
            "r": "interest rate",
            "t": "time"
        },
        units="currency",
        topic="Simple Interest"
    )


def compound_interest():
    return make_formula(
        "A = P(1 + r/n)^(nt)",
        {
            "A": "final amount",
            "P": "principal",
            "r": "annual interest rate",
            "n": "compounds per year",
            "t": "time (years)"
        },
        units="currency",
        topic="Compound Interest"
    )