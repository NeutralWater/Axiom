from formula_display.core import *


def dynamic_pressure():
    return make_formula(
        "q = ½ρv²",
        {
            "q": "dynamic pressure",
            "ρ": "air density",
            "v": "velocity"
        },
        units="pascals",
        topic="Dynamic Pressure"
    )


def lift():
    return make_formula(
        "L = ½ρv²SCL",
        {
            "L": "lift force",
            "ρ": "air density",
            "v": "velocity",
            "S": "wing area",
            "CL": "lift coefficient"
        },
        units="newtons",
        topic="Lift"
    )


def drag():
    return make_formula(
        "D = ½ρv²SCD",
        {
            "D": "drag force",
            "ρ": "air density",
            "v": "velocity",
            "S": "reference area",
            "CD": "drag coefficient"
        },
        units="newtons",
        topic="Drag"
    )


def lift_to_drag_ratio():
    return make_formula(
        "L/D = L / D",
        {
            "L/D": "lift-to-drag ratio",
            "L": "lift force",
            "D": "drag force"
        },
        topic="Lift-to-Drag Ratio"
    )


def wing_loading():
    return make_formula(
        "WL = W / S",
        {
            "WL": "wing loading",
            "W": "weight",
            "S": "wing area"
        },
        units="N/m²",
        topic="Wing Loading"
    )


def thrust_to_weight_ratio():
    return make_formula(
        "T/W = T / W",
        {
            "T/W": "thrust-to-weight ratio",
            "T": "thrust",
            "W": "weight"
        },
        topic="Thrust-to-Weight Ratio"
    )


def thrust():
    return make_formula(
        "T = ṁve",
        {
            "T": "thrust",
            "ṁ": "mass flow rate",
            "ve": "exhaust velocity"
        },
        units="newtons",
        topic="Thrust"
    )


def mass_flow_rate():
    return make_formula(
        "ṁ = T / ve",
        {
            "ṁ": "mass flow rate",
            "T": "thrust",
            "ve": "exhaust velocity"
        },
        units="kg/s",
        topic="Mass Flow Rate"
    )


def specific_impulse():
    return make_formula(
        "Isp = T / (ṁg)",
        {
            "Isp": "specific impulse",
            "T": "thrust",
            "ṁ": "mass flow rate",
            "g": "gravity"
        },
        units="seconds",
        topic="Specific Impulse"
    )


def effective_exhaust_velocity():
    return make_formula(
        "ve = Ispg",
        {
            "ve": "effective exhaust velocity",
            "Isp": "specific impulse",
            "g": "gravity"
        },
        units="m/s",
        topic="Effective Exhaust Velocity"
    )


def rocket_equation():
    return make_formula(
        "Δv = ve ln(m0 / mf)",
        {
            "Δv": "change in velocity",
            "ve": "exhaust velocity",
            "m0": "initial mass",
            "mf": "final mass"
        },
        units="m/s",
        topic="Tsiolkovsky Rocket Equation"
    )


def escape_velocity():
    return make_formula(
        "v = √(2GM / r)",
        {
            "v": "escape velocity",
            "G": "gravitational constant",
            "M": "mass of planet",
            "r": "distance from planet center"
        },
        units="m/s",
        topic="Escape Velocity"
    )


def earth_escape_velocity():
    return make_formula(
        "v = √(2μ / r)",
        {
            "v": "escape velocity",
            "μ": "Earth gravitational parameter",
            "r": "Earth radius"
        },
        units="m/s",
        topic="Earth Escape Velocity"
    )


def orbital_velocity():
    return make_formula(
        "v = √(μ / r)",
        {
            "v": "orbital velocity",
            "μ": "gravitational parameter",
            "r": "orbital radius"
        },
        units="m/s",
        topic="Orbital Velocity"
    )


def earth_orbital_velocity():
    return make_formula(
        "v = √(μ / r)",
        {
            "v": "orbital velocity",
            "μ": "Earth gravitational parameter",
            "r": "orbital radius"
        },
        units="m/s",
        topic="Earth Orbital Velocity"
    )


def orbital_period():
    return make_formula(
        "T = 2π√(r³ / μ)",
        {
            "T": "orbital period",
            "r": "orbital radius",
            "μ": "gravitational parameter"
        },
        units="seconds",
        topic="Orbital Period"
    )


def earth_orbital_period():
    return make_formula(
        "T = 2π√(r³ / μ)",
        {
            "T": "orbital period",
            "r": "orbital radius",
            "μ": "Earth gravitational parameter"
        },
        units="seconds",
        topic="Earth Orbital Period"
    )


def orbital_energy():
    return make_formula(
        "ε = -μ / 2a",
        {
            "ε": "specific orbital energy",
            "μ": "gravitational parameter",
            "a": "semi-major axis"
        },
        units="J/kg",
        topic="Orbital Energy"
    )


def mach_number():
    return make_formula(
        "M = v / a",
        {
            "M": "Mach number",
            "v": "object velocity",
            "a": "speed of sound"
        },
        topic="Mach Number"
    )


def earth_mach_number():
    return make_formula(
        "M = v / a",
        {
            "M": "Mach number",
            "v": "object velocity",
            "a": "speed of sound at sea level"
        },
        topic="Earth Mach Number"
    )