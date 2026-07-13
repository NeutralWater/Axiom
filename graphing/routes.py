import math

from flask import Blueprint, jsonify, render_template, request

from .engine import GraphingError, sample_expression


graphing_bp = Blueprint(
    "graphing",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/assets",
)


@graphing_bp.get("/")
def graphing_page():
    return render_template("graphing.html")


@graphing_bp.post("/api")
def graph_data():
    payload = request.get_json(silent=True) or {}
    expressions = payload.get("expressions", [])

    if not isinstance(expressions, list):
        return jsonify(
            error="Expressions must be a list."
        ), 400

    try:
        x_min = float(payload.get("x_min", -10))
        x_max = float(payload.get("x_max", 10))
        samples = int(payload.get("samples", 801))

    except (TypeError, ValueError):
        return jsonify(
            error="Enter valid graph bounds."
        ), 400

    if not math.isfinite(x_min) or not math.isfinite(x_max):
        return jsonify(
            error="Graph bounds must be finite numbers."
        ), 400

    traces = []
    errors = []

    for index, item in enumerate(expressions, start=1):
        expression = str(
            item.get("expression", "")
        ).strip()

        if not expression:
            continue

        try:
            graph = sample_expression(
                expression,
                x_min,
                x_max,
                samples,
            )

            traces.append({
                **graph,
                "name": item.get("name") or f"y = {expression}",
                "color": item.get("color") or "#60a5fa",
            })

        except GraphingError as error:
            errors.append(f"Row {index}: {error}")

    if not traces:
        return jsonify(
            error=" ".join(errors)
            or "Add at least one function to graph."
        ), 400

    return jsonify(
        traces=traces,
        errors=errors,
    )