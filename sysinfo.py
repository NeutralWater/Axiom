import inspect

from formulas import (
    algebra,
    calculus,
    conversions,
    geometry,
    physics,
    statistics,
    linear_algebra,
    chemistry,
    astronomy,
    computer_science,

)

MODULES = {
    "Algebra": algebra,
    "Calculus": calculus,
    "Conversions": conversions,
    "Geometry": geometry,
    "Physics": physics,
    "Statistics": statistics,
    "Linear Algebra": linear_algebra,
    "Chemistry": chemistry,
    "Astronomy": astronomy,
    "Computer Science": computer_science
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