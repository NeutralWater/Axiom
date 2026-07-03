from formula_display.core import *


def torque():
    return make_formula(
        "τ = Fr",
        {
            "τ": "torque",
            "F": "force",
            "r": "lever arm"
        },
        units="N·m",
        topic="Torque"
    )


def angular_velocity():
    return make_formula(
        "ω = θ / t",
        {
            "ω": "angular velocity",
            "θ": "angular displacement",
            "t": "time"
        },
        units="rad/s",
        topic="Angular Velocity"
    )


def angular_acceleration():
    return make_formula(
        "α = (ωf - ωi) / t",
        {
            "α": "angular acceleration",
            "ωf": "final angular velocity",
            "ωi": "initial angular velocity",
            "t": "time"
        },
        units="rad/s²",
        topic="Angular Acceleration"
    )


def rotational_kinetic_energy():
    return make_formula(
        "KErot = ½Iω²",
        {
            "KErot": "rotational kinetic energy",
            "I": "moment of inertia",
            "ω": "angular velocity"
        },
        units="joules",
        topic="Rotational Kinetic Energy"
    )


def moment_of_inertia():
    return make_formula(
        "I = mr²",
        {
            "I": "moment of inertia",
            "m": "mass",
            "r": "radius"
        },
        units="kg·m²",
        topic="Moment of Inertia"
    )


def rotational_power():
    return make_formula(
        "P = τω",
        {
            "P": "rotational power",
            "τ": "torque",
            "ω": "angular velocity"
        },
        units="watts",
        topic="Rotational Power"
    )


def mechanical_advantage():
    return make_formula(
        "MA = Fout / Fin",
        {
            "MA": "mechanical advantage",
            "Fout": "output force",
            "Fin": "input force"
        },
        topic="Mechanical Advantage"
    )


def gear_ratio():
    return make_formula(
        "GR = driven teeth / driver teeth",
        {
            "GR": "gear ratio",
            "driven teeth": "teeth on the driven gear",
            "driver teeth": "teeth on the driver gear"
        },
        topic="Gear Ratio"
    )


def stress():
    return make_formula(
        "σ = F / A",
        {
            "σ": "stress",
            "F": "force",
            "A": "cross-sectional area"
        },
        units="pascals",
        topic="Stress"
    )


def strain():
    return make_formula(
        "ε = ΔL / L₀",
        {
            "ε": "strain",
            "ΔL": "change in length",
            "L₀": "original length"
        },
        topic="Strain"
    )


def youngs_modulus():
    return make_formula(
        "E = σ / ε",
        {
            "E": "Young's modulus",
            "σ": "stress",
            "ε": "strain"
        },
        units="pascals",
        topic="Young's Modulus"
    )


def shear_stress():
    return make_formula(
        "τ = F / A",
        {
            "τ": "shear stress",
            "F": "force",
            "A": "area"
        },
        units="pascals",
        topic="Shear Stress"
    )


def shear_strain():
    return make_formula(
        "γ = x / h",
        {
            "γ": "shear strain",
            "x": "lateral displacement",
            "h": "height"
        },
        topic="Shear Strain"
    )


def spring_force():
    return make_formula(
        "F = kx",
        {
            "F": "spring force",
            "k": "spring constant",
            "x": "displacement"
        },
        units="newtons",
        topic="Spring Force"
    )


def spring_potential_energy():
    return make_formula(
        "PE = ½kx²",
        {
            "PE": "spring potential energy",
            "k": "spring constant",
            "x": "displacement"
        },
        units="joules",
        topic="Spring Potential Energy"
    )


def hookes_law():
    return make_formula(
        "F = kx",
        {
            "F": "restoring force",
            "k": "spring constant",
            "x": "displacement"
        },
        units="newtons",
        topic="Hooke's Law"
    )


def thermal_expansion():
    return make_formula(
        "ΔL = αL₀ΔT",
        {
            "ΔL": "change in length",
            "α": "coefficient of linear expansion",
            "L₀": "original length",
            "ΔT": "change in temperature"
        },
        units="meters",
        topic="Thermal Expansion"
    )


def linear_expansion():
    return make_formula(
        "L = L₀(1 + αΔT)",
        {
            "L": "final length",
            "L₀": "original length",
            "α": "coefficient of linear expansion",
            "ΔT": "change in temperature"
        },
        units="meters",
        topic="Linear Expansion"
    )


def safety_factor():
    return make_formula(
        "SF = material strength / applied stress",
        {
            "SF": "safety factor",
            "material strength": "maximum allowable strength",
            "applied stress": "working stress"
        },
        topic="Safety Factor"
    )


def beam_bending_stress():
    return make_formula(
        "σ = My / I",
        {
            "σ": "bending stress",
            "M": "bending moment",
            "y": "distance from neutral axis",
            "I": "area moment of inertia"
        },
        units="pascals",
        topic="Beam Bending Stress"
    )