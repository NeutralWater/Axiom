import sympy as sp

x = sp.Symbol("x")

def derivative(e):
    expr = sp.sympify(e)
    return sp.diff(expr,x)

def second_derivative(expr):
    expr = sp.sympify(expr)
    return sp.diff(expr, x, 2)

def indefinite_integral(expr):
    expr = sp.sympify(expr)
    return sp.integrate(expr, x)

def definite_integral(expr, a, b):
    expr = sp.sympify(expr)
    return sp.integrate(expr, (x, a, b))

def limit(expr, value):
    expr = sp.sympify(expr)

    if value == "inf":
        value = sp.oo
    elif value == "-inf":
        value = -sp.oo

    return sp.limit(expr, x, value)

def critical_points(expr):
    expr = sp.sympify(expr)
    d = sp.diff(expr, x)
    return sp.solve(d, x)

def tangent_line(expr, a):
    expr = sp.sympify(expr)

    y1 = expr.subs(x, a)
    m = sp.diff(expr, x).subs(x, a)

    return sp.expand(m * (x - a) + y1)

def normal_line(expr, a):
    expr = sp.sympify(expr)

    y1 = expr.subs(x, a)
    m = sp.diff(expr, x).subs(x, a)

    if m == 0:
        return None

    normal_m = -1 / m
    return sp.expand(normal_m * (x - a) + y1)