from sympy import symbols
from sympy.logic.boolalg import *
from sympy.parsing.sympy_parser import * 
import itertools
import re


def normalize_boolean_expression(expression):
    expression = expression.upper()
    replacements = {
        "XOR": "^",
        "AND": "&",
        "NOT": "~",
        "OR": "|",
    }
    for word, operator in replacements.items():
        expression = re.sub(rf"\b{word}\b", operator, expression)
    return expression

def simplify_boolean_expression(e):
    e = normalize_boolean_expression(e)
    
    p = parse_expr(e, evaluate=True)
    s = simplify_logic(p, form="cnf")
    
    return s

# from line 17 to line 63 is all just to generate a truth table
def clean_boolean_variables(e):
    return normalize_boolean_expression(e)

def get_boolean_variables(e):
    c = clean_boolean_variables(e)
    v = sorted(set(char for char in c if char.isalpha()))
    
    return v

def generate_truth_table(e):
    c = clean_boolean_variables(e)
    v = get_boolean_variables(c)
    
    symbol_map = {var: symbols(var) for var in v}
    p = parse_expr(c, local_dict=symbol_map, evaluate=True)

    rows = []
    for values in itertools.product([False, True], repeat=len(v)):
        value_map = dict(zip(v,values))
        r = bool(p.subs(value_map))

        rows.append({
            "inputs" : [int(v) for v in values],
            "output": int(r)
        })
    return v, rows

def format_truth_table(e):
    v, rows = generate_truth_table(e)

    header = " ".join(v) + " | F"
    divider = "-" * len(header)

    lines = [header, divider]

    for r in rows:
        inputs = " ".join(str(v) for v in r["inputs"])
        lines.append(f"{inputs} | {r['output']}")
    
    return "\n".join(lines)

# from here to 181 is for k map
def gray_code(n):
    if n == 0:
        return [""]
    previous = gray_code(n - 1)
    return (
        ["0" + code for code in previous] +
        ["1" + code for code in reversed(previous)]
    )

def generate_kmap(expression):
    variables, rows = generate_truth_table(expression)
    num_vars = len(variables)

    if num_vars < 2 or num_vars > 6:
        return "K-map supports 2 to 6 variables only."

    truth_outputs = {}

    for row in rows:
        key = "".join(str(bit) for bit in row["inputs"])
        truth_outputs[key] = row["output"]

    row_var_count = num_vars // 2
    col_var_count = num_vars - row_var_count

    row_vars = variables[:row_var_count]
    col_vars = variables[row_var_count:]

    row_codes = gray_code(row_var_count)
    col_codes = gray_code(col_var_count)

    cell_width = max(3, len(col_codes[0]) + 2)
    row_label_width = max(len(row_codes[0]), len("".join(row_vars))) + 2

    col_label = "".join(col_vars)

    table_width = (
        row_label_width
        + 1
        + len(col_codes) * cell_width
        + len(col_codes)
        + 1
    )

    col_label_padding = max(
        0,
        row_label_width + 1 + ((table_width - row_label_width - 1) // 2) - (len(col_label) // 2)
    )

    lines = []
    lines.append("Karnaugh Map")
    lines.append("")
    lines.append("Rows: " + "".join(row_vars))
    lines.append("Cols: " + col_label)
    lines.append("")
    lines.append(" " * col_label_padding + col_label)

    top = (
        "┌"
        + "─" * row_label_width
        + "┬"
        + "┬".join("─" * cell_width for _ in col_codes)
        + "┐"
    )

    header = (
        "│"
        + " " * row_label_width
        + "│"
        + "│".join(f"{code:^{cell_width}}" for code in col_codes)
        + "│"
    )

    divider = (
        "├"
        + "─" * row_label_width
        + "┼"
        + "┼".join("─" * cell_width for _ in col_codes)
        + "┤"
    )

    bottom = (
        "└"
        + "─" * row_label_width
        + "┴"
        + "┴".join("─" * cell_width for _ in col_codes)
        + "┘"
    )

    lines.append(top)
    lines.append(header)
    lines.append(divider)

    for i, row_code in enumerate(row_codes):
        values = []

        for col_code in col_codes:
            key = row_code + col_code
            values.append(str(truth_outputs[key]))

        line = (
            "│"
            + f"{row_code:^{row_label_width}}"
            + "│"
            + "│".join(f"{value:^{cell_width}}" for value in values)
            + "│"
        )

        lines.append(line)

        if i != len(row_codes) - 1:
            lines.append(divider)

    lines.append(bottom)

    return "\n".join(lines)
