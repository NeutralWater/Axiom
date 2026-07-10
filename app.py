import json

from flask import Flask, render_template, request
from website.web_registry import MODULES, SOLVERS
from formulas.constant_values import CONSTANT_GROUPS

app = Flask(
    __name__,
    template_folder="website/templates",
    static_folder="website/static",
)


def get_value(obj, key, default=None):
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def parse_number(value):
    number = float(value)
    return int(number) if number.is_integer() else number


def parse_vector(value):
    parts = value.replace("[", "").replace("]", "").split(",")
    values = [parse_number(part.strip()) for part in parts if part.strip()]
    if not values:
        raise ValueError("Enter at least one value.")
    return values


def parse_input(input_data, raw_value):
    input_type = input_data["type"]
    raw_value = raw_value.strip()

    if input_type == "text":
        if not raw_value:
            raise ValueError("Expression cannot be empty.")
        return raw_value
    if input_type == "integer":
        return int(raw_value)
    if input_type == "vector":
        return parse_vector(raw_value)
    if input_type == "vectors":
        rows = raw_value.replace("\n", ";").split(";")
        vectors = [parse_vector(row) for row in rows if row.strip()]
        if not vectors:
            raise ValueError("Enter at least one vector.")
        return vectors
    if input_type == "matrix":
        matrix = json.loads(raw_value)
        if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) and row for row in matrix):
            raise ValueError("Generate and fill in the matrix.")
        width = len(matrix[0])
        if any(len(row) != width for row in matrix):
            raise ValueError("Every matrix row must have the same number of values.")
        return [[parse_number(str(value)) for value in row] for row in matrix]
    return parse_number(raw_value)


def format_result(value):
    if isinstance(value, float):
        return str(round(value, 6))
    if isinstance(value, (list, tuple, dict)):
        return str(value)
    return str(value)


@app.route("/")
def home():
    return render_template("index.html", modules=MODULES)

@app.route("/constants")
def constants_page():
    return render_template(
        "constants.html",
        groups=CONSTANT_GROUPS,
    )

@app.route("/module/<module_id>")
def module_page(module_id):
    module = MODULES.get(module_id)
    solvers = SOLVERS.get(module_id, {})

    if module is None:
        return "Module not found", 404

    return render_template(
        "module.html",
        module_id=module_id,
        module=module,
        solvers=solvers
    )

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/solver/<module_id>/<solver_id>", methods=["GET", "POST"])
def solver_page(module_id, solver_id):
    solver = SOLVERS.get(module_id, {}).get(solver_id)

    if solver is None:
        return "Solver not found", 404

    display_data = solver["display"]()

    result = None
    error = None
    values = {}

    if request.method == "POST":
        try:
            args = []

            for input_data in solver["inputs"]:
                name = input_data["name"]
                raw_value = request.form.get(name, "")
                if not raw_value and "default" in input_data:
                    raw_value = str(input_data["default"])
                value = parse_input(input_data, raw_value)

                values[name] = raw_value
                args.append(value)

            result = solver["function"](*args)
            if result is None:
                raise ValueError("The supplied dimensions or values are not valid for this operation.")
            result = format_result(result)

        except (ValueError, json.JSONDecodeError) as e:
            error = str(e) or "Enter valid input values."
        except Exception as e:
            error = str(e)

    formula = get_value(display_data, "formula", "")
    variables = get_value(display_data, "variables", {})
    units = get_value(display_data, "units", "")
    topic = get_value(display_data, "topic", solver["name"])
    notes = get_value(display_data, "notes", "")

    return render_template(
        "solver.html",
        module_id=module_id,
        solver=solver,
        formula=formula,
        variables=variables,
        units=units,
        topic=topic,
        notes=notes,
        values=values,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run()
