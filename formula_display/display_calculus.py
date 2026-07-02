from formula_display.core import *

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

def increasing_decreasing():
    return make_formula(
        "f'(x) > 0,  f'(x) < 0",
        {
            "f'(x) > 0": "function is increasing",
            "f'(x) < 0": "function is decreasing",
            "x": "variable"
        },
        topic="Increasing / Decreasing Intervals"
    )

def concavity():
    return make_formula(
        "f''(x) > 0,  f''(x) < 0",
        {
            "f''(x) > 0": "concave up",
            "f''(x) < 0": "concave down",
            "x": "variable"
        },
        topic="Concavity"
    )

def inflection_points():
    return make_formula(
        "f''(x) = 0",
        {
            "f''(x)": "second derivative",
            "x": "possible inflection point"
        },
        topic="Inflection Points"
    )

def average_value():
    return make_formula(
        "(1/(b-a)) ∫ₐᵇ f(x) dx",
        {
            "a": "lower bound",
            "b": "upper bound",
            "f(x)": "function",
            "1/(b-a)": "average over the interval"
        },
        topic="Average Value of a Function"
    )

def area_between_curves():
    return make_formula(
        "∫ₐᵇ |f(x)-g(x)| dx",
        {
            "a": "lower bound",
            "b": "upper bound",
            "f(x)": "upper function",
            "g(x)": "lower function"
        },
        topic="Area Between Curves"
    )

def arc_length():
    return make_formula(
        "∫ₐᵇ √(1 + [f'(x)]²) dx",
        {
            "a": "lower bound",
            "b": "upper bound",
            "f'(x)": "derivative of the function"
        },
        topic="Arc Length"
    )

def disk_volume():
    return make_formula(
        "π ∫ₐᵇ [f(x)]² dx",
        {
            "π": "pi",
            "a": "lower bound",
            "b": "upper bound",
            "f(x)": "radius of the solid"
        },
        topic="Disk Method"
    )

def washer_volume():
    return make_formula(
        "π ∫ₐᵇ (R²-r²) dx",
        {
            "R": "outer radius",
            "r": "inner radius",
            "a": "lower bound",
            "b": "upper bound"
        },
        topic="Washer Method"
    )

def newtons_method():
    return make_formula(
        "xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)",
        {
            "xₙ": "current approximation",
            "xₙ₊₁": "next approximation",
            "f(xₙ)": "function value",
            "f'(xₙ)": "derivative at xₙ"
        },
        topic="Newton's Method"
    )