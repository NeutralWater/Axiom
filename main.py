from formulas import algebra, calculus, conversions, geometry, physics, statistics
from topic_lib import *
from runners.algebra_runner import run_algebra
from runners.calculus_runner import run_calculus
from runners.constant_runner import run_constants
from runners.conversions_runner import run_conversions
from runners.geometry_runner import run_geometry
from runners.physics_runner import run_physics
from runners.statistics_runner import run_statistics


def main():
    menu()
    choice = input("Select Module > ")
    print("")

    if choice == "1":
        run_algebra()
    elif choice == "2":
        run_calculus()
    elif choice == "3":
        run_constants()
    elif choice == "4":
        run_conversions()
    elif choice == "5":
        run_geometry()
    elif choice == "6":
        run_physics()
    elif choice == "7":
        run_statistics()
    elif choice == "0":
        exit()
    else:
        print("Invalid choice.")

main()