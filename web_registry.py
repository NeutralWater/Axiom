import inspect
import importlib
import pkgutil

import formulas
import formula_display


def make_label(name):
    return name.replace("_", " ").title()


def build_solvers(formula_module, display_module):
    solvers = {}

    for name, function in inspect.getmembers(formula_module, inspect.isfunction):
        display_function = getattr(display_module, name, None)

        if display_function is None:
            continue

        parameters = inspect.signature(function).parameters

        solvers[name] = {
            "name": make_label(name),
            "function": function,
            "display": display_function,
            "inputs": [
                {
                    "name": parameter_name,
                    "label": make_label(parameter_name),
                }
                for parameter_name in parameters
            ],
        }

    return solvers


MODULES = {}
SOLVERS = {}

for module_info in pkgutil.iter_modules(formulas.__path__):
    module_id = module_info.name

    if module_id.startswith("__"):
        continue

    try:
        formula_module = importlib.import_module(f"formulas.{module_id}")
        display_module = importlib.import_module(
            f"formula_display.display_{module_id}"
        )
    except ModuleNotFoundError:
        continue

    solvers = build_solvers(formula_module, display_module)

    if not solvers:
        continue

    MODULES[module_id] = {
        "name": make_label(module_id),
        "icon": "🧠",
        "description": f"{len(solvers)} tools available",
    }

    SOLVERS[module_id] = solvers