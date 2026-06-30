from formulas import physics
from topic_lib import physics_lib
import math
import formula_display.core as core
import formula_display.display_physics as fd

def show_formula(formula):
    core.display_formula(formula)

def run_physics():
    physics_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("")
        print(f"Kinetic Energy = {physics.kinetic_energy(m, v)} J")
        show_formula(fd.kinetic_energy())
        print("")
    
    elif choice == "2":
        m = float(input("Mass (kg): "))
        a = float(input("Acceleration (m/s²): "))
        print("")
        print(f"Force = {physics.force(m, a)} N")
        show_formula(fd.force())
        print("")
    
    elif choice == "3":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("")
        print(f"Momentum = {physics.momentum(m, v)} kg·m/s")
        show_formula(fd.momentum())
        print("")
    
    elif choice == "4":
        f = float(input("Force (N): "))
        d = float(input("Distance (m): "))
        print("")
        print(f"Work = {physics.work(f, d)} J")
        show_formula(fd.work())
    
    elif choice == "0":
        exit()