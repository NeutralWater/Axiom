from formula_display import *

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