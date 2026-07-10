import math


# Mathematical Constants
PI = math.pi
E = math.e
PHI = (1 + math.sqrt(5)) / 2
TAU = math.tau


# Mechanics
GRAVITY = 9.81                             # m/s²


# Physical Constants
SPEED_OF_LIGHT = 299792458                 # m/s
PLANCK_CONSTANT = 6.62607015e-34           # J·s
GRAVITATIONAL_CONSTANT = 6.67430e-11       # m³·kg⁻¹·s⁻²
BOLTZMANN_CONSTANT = 1.380649e-23          # J/K


# Electricity
COULOMBS_CONSTANT = 8.9875517923e9         # N·m²/C²
ELEMENTARY_CHARGE = 1.602176634e-19        # C
VACUUM_PERMITTIVITY = 8.8541878128e-12     # F/m
VACUUM_PERMEABILITY = 1.25663706212e-6     # N/A²


# Chemistry
AVOGADRO_CONSTANT = 6.02214076e23          # mol⁻¹
GAS_CONSTANT = 8.314462618                 # J/(mol·K)
FARADAY_CONSTANT = 96485.33212             # C/mol


# Planck Units
PLANCK_LENGTH = 1.616255e-35               # m
PLANCK_TIME = 5.391247e-44                 # s
PLANCK_MASS = 2.176434e-8                  # kg


# Astronomical Constants
ASTRONOMICAL_UNIT = 1.495978707e11         # m
LIGHT_YEAR = 9.4607304725808e15            # m
PARSEC = 3.08567758149137e16               # m
HUBBLE_CONSTANT = 67.4                     # km/s/Mpc


# Atomic Constants
RYDBERG_CONSTANT = 10973731.568160         # m⁻¹
FINE_STRUCTURE_CONSTANT = 7.2973525693e-3  # Dimensionless
BOHR_RADIUS = 5.29177210903e-11            # m


# Radiation Constants
STEFAN_BOLTZMANN_CONSTANT = 5.670374419e-8 # W·m⁻²·K⁻⁴
WIEN_CONSTANT = 2.897771955e-3             # m·K

# Earth / Aerospace Constants
EARTH_MASS = 5.9722e24                     # kg
EARTH_RADIUS = 6371000                     # m
EARTH_MU = 3.986004418e14                  # m³/s²
STANDARD_AIR_DENSITY = 1.225               # kg/m³
SPEED_OF_SOUND = 343                       # m/s

