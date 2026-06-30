import math
from constants import *
import constants

def constant_topic_lib():
    print("1. Mathematical Constants")
    print("2. Physical Constants")
    print("3. Planck Units")
    print("4. Astronomical Constants")
    
    print("")
    print("0. Exit")
    print("")

def constants_mathematical_lib():
    print("=== Mathematical Constants ===\n")

    print(f"π (Pi): {constants.PI}")
    print("    Ratio of a circle's circumference to its diameter.\n")

    print(f"e (Euler's Number): {constants.E}")
    print("    Base of the natural logarithm.\n")

    print(f"φ (Golden Ratio): {constants.PHI}")
    print("    Appears in geometry, art, and nature.\n")

    print(f"τ (Tau): {constants.TAU}")
    print("    Equal to 2π.\n")
    print("")


def constants_physical_lib():
    print("=== Physical Constants ===\n")

    print(f"Speed of Light (c): {constants.SPEED_OF_LIGHT} m/s")
    print("    Speed of light in a vacuum.\n")

    print(f"Planck Constant (h): {constants.PLANCK_CONSTANT} J·s")
    print("    Relates a photon's energy to its frequency.\n")

    print(f"Gravitational Constant (G): {constants.G} m³·kg⁻¹·s⁻²")
    print("    Determines the strength of gravity.\n")

    print(f"Boltzmann Constant (k): {constants.BOLTZMANN} J/K")
    print("    Relates temperature to particle energy.\n")
    print("")

def constants_planck_lib():
    print("=== Planck Units ===\n")

    print(f"Planck Length: {constants.PLANCK_LENGTH} m")
    print("    Smallest meaningful unit of length.\n")

    print(f"Planck Time: {constants.PLANCK_TIME} s")
    print("    Time light takes to travel one Planck length.\n")

    print(f"Planck Mass: {constants.PLANCK_MASS} kg")
    print("    Fundamental unit of mass in Planck units.\n")
    print("")

def constants_astronomical_lib():
    print("=== Astronomical Constants ===\n")

    print(f"Astronomical Unit (AU): {constants.ASTRONOMICAL_UNIT} m")
    print("    Average distance from Earth to the Sun.\n")

    print(f"Light Year: {constants.LIGHT_YEAR} m")
    print("    Distance light travels in one year.\n")

    print(f"Parsec: {constants.PARSEC} m")
    print("    Standard unit of distance in astronomy.\n")

    print(f"Hubble Constant (H₀): {constants.HUBBLE_CONSTANT} km/s/Mpc")
    print("    Describes the expansion rate of the universe.\n")

    print(f"Rydberg Constant (R∞): {constants.RYDBERG_CONSTANT} m⁻¹")
    print("    Used in atomic spectroscopy.\n")

    print(f"Fine-Structure Constant (α): {constants.FINE_STRUCTURE_CONSTANT}")
    print("    Dimensionless constant governing electromagnetic interactions.\n")

    print(f"Bohr Radius (a₀): {constants.BOHR_RADIUS} m")
    print("    Approximate radius of a hydrogen atom.\n")
    print("")