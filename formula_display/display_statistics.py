from formula_display.formula_display_core import *

def mean():
    return make_formula(
        "Mean = Σx / n",
        {
            "Σx": "sum of all values",
            "n": "number of values"
        },
        topic="Arithmetic Mean"
    )

def range():
    return make_formula(
        "Range = max(x) - min(x)",
        {
            "max(x)": "maximum value",
            "min(x)": "minimum value"
        },
        topic="Range"
    )

def simple_interest():
    return make_formula(
        "I = Prt",
        {
            "I": "interest",
            "P": "principal",
            "r": "interest rate",
            "t": "time"
        },
        units="currency",
        topic="Simple Interest"
    )


def compound_interest():
    return make_formula(
        "A = P(1 + r/n)^(nt)",
        {
            "A": "final amount",
            "P": "principal",
            "r": "annual interest rate",
            "n": "compounds per year",
            "t": "time (years)"
        },
        units="currency",
        topic="Compound Interest"
    )