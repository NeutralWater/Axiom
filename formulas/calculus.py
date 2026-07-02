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

def power_rule(expr):
    expr = sp.sympify(expr)
    return sp.diff(expr, x)

def increasing_decreasing(expr):
    expr = sp.sympify(expr)
    d = sp.diff(expr, x)
    return sp.solve_univariate_inequality(d > 0, x), sp.solve_univariate_inequality(d < 0, x)

def concavity(expr):
    expr = sp.sympify(expr)
    dd = sp.diff(expr, x, 2)
    return sp.solve_univariate_inequality(dd > 0, x), sp.solve_univariate_inequality(dd < 0, x)

def inflection_points(expr):
    expr = sp.sympify(expr)
    dd = sp.diff(expr, x, 2)
    points = sp.solve(dd, x)
    return points

def average_value(expr, a, b):
    expr = sp.sympify(expr)
    return sp.integrate(expr, (x, a, b)) / (b - a)

def area_between_curves(expr1, expr2, a, b):
    expr1 = sp.sympify(expr1)
    expr2 = sp.sympify(expr2)
    return sp.integrate(abs(expr1 - expr2), (x, a, b))

def arc_length(expr, a, b):
    expr = sp.sympify(expr)
    d = sp.diff(expr, x)
    return sp.integrate(sp.sqrt(1 + d**2), (x, a, b))

def disk_volume(expr, a, b):
    expr = sp.sympify(expr)
    return sp.pi * sp.integrate(expr**2, (x, a, b))

def washer_volume(outer, inner, a, b):
    outer = sp.sympify(outer)
    inner = sp.sympify(inner)
    return sp.pi * sp.integrate(outer**2 - inner**2, (x, a, b))

def newtons_method(expr, guess, iterations=5):
    expr = sp.sympify(expr)
    d = sp.diff(expr, x)

    current = sp.Float(guess)

    for _ in range(iterations):
        current = current - expr.subs(x, current) / d.subs(x, current)

    return sp.N(current)