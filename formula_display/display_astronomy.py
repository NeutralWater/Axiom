from formula_display.core import make_formula


def escape_velocity():
    return make_formula(
        "v = √(2GM/r)",
        {
            "v": "escape velocity",
            "G": "gravitational constant",
            "M": "mass of the celestial body",
            "r": "distance from the center of the body"
        },
        topic="Escape Velocity"
    )


def orbital_velocity():
    return make_formula(
        "v = √(GM/r)",
        {
            "v": "orbital velocity",
            "G": "gravitational constant",
            "M": "mass of the central body",
            "r": "orbital radius"
        },
        topic="Orbital Velocity"
    )


def orbital_period():
    return make_formula(
        "T = 2π√(r³/GM)",
        {
            "T": "orbital period",
            "π": "pi",
            "r": "orbital radius",
            "G": "gravitational constant",
            "M": "mass of the central body"
        },
        topic="Orbital Period"
    )


def gravitational_force():
    return make_formula(
        "F = Gm₁m₂/r²",
        {
            "F": "gravitational force",
            "G": "gravitational constant",
            "m₁": "mass of the first object",
            "m₂": "mass of the second object",
            "r": "distance between the centers of the objects"
        },
        topic="Newton's Law of Gravitation"
    )


def surface_gravity():
    return make_formula(
        "g = GM/r²",
        {
            "g": "surface gravity",
            "G": "gravitational constant",
            "M": "mass of the planet or star",
            "r": "radius of the planet or star"
        },
        topic="Surface Gravity"
    )


def schwarzschild_radius():
    return make_formula(
        "Rₛ = 2GM/c²",
        {
            "Rₛ": "Schwarzschild radius",
            "G": "gravitational constant",
            "M": "mass of the black hole",
            "c": "speed of light"
        },
        topic="Schwarzschild Radius",
        notes="Objects compressed within this radius become black holes."
    )


def light_travel_time():
    return make_formula(
        "t = d/c",
        {
            "t": "travel time",
            "d": "distance traveled by light",
            "c": "speed of light"
        },
        topic="Light Travel Time"
    )


def parallax_distance():
    return make_formula(
        "d = 1/p",
        {
            "d": "distance in parsecs",
            "p": "parallax angle in arcseconds"
        },
        topic="Parallax Distance",
        notes="Distance is measured in parsecs."
    )


def luminosity():
    return make_formula(
        "L = 4πR²σT⁴",
        {
            "L": "luminosity",
            "π": "pi",
            "R": "radius of the star",
            "σ": "Stefan-Boltzmann constant",
            "T": "surface temperature"
        },
        topic="Luminosity"
    )


def flux():
    return make_formula(
        "F = L/(4πd²)",
        {
            "F": "observed flux",
            "L": "luminosity",
            "π": "pi",
            "d": "distance from the source"
        },
        topic="Flux"
    )


def distance_modulus():
    return make_formula(
        "m - M = 5log₁₀(d/10)",
        {
            "m": "apparent magnitude",
            "M": "absolute magnitude",
            "d": "distance in parsecs"
        },
        topic="Distance Modulus",
        notes="Used to determine stellar distances."
    )


def hubbles_law():
    return make_formula(
        "v = H₀d",
        {
            "v": "recession velocity",
            "H₀": "Hubble constant",
            "d": "distance to the galaxy"
        },
        topic="Hubble's Law"
    )


def redshift_velocity():
    return make_formula(
        "v = zc",
        {
            "v": "velocity",
            "z": "redshift",
            "c": "speed of light"
        },
        topic="Redshift Velocity",
        notes="Accurate only for relatively small redshifts."
    )


def keplers_third_law():
    return make_formula(
        "T² = (4π²r³)/(GM)",
        {
            "T": "orbital period",
            "π": "pi",
            "r": "orbital radius",
            "G": "gravitational constant",
            "M": "mass of the central body"
        },
        topic="Kepler's Third Law"
    )


def wiens_law():
    return make_formula(
        "λₘₐₓ = b/T",
        {
            "λₘₐₓ": "peak wavelength",
            "b": "Wien's displacement constant",
            "T": "temperature"
        },
        topic="Wien's Law"
    )


def stefan_boltzmann():
    return make_formula(
        "P = σAT⁴",
        {
            "P": "radiated power",
            "σ": "Stefan-Boltzmann constant",
            "A": "surface area",
            "T": "absolute temperature"
        },
        topic="Stefan-Boltzmann Law"
    )


def mass_energy():
    return make_formula(
        "E = mc²",
        {
            "E": "energy",
            "m": "mass",
            "c": "speed of light"
        },
        topic="Mass-Energy Equivalence"
    )


def doppler_shift():
    return make_formula(
        "Δλ/λ = v/c",
        {
            "Δλ": "change in wavelength",
            "λ": "original wavelength",
            "v": "relative velocity",
            "c": "speed of light"
        },
        topic="Doppler Shift"
    )


def roche_limit():
    return make_formula(
        "d = 2.44R(M/m)^(1/3)",
        {
            "d": "Roche limit",
            "R": "radius of the larger body",
            "M": "mass of the larger body",
            "m": "mass of the smaller body"
        },
        topic="Roche Limit",
        notes="Inside this distance, tidal forces can tear apart a satellite."
    )


def hill_sphere():
    return make_formula(
        "r = a(M/(3m))^(1/3)",
        {
            "r": "Hill sphere radius",
            "a": "orbital distance",
            "M": "mass of the planet",
            "m": "mass of the star"
        },
        topic="Hill Sphere"
    )


def rocket_equation():
    return make_formula(
        "Δv = Vₑ ln(m₀/mf)",
        {
            "Δv": "change in velocity",
            "Vₑ": "effective exhaust velocity",
            "m₀": "initial mass",
            "mf": "final mass",
            "ln": "natural logarithm"
        },
        topic="Tsiolkovsky Rocket Equation"
    )


def escape_energy():
    return make_formula(
        "E = GMm/r",
        {
            "E": "minimum escape energy",
            "G": "gravitational constant",
            "M": "mass of the celestial body",
            "m": "mass of the escaping object",
            "r": "distance from the center"
        },
        topic="Escape Energy"
    )