from formulas import calculus
from topic_lib import calculus_lib
import math
import formula_display.core as core
import formula_display.display_calculus as fd

def show_formula(formula):
    core.display_formula(formula)

def run_calculus():
    calculus_lib()    
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        expr = input("f(x) = ")
        print("")
        print(f"f'(x) = {calculus.derivative(expr)}")
        show_formula(fd.derivative())
        print("")

    elif choice == "2":
        expr = input("f(x) = ")
        print("")
        print(f"f''(x) = {calculus.second_derivative(expr)}")
        show_formula(fd.derivative())
        print("")

    
    elif choice == "3":
        expr = input("f(x) = ")
        print("")
        print(f"∫f(x) dx = {calculus.indefinite_integral(expr)} + C")
        show_formula(fd.indefinite_integral())
        print("")
    
    elif choice == "4":
        expr = input("f(x) = ")
        a = float(input("Lower bound: "))
        b = float(input("Upper bound: "))
        print("")
        print(f"Definite Integral = {calculus.definite_integral(expr, a, b)}")
        show_formula(fd.definite_integral())
        print("")

    elif choice == "5":
        expr = input("f(x) = ")
        value = input("x approaches: ")
        print("")
        print(f"Limit = {calculus.limit(expr, value)}")
        show_formula(fd.limit())
        print("")
    
    elif choice == "6":
        expr = input("f(x) = ")
        print("")
        print(f"Critical Points = {calculus.critical_points(expr)}")
        show_formula(fd.critical_points())
        print("")
    
    elif choice == "7":
        expr = input("f(x) = ")
        a = float(input("Point of tangency: "))
        print("")
        print(f"Tangent Line = {calculus.tangent_line(expr, a)}")
        show_formula(fd.tangent_line())
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
            show_formula(fd.normal_line())
        print("")

    elif choice == "9":
        expr = input("f(x) = ")
        print("")
        print(f"Power Rule: f'(x) = {calculus.power_rule(expr)}")
        show_formula(fd.power_rule())
        print("")

    elif choice == "9":
        expr = input("Function in x: ")
        print("")
        inc, dec = calculus.increasing_decreasing(expr)
        print(f"Increasing on: {inc}")
        print(f"Decreasing on: {dec}")
        show_formula(fd.increasing_decreasing())
        print("")

    elif choice == "10":
        expr = input("Function in x: ")
        print("")
        up, down = calculus.concavity(expr)
        print(f"Concave Up: {up}")
        print(f"Concave Down: {down}")
        show_formula(fd.concavity())
        print("")

    elif choice == "11":
        expr = input("Function in x: ")
        print("")
        print(f"Inflection Points = {calculus.inflection_points(expr)}")
        show_formula(fd.inflection_points())
        print("")

    elif choice == "12":
        expr = input("Function in x: ")
        a = float(input("Lower Bound: "))
        b = float(input("Upper Bound: "))
        print("")
        print(f"Average Value = {calculus.average_value(expr, a, b)}")
        show_formula(fd.average_value())
        print("")

    elif choice == "13":
        expr1 = input("Upper Function: ")
        expr2 = input("Lower Function: ")
        a = float(input("Lower Bound: "))
        b = float(input("Upper Bound: "))
        print("")
        print(f"Area Between Curves = {calculus.area_between_curves(expr1, expr2, a, b)}")
        show_formula(fd.area_between_curves())
        print("")

    elif choice == "14":
        expr = input("Function in x: ")
        a = float(input("Lower Bound: "))
        b = float(input("Upper Bound: "))
        print("")
        print(f"Arc Length = {calculus.arc_length(expr, a, b)}")
        show_formula(fd.arc_length())
        print("")

    elif choice == "15":
        expr = input("Function in x: ")
        a = float(input("Lower Bound: "))
        b = float(input("Upper Bound: "))
        print("")
        print(f"Disk Volume = {calculus.disk_volume(expr, a, b)}")
        show_formula(fd.disk_volume())
        print("")

    elif choice == "16":
        outer = input("Outer Function: ")
        inner = input("Inner Function: ")
        a = float(input("Lower Bound: "))
        b = float(input("Upper Bound: "))
        print("")
        print(f"Washer Volume = {calculus.washer_volume(outer, inner, a, b)}")
        show_formula(fd.washer_volume())
        print("")

    elif choice == "17":
        expr = input("Function in x: ")
        guess = float(input("Initial Guess: "))
        iterations = int(input("Iterations: "))
        print("")
        print(f"Approximate Root = {calculus.newtons_method(expr, guess, iterations)}")
        show_formula(fd.newtons_method())
        print("")
    
    elif choice == "18":
        expr = input("Function in x: ")
        print("")
        print(f"Power Rule: f'(x) = {calculus.power_rule(expr)}")
        show_formula(fd.power_rule())
        print("")

    elif choice == "0":
        exit()    