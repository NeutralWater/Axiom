from formula_display.core import *


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


def speed():
    return make_formula(
        "v = d / t",
        {
            "v": "speed",
            "d": "distance",
            "t": "time"
        },
        units="m/s",
        topic="Speed"
    )


def acceleration():
    return make_formula(
        "a = (vf - vi) / t",
        {
            "a": "acceleration",
            "vf": "final velocity",
            "vi": "initial velocity",
            "t": "time"
        },
        units="m/s²",
        topic="Acceleration"
    )


def displacement_average_velocity():
    return make_formula(
        "d = ((vi + vf) / 2)t",
        {
            "d": "displacement",
            "vi": "initial velocity",
            "vf": "final velocity",
            "t": "time"
        },
        units="meters",
        topic="Displacement"
    )


def displacement_acceleration():
    return make_formula(
        "d = vit + ½at²",
        {
            "d": "displacement",
            "vi": "initial velocity",
            "t": "time",
            "a": "acceleration"
        },
        units="meters",
        topic="Displacement with Acceleration"
    )


def final_velocity():
    return make_formula(
        "vf = vi + at",
        {
            "vf": "final velocity",
            "vi": "initial velocity",
            "a": "acceleration",
            "t": "time"
        },
        units="m/s",
        topic="Final Velocity"
    )


def final_velocity_squared():
    return make_formula(
        "vf² = vi² + 2ad",
        {
            "vf": "final velocity",
            "vi": "initial velocity",
            "a": "acceleration",
            "d": "displacement"
        },
        units="m²/s²",
        topic="Final Velocity Squared"
    )


def free_fall_time():
    return make_formula(
        "t = √(2h / g)",
        {
            "t": "time",
            "h": "height",
            "g": "gravity"
        },
        units="seconds",
        topic="Free Fall Time"
    )


def weight():
    return make_formula(
        "Fg = mg",
        {
            "Fg": "weight force",
            "m": "mass",
            "g": "gravity"
        },
        units="newtons",
        topic="Weight"
    )


def friction():
    return make_formula(
        "Ff = μFn",
        {
            "Ff": "friction force",
            "μ": "coefficient of friction",
            "Fn": "normal force"
        },
        units="newtons",
        topic="Friction"
    )


def normal_force():
    return make_formula(
        "Fn = mg",
        {
            "Fn": "normal force",
            "m": "mass",
            "g": "gravity"
        },
        units="newtons",
        topic="Normal Force"
    )


def gravitational_force():
    return make_formula(
        "F = Gm₁m₂ / r²",
        {
            "F": "gravitational force",
            "G": "gravitational constant",
            "m₁": "first mass",
            "m₂": "second mass",
            "r": "distance between centers"
        },
        units="newtons",
        topic="Universal Gravitation"
    )


def centripetal_force():
    return make_formula(
        "Fc = mv² / r",
        {
            "Fc": "centripetal force",
            "m": "mass",
            "v": "velocity",
            "r": "radius"
        },
        units="newtons",
        topic="Centripetal Force"
    )


def centripetal_acceleration():
    return make_formula(
        "ac = v² / r",
        {
            "ac": "centripetal acceleration",
            "v": "velocity",
            "r": "radius"
        },
        units="m/s²",
        topic="Centripetal Acceleration"
    )


def potential_energy():
    return make_formula(
        "PE = mgh",
        {
            "PE": "potential energy",
            "m": "mass",
            "g": "gravity",
            "h": "height"
        },
        units="joules",
        topic="Potential Energy"
    )


def mechanical_energy():
    return make_formula(
        "ME = KE + PE",
        {
            "ME": "mechanical energy",
            "KE": "kinetic energy",
            "PE": "potential energy"
        },
        units="joules",
        topic="Mechanical Energy"
    )


def power():
    return make_formula(
        "P = W / t",
        {
            "P": "power",
            "W": "work",
            "t": "time"
        },
        units="watts",
        topic="Power"
    )


def efficiency():
    return make_formula(
        "Efficiency = (output work / input work) × 100",
        {
            "output work": "useful work produced",
            "input work": "total work supplied"
        },
        units="percent",
        topic="Efficiency"
    )


