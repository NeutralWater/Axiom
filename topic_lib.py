import math
from constants import *
import constants

def menu():
    print("╔══════════════════════════════════════════════╗")
    print("║      MATHEMATICAL COMPUTATION TERMINAL       ║")
    print("║               Version 1.0.0                  ║")
    print("╠══════════════════════════════════════════════╣")
    print("║ Status           : ONLINE                    ║")
    print("║ Formula Modules  : 6 Loaded                  ║")
    print("║ Constant Library : Loaded                    ║")
    print("║ Formula Database : Ready                     ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")
    print("║  [1] Algebra                                 ║")
    print("║  [2] Calculus                                ║")
    print("║  [3] Constants                               ║")
    print("║  [4] Conversions                             ║")
    print("║  [5] Geometry                                ║")
    print("║  [6] Physics                                 ║")
    print("║  [7] Statistics                              ║")
    print("║                                              ║")
    print("║  [0] Exit                                    ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")
    print("")

def algebra_lib():
    print("1. Discrimiant Finder")
    print("2. Quadratic Formula")
    print("3. Slope Formula")
    print("4. Midpoint Formula")
    print("5. Distance Formula")
    print("6. Point Slope Formula")
    print("7. Slope Intercept Formula")

    print("")
    print("0. Exit")
    print("")

def calculus_lib():
    print("1. Derivatives")
    print("2. Second Derivative")
    print("3. Indefinite Integral")
    print("4. Definite Integral")
    print("5. Limit")
    print("6. Critical Points")
    print("7. Tangent Line")
    print("8. Normal Line")

    print("")
    print("0. Exit")
    print("")

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

def conversions_lib():
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    
    print("")
    print("0. Exit")
    print("")
    

def geometry_lib():
    print("║ 2D Geometry ║")
    print("1. Circle Area")
    print("2. Rectangle Area")
    print("3. Triangle Area")
    print("4. Circle Circumference")
    print("5. Rectangle Perimeter")
    print("6. Pythagorean Theorem")
    print("")

    print("║ 3D Volumes ║")
    print("7. Sphere Volume")
    print("8. Cylinder Volume")
    print("9. Cone Volume")
    print("10. Prism Volume")
    print("11. Pyramid Volume")
    print("12. Torus Volume")
    print("13. Ellipsoid Volume")
    print("14. Frustum Volume")
    print("")

    print("║ 3D Surface Areas ║")
    print("15. Sphere Surface Area")
    print("16. Cylinder Surface Area")
    print("17. Cone Surface Area")
    print("18. Prism Surface Area")
    print("19. Pyramid Surface Area")
    print("20. Torus Surface Area")
    print("21. Ellipsoid Surface Area")
    print("22. Frustum Surface Area")
    print("")
    print("0. Exit")
    print("")

def physics_lib():
    print("1. Kinetic Energy")
    print("2. Force")
    print("3. Momentum")
    print("4. Work")

    print("")
    print("0. Exit")
    print("")

def statistics_lib():
    print("1. Mean")
    print("2. Range Value")
    print("3. Simple Interest")
    print("4. Compound Interest")

    print("")
    print("0. Exit")
    print("")

