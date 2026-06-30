from formulas import conversions
from topic_lib import conversions_lib
import math
import formula_display.formula_display_core as formula_display_core

def show_formula(formula):
    formula_display_core.display_formula(formula)

def run_conversions():
    conversions_lib()
    choice = input("Pick a conversion: ")
    print("")

    if choice == "1":
        f = float(input("Fahrenheit: "))
        print("")
        print(f"Celsius = {conversions.fahrenheit_to_celsius(f)} °C")
        show_formula(formula_display_core.fahrenheit_to_celsius())
        print("")
    
    elif choice == "2":
        c = float(input("Celsius: "))
        print("")
        print(f"Fahrenheit = {conversions.celsius_to_fahrenheit(c)} °F")
        show_formula(formula_display_core.celsius_to_fahrenheit())
        print("")
    
    elif choice == "0":
        exit()