def impulse():
    return make_formula(
        "J = Ft",
        {
            "J": "impulse",
            "F": "force",
            "t": "time"
        },
        units="N·s",
        topic="Impulse"
    )


def change_in_momentum():
    return make_formula(
        "Δp = pf - pi",
        {
            "Δp": "change in momentum",
            "pf": "final momentum",
            "pi": "initial momentum"
        },
        units="kg·m/s",
        topic="Change in Momentum"
    )


def wave_speed():
    return make_formula(
        "v = fλ",
        {
            "v": "wave speed",
            "f": "frequency",
            "λ": "wavelength"
        },
        units="m/s",
        topic="Wave Speed"
    )


def frequency():
    return make_formula(
        "f = v / λ",
        {
            "f": "frequency",
            "v": "wave speed",
            "λ": "wavelength"
        },
        units="hertz",
        topic="Frequency"
    )


def wavelength():
    return make_formula(
        "λ = v / f",
        {
            "λ": "wavelength",
            "v": "wave speed",
            "f": "frequency"
        },
        units="meters",
        topic="Wavelength"
    )


def period():
    return make_formula(
        "T = 1 / f",
        {
            "T": "period",
            "f": "frequency"
        },
        units="seconds",
        topic="Period"
    )


def frequency_from_period():
    return make_formula(
        "f = 1 / T",
        {
            "f": "frequency",
            "T": "period"
        },
        units="hertz",
        topic="Frequency from Period"
    )


def ohms_law():
    return make_formula(
        "I = V / R",
        {
            "I": "current",
            "V": "voltage",
            "R": "resistance"
        },
        units="amps",
        topic="Ohm's Law"
    )


def voltage():
    return make_formula(
        "V = IR",
        {
            "V": "voltage",
            "I": "current",
            "R": "resistance"
        },
        units="volts",
        topic="Voltage"
    )


def resistance():
    return make_formula(
        "R = V / I",
        {
            "R": "resistance",
            "V": "voltage",
            "I": "current"
        },
        units="ohms",
        topic="Resistance"
    )


def electrical_power_vi():
    return make_formula(
        "P = VI",
        {
            "P": "electrical power",
            "V": "voltage",
            "I": "current"
        },
        units="watts",
        topic="Electrical Power"
    )


def electrical_power_i2r():
    return make_formula(
        "P = I²R",
        {
            "P": "electrical power",
            "I": "current",
            "R": "resistance"
        },
        units="watts",
        topic="Electrical Power"
    )


def electrical_power_v2r():
    return make_formula(
        "P = V² / R",
        {
            "P": "electrical power",
            "V": "voltage",
            "R": "resistance"
        },
        units="watts",
        topic="Electrical Power"
    )


def charge():
    return make_formula(
        "q = It",
        {
            "q": "charge",
            "I": "current",
            "t": "time"
        },
        units="coulombs",
        topic="Charge"
    )


def current():
    return make_formula(
        "I = q / t",
        {
            "I": "current",
            "q": "charge",
            "t": "time"
        },
        units="amps",
        topic="Current"
    )


def resistance_series():
    return make_formula(
        "Rt = R₁ + R₂ + R₃ + ...",
        {
            "Rt": "total resistance",
            "R₁, R₂, R₃": "individual resistors"
        },
        units="ohms",
        topic="Series Resistance"
    )


def resistance_parallel():
    return make_formula(
        "1/Rt = 1/R₁ + 1/R₂ + 1/R₃ + ...",
        {
            "Rt": "total resistance",
            "R₁, R₂, R₃": "individual resistors"
        },
        units="ohms",
        topic="Parallel Resistance"
    )


def coulombs_law():
    return make_formula(
        "F = kq₁q₂ / r²",
        {
            "F": "electric force",
            "k": "Coulomb's constant",
            "q₁": "first charge",
            "q₂": "second charge",
            "r": "distance between charges"
        },
        units="newtons",
        topic="Coulomb's Law"
    )


def electric_field():
    return make_formula(
        "E = F / q",
        {
            "E": "electric field",
            "F": "force",
            "q": "charge"
        },
        units="N/C",
        topic="Electric Field"
    )