import inspect

from formulas import (
    algebra,
    calculus,
    conversions,
    geometry,
    physics,
    statistics,
    linear_algebra,
)

MODULES = {
    "Algebra": algebra,
    "Calculus": calculus,
    "Conversions": conversions,
    "Geometry": geometry,
    "Physics": physics,
    "Statistics": statistics,
    "Linear Algebra": linear_algebra,
}


def formula_count():
    total = 0

    for module in MODULES.values():
        total += len(inspect.getmembers(module, inspect.isfunction))

    return total


def module_count():
    return len(MODULES)


def module_breakdown():
    return {
        name: len(inspect.getmembers(module, inspect.isfunction))
        for name, module in MODULES.items()
    }