from formula_display.core import make_formula

def simplify_boolean_expression():
    return make_formula(
        "Simplified Boolean Expression",
        {
            "AND": "logical conjuction",
            "OR": "logical disjunction",
            "NOT": "logical negation",
            "XOR": "exclusive OR",
        },
        topic = "Boolean Algebra Simplifier",
        notes="Accepts expressions using AND, OR, NOT, XOR, &, |, ~, and ^."
    )

def format_truth_table():
    return make_formula(
        "F = expression(A, B, C, ...)",
        {
            "F": "output value",
            "A, B, C": "Boolean input variables",
            "0": "false",
            "1": "true",
        },
        topic="Truth Table Generator",
        notes="Generates every input combination and evalutes the Boolean expression."
    )

def generate_kmap():
    return make_formula(
        "K=Map = truth table arranged in Gray code order",
        {
            "K-map" : "Karnaugh Map",
            "Gray code": "ordering where only one bit changed between adjacent cells",
            "0": "false output",
            "1": "true output",
        },
        topic="Karnaugh Map Generator",
        notes="Supports Boolean expressions with 2-6 variables."
    )
