from formula_display.formula_display_core import *

def work():
    return make_formula(
        "W = Fd",
        {
            "W": "work",
            "F": "force",
            "d": "distance"
        },
        units="joules",
        topic="Work"
    )

def kinetic_energy():
    return make_formula(
        "KE = ½mv²",
        {
            "KE": "kinetic energy",
            "m": "mass",
            "v": "velocity"
        },
        units="joules",
        topic="Kinetic Energy"
    )
def force():
    return make_formula(
        "F = ma",
        {
            "F": "force",
            "m": "mass",
            "a": "acceleration"
        },
        units="newtons",
        topic="Force"
    )
def momentum():
    return make_formula(
        "p = mv",
        {
            "p": "momentum",
            "m": "mass",
            "v": "velocity"
        },
        units="kg·m/s",
        topic="Momentum"
    )