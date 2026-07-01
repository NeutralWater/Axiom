from formulas import conversions
from topic_lib import conversions_lib
import formula_display.core as core
import formula_display.display_conversions as fd


def show_formula(formula):
    core.display_formula(formula)


def run_conversions():
    conversions_lib()
    choice = input("Select a conversion: ")
    print("")

    if choice == "1":
        f = float(input("Fahrenheit: "))
        print(f"Celsius = {conversions.fahrenheit_to_celsius(f)}")
        show_formula(fd.fahrenheit_to_celsius())

    elif choice == "2":
        c = float(input("Celsius: "))
        print(f"Fahrenheit = {conversions.celsius_to_fahrenheit(c)}")
        show_formula(fd.celsius_to_fahrenheit())

    elif choice == "3":
        c = float(input("Celsius: "))
        print(f"Kelvin = {conversions.celsius_to_kelvin(c)}")
        show_formula(fd.celsius_to_kelvin())

    elif choice == "4":
        k = float(input("Kelvin: "))
        print(f"Celsius = {conversions.kelvin_to_celsius(k)}")
        show_formula(fd.kelvin_to_celsius())

    elif choice == "5":
        f = float(input("Fahrenheit: "))
        print(f"Kelvin = {conversions.fahrenheit_to_kelvin(f)}")
        show_formula(fd.fahrenheit_to_kelvin())

    elif choice == "6":
        k = float(input("Kelvin: "))
        print(f"Fahrenheit = {conversions.kelvin_to_fahrenheit(k)}")
        show_formula(fd.kelvin_to_fahrenheit())

    elif choice == "7":
        m = float(input("Meters: "))
        print(f"Kilometers = {conversions.meters_to_kilometers(m)}")
        show_formula(fd.meters_to_kilometers())

    elif choice == "8":
        km = float(input("Kilometers: "))
        print(f"Meters = {conversions.kilometers_to_meters(km)}")
        show_formula(fd.kilometers_to_meters())

    elif choice == "9":
        m = float(input("Meters: "))
        print(f"Centimeters = {conversions.meters_to_centimeters(m)}")
        show_formula(fd.meters_to_centimeters())

    elif choice == "10":
        cm = float(input("Centimeters: "))
        print(f"Meters = {conversions.centimeters_to_meters(cm)}")
        show_formula(fd.centimeters_to_meters())

    elif choice == "11":
        inches = float(input("Inches: "))
        print(f"Centimeters = {conversions.inches_to_centimeters(inches)}")
        show_formula(fd.inches_to_centimeters())

    elif choice == "12":
        cm = float(input("Centimeters: "))
        print(f"Inches = {conversions.centimeters_to_inches(cm)}")
        show_formula(fd.centimeters_to_inches())

    elif choice == "13":
        ft = float(input("Feet: "))
        print(f"Meters = {conversions.feet_to_meters(ft)}")
        show_formula(fd.feet_to_meters())

    elif choice == "14":
        m = float(input("Meters: "))
        print(f"Feet = {conversions.meters_to_feet(m)}")
        show_formula(fd.meters_to_feet())

    elif choice == "15":
        mi = float(input("Miles: "))
        print(f"Kilometers = {conversions.miles_to_kilometers(mi)}")
        show_formula(fd.miles_to_kilometers())

    elif choice == "16":
        km = float(input("Kilometers: "))
        print(f"Miles = {conversions.kilometers_to_miles(km)}")
        show_formula(fd.kilometers_to_miles())

    elif choice == "0":
        exit()

    else:
        print("Invalid option.")