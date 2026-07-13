import math
import re

import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    parse_expr,
    standard_transformations,
)


x = sp.Symbol("x", real=True)

MAX_ABSOLUTE_Y = 1_000_000

ALLOWED_NAMES = {
    "x": x,
    "pi": sp.pi,
    "e": sp.E,
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "sinh": sp.sinh,
    "cosh": sp.cosh,
    "tanh": sp.tanh,
    "sqrt": sp.sqrt,
    "log": sp.log,
    "ln": sp.log,
    "exp": sp.exp,
    "abs": sp.Abs,
}


class GraphingError(ValueError):
    pass


def normalize_expression(expression):
    expression = str(expression).strip()

    expression = re.sub(
        r"^\s*y\s*=\s*",
        "",
        expression,
        flags=re.IGNORECASE,
    )

    expression = expression.replace("^", "**")

    if not expression:
        raise GraphingError(
            "Enter a function, such as x^2 or sin(x)."
        )

    return expression


def parse_expression(expression):
    source = normalize_expression(expression)

    names = set(re.findall(r"[A-Za-z_]\w*", source))
    unknown_names = names - set(ALLOWED_NAMES)

    if unknown_names:
        names = ", ".join(sorted(unknown_names))

        raise GraphingError(
            f"Use x as the graph variable. Unknown: {names}."
        )

    try:
        parsed = parse_expr(
            source,
            local_dict=ALLOWED_NAMES,
            global_dict={
                "__builtins__": {},
                "Integer": sp.Integer,
                "Float": sp.Float,
                "Rational": sp.Rational,
            },
            transformations=standard_transformations + (convert_xor,),
        )

    except (NameError, SyntaxError, TypeError, ValueError) as error:
        raise GraphingError(
            "Axiom could not read that expression."
        ) from error

    if not isinstance(parsed, sp.Expr):
        raise GraphingError(
            "Enter a mathematical expression in x."
        )

    return parsed


def sample_expression(
    expression,
    x_min=-10,
    x_max=10,
    samples=801,
):
    if x_min >= x_max:
        raise GraphingError(
            "The minimum x value must be smaller than the maximum."
        )

    if samples < 2 or samples > 2000:
        raise GraphingError(
            "Choose between 2 and 2,000 sample points."
        )

    parsed = parse_expression(expression)

    try:
        function = sp.lambdify(
            x,
            parsed,
            modules=["math"],
        )

    except (TypeError, ValueError) as error:
        raise GraphingError(
            "Axiom could not turn that expression into a graph."
        ) from error

    step = (x_max - x_min) / (samples - 1)

    x_values = []
    y_values = []

    for index in range(samples):
        x_value = x_min + index * step
        x_values.append(x_value)

        try:
            y_value = function(x_value)

            if isinstance(y_value, complex):
                y_values.append(None)
                continue

            y_value = float(y_value)

            if (
                not math.isfinite(y_value)
                or abs(y_value) > MAX_ABSOLUTE_Y
            ):
                y_values.append(None)
            else:
                y_values.append(y_value)

        except Exception:
            y_values.append(None)

    return {
        "expression": str(parsed),
        "x": x_values,
        "y": y_values,
    }