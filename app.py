from flask import Flask, render_template, request
from web_registry import MODULES, SOLVERS

app = Flask(__name__)


def get_value(obj, key, default=None):
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


@app.route("/")
def home():
    return render_template("index.html", modules=MODULES)


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
                raw_value = request.form[name]
                number = float(raw_value)

                values[name] = number
                args.append(number)

            result = solver["function"](*args)
            result = round(result, 6)

        except ValueError:
            error = "Enter valid numbers."
        except Exception as e:
            error = str(e)

    formula = get_value(display_data, "formula", "")
    variables = get_value(display_data, "variables", {})
    units = get_value(display_data, "units", "")
    topic = get_value(display_data, "topic", solver["name"])

    return render_template(
        "solver.html",
        module_id=module_id,
        solver=solver,
        formula=formula,
        variables=variables,
        units=units,
        topic=topic,
        values=values,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)