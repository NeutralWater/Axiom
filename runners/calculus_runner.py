from formulas import calculus
from topic_lib import calculus_lib
import math
import formula_display.core as core

def show_formula(formula):
    core.display_formula(formula)

def run_calculus():
    calculus_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        expr = input("f(x) = ")
        print("")
        print(f"f'(x) = {calculus.derivative(expr)}")
        show_formula(core.derivative())
        print("")

    elif choice == "2":
        expr = input("f(x) = ")
        print("")
        print(f"f''(x) = {calculus.second_derivative(expr)}")
        show_formula(core.derivative())
        print("")

    
    elif choice == "3":
        expr = input("f(x) = ")
        print("")
        print(f"∫f(x) dx = {calculus.indefinite_integral(expr)} + C")
        show_formula(core.indefinite_integral())
        print("")
    
    elif choice == "4":
        expr = input("f(x) = ")
        a = float(input("Lower bound: "))
        b = float(input("Upper bound: "))
        print("")
        print(f"Definite Integral = {calculus.definite_integral(expr, a, b)}")
        show_formula(core.definite_integral())
        print("")

    elif choice == "5":
        expr = input("f(x) = ")
        value = input("x approaches: ")
        print("")
        print(f"Limit = {calculus.limit(expr, value)}")
        show_formula(core.limit())
        print("")
    
    elif choice == "6":
        expr = input("f(x) = ")
        print("")
        print(f"Critical Points = {calculus.critical_points(expr)}")
        show_formula(core.critical_points())
        print("")
    
    elif choice == "7":
        expr = input("f(x) = ")
        a = float(input("Point of tangency: "))
        print("")
        print(f"Tangent Line = {calculus.tangent_line(expr, a)}")
        show_formula(core.tangent_line())
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
            show_formula(core.normal_line())
        print("")

    elif choice == "9":
        expr = input("f(x) = ")
        print("")
        print(f"Power Rule: f'(x) = {calculus.power_rule(expr)}")
        show_formula(core.power_rule())
        print("")

    elif choice == "0":
        exit()    