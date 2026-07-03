import inspect

from formula_display import (
    display_algebra,
    display_astronomy,
    display_calculus,
    display_chemistry,
    display_computer_science,
    display_conversions,
    display_digital_electronics,
    display_electrical_engineering,
    display_geometry,
    display_linear_algebra,
    display_physics,
    display_statistics,
    display_aerospace_engineering,
    display_mechanical_engineering,
)


FORMULA_DISPLAY_MODULES = [
    display_algebra,
    display_astronomy,
    display_calculus,
    display_chemistry,
    display_computer_science,
    display_conversions,
    display_digital_electronics,
    display_electrical_engineering,
    display_geometry,
    display_linear_algebra,
    display_physics,
    display_statistics,
    display_aerospace_engineering,
    display_mechanical_engineering,
]


def count_functions(module):
    return sum(
        1
        for _, func in inspect.getmembers(module, inspect.isfunction)
        if func.__module__ == module.__name__
    )


def formula_count():
    total = 0

    for module in FORMULA_DISPLAY_MODULES:
        total += count_functions(module)

    return total


def module_count():
    return len(FORMULA_DISPLAY_MODULES)