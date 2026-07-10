import inspect
import importlib
import pkgutil

import formulas
import formula_display
from formulas.constant_values import CONSTANT_COUNT

TEXT_PARAMETERS = {
    "calculus": {"e", "expr", "expr1", "expr2", "outer", "inner", "value"},
    "digital_electronics": {"e", "expression"},
}

VECTOR_PARAMETERS = {
    "linear_algebra": {"v", "v1", "v2", "u", "b"},
    "statistics": {"values"},
}

VECTOR_SET_PARAMETERS = {
    "linear_algebra": {"vectors"},
}

MATRIX_PARAMETERS = {
    "linear_algebra": {"A", "B"},
}

INTEGER_PARAMETERS = {"iterations", "n"}




def make_label(name):
    return name.replace("_", " ").title()


def input_definition(module_id, parameter_name, parameter):
    input_type = "number"
    placeholder = f"Enter {make_label(parameter_name).lower()}"

    if parameter_name in TEXT_PARAMETERS.get(module_id, set()):
        input_type = "text"
        placeholder = "Example: x^2 + 3*x"
    elif parameter_name in MATRIX_PARAMETERS.get(module_id, set()):
        input_type = "matrix"
    elif parameter_name in VECTOR_SET_PARAMETERS.get(module_id, set()):
        input_type = "vectors"
        placeholder = "Example: 1, 0; 0, 1"
    elif parameter_name in VECTOR_PARAMETERS.get(module_id, set()):
        input_type = "vector"
        placeholder = "Example: 1, 2, 3"
    elif parameter_name in INTEGER_PARAMETERS:
        input_type = "integer"

    data = {
        "name": parameter_name,
        "label": make_label(parameter_name),
        "type": input_type,
        "placeholder": placeholder,
    }

    if parameter.default is not inspect.Parameter.empty:
        data["default"] = parameter.default

    return data


def build_solvers(module_id, formula_module, display_module):
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
                input_definition(module_id, parameter_name, parameter)
                for parameter_name, parameter in parameters.items()
            ],
        }

    return solvers


MODULES = {}
SOLVERS = {}

for module_info in pkgutil.iter_modules(formulas.__path__):
    module_id = module_info.name

    if module_id.startswith("__") or module_id == "constant_values":
        continue

    try:
        formula_module = importlib.import_module(f"formulas.{module_id}")
        display_module = importlib.import_module(
            f"formula_display.display_{module_id}"
        )
    except ModuleNotFoundError:
        continue

    solvers = build_solvers(module_id, formula_module, display_module)

    if not solvers:
        continue

    MODULES[module_id] = {
        "name": make_label(module_id),
        "icon": "🧠",
        "description": f"{len(solvers)} tools available",
    }

    SOLVERS[module_id] = solvers

MODULES["constants"] = {
    "name": "Constants",
    "icon": "📚",
    "description": f"{CONSTANT_COUNT} reference values available",
    "href": "/constants",
}
