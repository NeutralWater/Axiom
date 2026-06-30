from formulas import algebra
from topic_lib import algebra_lib
import math
import formula_display.core as core
import formula_display.display_algebra as fd

def show_formula(formula):
    fd.display_formula(formula)

def run_algebra():
    algebra_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        a = float(input("a value: "))
        b = float(input("b value: "))
        c = float(input("c value: "))
        print("")

        print(f"Discriminant = {algebra.discriminant(a, b, c)}")
        show_formula(fd.discriminant())
        print("")

    elif choice == "2":
        a = float(input("a value: "))
        b = float(input("b value: "))
        c = float(input("c value: "))
        print("")

        r = algebra.quadratic(a, b, c)

        if r is None:
            print("Not a quadratic equation.")
        elif len(r) == 0:
            print("No real solutions.")
        elif len(r) == 1:
            print(f"x = {r[0]}")
        else:
            print(f"1st Root = {r[0]}")
            print(f"2nd Root = {r[1]}")

        show_formula(fd.quadratic())
        print("")

    elif choice == "3":
        x1 = float(input("x1 value: "))
        y1 = float(input("y1 value: "))
        x2 = float(input("x2 value: "))
        y2 = float(input("y2 value: "))
        print("")

        r = algebra.slope(x1, y1, x2, y2)

        if r is None:
            print("Undefined slope.")
        else:
            print(f"Slope = {r}")

        show_formula(fd.slope())
        print("")

    elif choice == "4":
        x1 = float(input("x1 value: "))
        y1 = float(input("y1 value: "))
        x2 = float(input("x2 value: "))
        y2 = float(input("y2 value: "))
        print("")

        print(f"Midpoint = {algebra.midpoint(x1, y1, x2, y2)}")
        show_formula(fd.midpoint())
        print("")

    elif choice == "5":
        x1 = float(input("x1 value: "))
        y1 = float(input("y1 value: "))
        x2 = float(input("x2 value: "))
        y2 = float(input("y2 value: "))
        print("")

        print(f"Distance = {algebra.distance(x1, y1, x2, y2)}")
        show_formula(fd.distance())
        print("")