CONSTANT_GROUPS = [
    {
        "category": "Mathematical",
        "constants": [
            {"name": "Pi", "symbol": "π", "value": PI, "units": ""},
            {"name": "Euler's number", "symbol": "e", "value": E, "units": ""},
            {"name": "Golden ratio", "symbol": "φ", "value": PHI, "units": ""},
            {"name": "Tau", "symbol": "τ", "value": TAU, "units": ""},
        ],
    },
    {
        "category": "Mechanics",
        "constants": [
            {
                "name": "Standard gravity",
                "symbol": "g",
                "value": GRAVITY,
                "units": "m/s²",
            },
        ],
    },
    {
        "category": "Physical",
        "constants": [
            {
                "name": "Speed of light",
                "symbol": "c",
                "value": SPEED_OF_LIGHT,
                "units": "m/s",
            },
            {
                "name": "Planck constant",
                "symbol": "h",
                "value": PLANCK_CONSTANT,
                "units": "J·s",
            },
            {
                "name": "Gravitational constant",
                "symbol": "G",
                "value": GRAVITATIONAL_CONSTANT,
                "units": "m³·kg⁻¹·s⁻²",
            },
            {
                "name": "Boltzmann constant",
                "symbol": "k",
                "value": BOLTZMANN_CONSTANT,
                "units": "J/K",
            },
        ],
    },
    {
        "category": "Electricity",
        "constants": [
            {
                "name": "Coulomb constant",
                "symbol": "kₑ",
                "value": COULOMBS_CONSTANT,
                "units": "N·m²/C²",
            },
            {
                "name": "Elementary charge",
                "symbol": "e",
                "value": ELEMENTARY_CHARGE,
                "units": "C",
            },
            {
                "name": "Vacuum permittivity",
                "symbol": "ε₀",
                "value": VACUUM_PERMITTIVITY,
                "units": "F/m",
            },
            {
                "name": "Vacuum permeability",
                "symbol": "μ₀",
                "value": VACUUM_PERMEABILITY,
                "units": "N/A²",
            },
        ],
    },
    {
        "category": "Chemistry",
        "constants": [
            {
                "name": "Avogadro constant",
                "symbol": "Nₐ",
                "value": AVOGADRO_CONSTANT,
                "units": "mol⁻¹",
            },
            {
                "name": "Gas constant",
                "symbol": "R",
                "value": GAS_CONSTANT,
                "units": "J/(mol·K)",
            },
            {
                "name": "Faraday constant",
                "symbol": "F",
                "value": FARADAY_CONSTANT,
                "units": "C/mol",
            },
        ],
    },
    {
        "category": "Planck units",
        "constants": [
            {
                "name": "Planck length",
                "symbol": "lₚ",
                "value": PLANCK_LENGTH,
                "units": "m",
            },
            {
                "name": "Planck time",
                "symbol": "tₚ",
                "value": PLANCK_TIME,
                "units": "s",
            },
            {
                "name": "Planck mass",
                "symbol": "mₚ",
                "value": PLANCK_MASS,
                "units": "kg",
            },
        ],
    },
    {
        "category": "Astronomical",
        "constants": [
            {
                "name": "Astronomical unit",
                "symbol": "AU",
                "value": ASTRONOMICAL_UNIT,
                "units": "m",
            },
            {
                "name": "Light-year",
                "symbol": "ly",
                "value": LIGHT_YEAR,
                "units": "m",
            },
            {
                "name": "Parsec",
                "symbol": "pc",
                "value": PARSEC,
                "units": "m",
            },
            {
                "name": "Hubble constant",
                "symbol": "H₀",
                "value": HUBBLE_CONSTANT,
                "units": "km/s/Mpc",
            },
        ],
    },
    {
        "category": "Atomic",
        "constants": [
            {
                "name": "Rydberg constant",
                "symbol": "R∞",
                "value": RYDBERG_CONSTANT,
                "units": "m⁻¹",
            },
            {
                "name": "Fine-structure constant",
                "symbol": "α",
                "value": FINE_STRUCTURE_CONSTANT,
                "units": "dimensionless",
            },
            {
                "name": "Bohr radius",
                "symbol": "a₀",
                "value": BOHR_RADIUS,
                "units": "m",
            },
        ],
    },
    {
        "category": "Radiation",
        "constants": [
            {
                "name": "Stefan–Boltzmann constant",
                "symbol": "σ",
                "value": STEFAN_BOLTZMANN_CONSTANT,
                "units": "W·m⁻²·K⁻⁴",
            },
            {
                "name": "Wien displacement constant",
                "symbol": "b",
                "value": WIEN_CONSTANT,
                "units": "m·K",
            },
        ],
    },
    {
        "category": "Earth / Aerospace",
        "constants": [
            {
                "name": "Earth mass",
                "symbol": "M⊕",
                "value": EARTH_MASS,
                "units": "kg",
            },
            {
                "name": "Earth radius",
                "symbol": "R⊕",
                "value": EARTH_RADIUS,
                "units": "m",
            },
            {
                "name": "Earth gravitational parameter",
                "symbol": "μ",
                "value": EARTH_MU,
                "units": "m³/s²",
            },
            {
                "name": "Standard air density",
                "symbol": "ρ₀",
                "value": STANDARD_AIR_DENSITY,
                "units": "kg/m³",
            },
            {
                "name": "Speed of sound",
                "symbol": "a",
                "value": SPEED_OF_SOUND,
                "units": "m/s",
            },
        ],
    },
]


CONSTANT_COUNT = sum(
    len(group["constants"])
    for group in CONSTANT_GROUPS
)