from formula_display.core import make_formula


def density():
    return make_formula(
        "ρ = m / V",
        {"ρ": "density", "m": "mass", "V": "volume"},
        units="g/mL, g/cm³, or kg/m³",
        topic="Density"
    )


def molarity():
    return make_formula(
        "M = n / V",
        {"M": "molarity", "n": "moles of solute", "V": "liters of solution"},
        units="mol/L",
        topic="Molarity"
    )


def molality():
    return make_formula(
        "m = n / kg",
        {"m": "molality", "n": "moles of solute", "kg": "kilograms of solvent"},
        units="mol/kg",
        topic="Molality"
    )


def dilution():
    return make_formula(
        "M₁V₁ = M₂V₂",
        {
            "M₁": "initial molarity",
            "V₁": "initial volume",
            "M₂": "final molarity",
            "V₂": "final volume"
        },
        topic="Dilution",
        notes="Volume units must match."
    )


def heat():
    return make_formula(
        "q = mcΔT",
        {
            "q": "heat energy",
            "m": "mass",
            "c": "specific heat",
            "ΔT": "change in temperature"
        },
        units="joules",
        topic="Heat"
    )


def specific_heat():
    return make_formula(
        "c = q / (mΔT)",
        {
            "c": "specific heat",
            "q": "heat energy",
            "m": "mass",
            "ΔT": "change in temperature"
        },
        units="J/(g°C) or J/(kg·K)",
        topic="Specific Heat"
    )


def boyles_law():
    return make_formula(
        "P₁V₁ = P₂V₂",
        {
            "P₁": "initial pressure",
            "V₁": "initial volume",
            "P₂": "final pressure",
            "V₂": "final volume"
        },
        topic="Boyle's Law",
        notes="Temperature and moles stay constant."
    )


def charles_law():
    return make_formula(
        "V₁ / T₁ = V₂ / T₂",
        {
            "V₁": "initial volume",
            "T₁": "initial temperature",
            "V₂": "final volume",
            "T₂": "final temperature"
        },
        topic="Charles' Law",
        notes="Temperature must be in Kelvin."
    )


def gay_lussac_law():
    return make_formula(
        "P₁ / T₁ = P₂ / T₂",
        {
            "P₁": "initial pressure",
            "T₁": "initial temperature",
            "P₂": "final pressure",
            "T₂": "final temperature"
        },
        topic="Gay-Lussac's Law",
        notes="Temperature must be in Kelvin."
    )


def combined_gas_law():
    return make_formula(
        "(P₁V₁) / T₁ = (P₂V₂) / T₂",
        {
            "P₁": "initial pressure",
            "V₁": "initial volume",
            "T₁": "initial temperature",
            "P₂": "final pressure",
            "V₂": "final volume",
            "T₂": "final temperature"
        },
        topic="Combined Gas Law",
        notes="Temperature must be in Kelvin."
    )


def ideal_gas_law():
    return make_formula(
        "PV = nRT",
        {
            "P": "pressure",
            "V": "volume",
            "n": "moles",
            "R": "ideal gas constant",
            "T": "temperature"
        },
        topic="Ideal Gas Law",
        notes="Default R = 0.0821 L·atm/(mol·K)."
    )