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
    
    elif choice == "6":
        expr = input("f(x) = ")
        print("")
        print(f"Critical Points = {calculus.critical_points(expr)}")
        show_formula(formula_display.critical_points())
        print("")
    
    elif choice == "7":
        expr = input("f(x) = ")
        a = float(input("Point of tangency: "))
        print("")
        print(f"Tangent Line = {calculus.tangent_line(expr, a)}")
        show_formula(formula_display.tangent_line())
        print("")
    
    elif choice == "8":
        expr = input("f(x) = ")
        a = float(input("Point of tangency: "))
        print("")
        normal_line = calculus.normal_line(expr, a)
        if normal_line is None:
            print("Normal line is undefined (slope is zero).")
        else:
            print(f"Normal Line = {normal_line}")
            show_formula(formula_display.normal_line())
        print("")

    elif choice == "9":
        expr = input("f(x) = ")
        print("")
        print(f"Power Rule: f'(x) = {calculus.power_rule(expr)}")
        show_formula(formula_display.power_rule())
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

def run_conversions():
    conversions_lib()
    choice = input("Pick a conversion: ")
    print("")

    if choice == "1":
        f = float(input("Fahrenheit: "))
        print("")
        print(f"Celsius = {conversions.fahrenheit_to_celsius(f)} °C")
        show_formula(formula_display.fahrenheit_to_celsius())
        print("")
    
    elif choice == "2":
        c = float(input("Celsius: "))
        print("")
        print(f"Fahrenheit = {conversions.celsius_to_fahrenheit(c)} °F")
        show_formula(formula_display.celsius_to_fahrenheit())
        print("")
    
    elif choice == "0":
        exit()

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

    elif choice == "3":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("")
        print(f"Area = {geometry.triangle_area(b, h)}")
        show_formula(formula_display.triangle_area())
        print("")
    
    elif choice == "4":
        r = float(input("Radius: "))
        print("")
        print(f"Circumference = {geometry.circle_circumference(r)}")
        show_formula(formula_display.circle_circumference())
        print("")
    
    elif choice == "5":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("")
        print(f"Perimeter = {geometry.rectangle_perimeter(l, w)}")
        show_formula(formula_display.rectangle_perimeter())
        print("")
    
    elif choice == "6":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        print("")
        print(f"Hypotenuse = {geometry.pythagorean(a, b)}")
        show_formula(formula_display.pythagorean())
        print("")
    
def run_physics():
    physics_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("")
        print(f"Kinetic Energy = {physics.kinetic_energy(m, v)} J")
        show_formula(formula_display.kinetic_energy())
        print("")
    
    elif choice == "2":
        m = float(input("Mass (kg): "))
        a = float(input("Acceleration (m/s²): "))
        print("")
        print(f"Force = {physics.force(m, a)} N")
        show_formula(formula_display.force())
        print("")
    
    elif choice == "3":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("")
        print(f"Momentum = {physics.momentum(m, v)} kg·m/s")
        show_formula(formula_display.momentum())
        print("")
    
    elif choice == "4":
        f = float(input("Force (N): "))
        d = float(input("Distance (m): "))
        print("")
        print(f"Work = {physics.work(f, d)} J")
        show_formula(formula_display.work())

def run_statistics():
    statistics_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        data = input("Enter data (comma-separated): ")
        data_list = [float(x.strip()) for x in data.split(",")]
        print("")
        print(f"Mean = {statistics.mean(data_list)}")
        show_formula(formula_display.mean())
        print("")
    
    elif choice == "2":
        data = input("Enter data (comma-separated): ")
        data_list = [float(x.strip()) for x in data.split(",")]
        print("")
        print(f"Median = {statistics.median(data_list)}")
        show_formula(formula_display.median())
        print("")
    
    elif choice == "3":
        data = input("Enter data (comma-separated): ")
        data_list = [float(x.strip()) for x in data.split(",")]
        print("")
        print(f"Mode = {statistics.mode(data_list)}")
        show_formula(formula_display.mode())
        print("")
    
    elif choice == "4":
        data = input("Enter data (comma-separated): ")
        data_list = [float(x.strip()) for x in data.split(",")]
        print("")
        print(f"Standard Deviation = {statistics.standard_deviation(data_list)}")
        show_formula(formula_display.standard_deviation())

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