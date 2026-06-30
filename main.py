from formulas import algebra, calculus, conversions, geometry, physics, statistics
from topic_lib import *
import formula_display


def show_formula(formula):
    formula_display.display_formula(formula)


def run_algebra():
    algebra_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        a = float(input("a value: "))
        b = float(input("b value: "))
        c = float(input("c value: "))
        print("")

        print(f"Discriminant = {algebra.discriminant(a, b, c)}")
        show_formula(formula_display.discriminant())
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

        show_formula(formula_display.quadratic())
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

        show_formula(formula_display.slope())
        print("")

    elif choice == "4":
        x1 = float(input("x1 value: "))
        y1 = float(input("y1 value: "))
        x2 = float(input("x2 value: "))
        y2 = float(input("y2 value: "))
        print("")

        print(f"Midpoint = {algebra.midpoint(x1, y1, x2, y2)}")
        show_formula(formula_display.midpoint())
        print("")

    elif choice == "5":
        x1 = float(input("x1 value: "))
        y1 = float(input("y1 value: "))
        x2 = float(input("x2 value: "))
        y2 = float(input("y2 value: "))
        print("")

        print(f"Distance = {algebra.distance(x1, y1, x2, y2)}")
        show_formula(formula_display.distance())
        print("")

def run_calculus():
    calculus_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        expr = input("f(x) = ")
        print("")
        print(f"f'(x) = {calculus.derivative(expr)}")
        show_formula(formula_display.derivative())
        print("")

    elif choice == "2":
        expr = input("f(x) = ")
        print("")
        print(f"f''(x) = {calculus.second_derivative(expr)}")
        show_formula(formula_display.derivative())
        print("")

    
    elif choice == "3":
        expr = input("f(x) = ")
        print("")
        print(f"∫f(x) dx = {calculus.indefinite_integral(expr)} + C")
        show_formula(formula_display.integral())
        print("")
    
    elif choice == "4":
        expr = input("f(x) = ")
        a = float(input("Lower bound: "))
        b = float(input("Upper bound: "))
        print("")
        print(f"Definite Integral = {calculus.definite_integral(expr, a, b)}")
        show_formula(formula_display.definite_integral())
        print("")

    elif choice == "5":
        expr = input("f(x) = ")
        value = input("x approaches: ")
        print("")
        print(f"Limit = {calculus.limit(expr, value)}")
        show_formula(formula_display.limit())
        print("")

def run_constants():
    print("=== CONSTANTS ===")
    constant_topic_lib()
    choice = input("Pick a category: ")
    print("")

    if choice == "1":
        constants_mathematical_lib()
    elif choice == "2":
        constants_physical_lib()
    elif choice == "3":
        constants_planck_lib()
    elif choice == "4":
        constants_astronomical_lib()


def run_geometry():
    geometry_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        r = float(input("Radius: "))
        print("")
        print(f"Area = {geometry.circle_area(r)}")
        show_formula(formula_display.circle_area())
        print("")

    elif choice == "2":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("")
        print(f"Area = {geometry.rectangle_area(l, w)}")
        show_formula(formula_display.rectangle_area())
        print("")


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
        conversions_lib()
    elif choice == "5":
        run_geometry()
    elif choice == "6":
        physics_lib()
    elif choice == "7":
        statistics_lib()
    elif choice == "0":
        exit()
    else:
        print("Invalid choice.")


main()