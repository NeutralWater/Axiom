from formulas import statistics
from topic_lib import statistics_lib
import math
import formula_display.formula_display_core as formula_display_core

def show_formula(formula):
    formula_display_core.display_formula(formula)

def run_statistics():
    statistics_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        data = input("Enter data (comma-separated): ")
        data_list = [float(x.strip()) for x in data.split(",")]
        print("")
        print(f"Mean = {statistics.mean(data_list)}")
        show_formula(formula_display_core.mean())
        print("")

    elif choice == "2":
        data = input("Enter data (comma-separated): ")
        data_list = [float(x.strip()) for x in data.split(",")]
        print("")
        print(f"Range = {statistics.range_value(data_list)}")
        show_formula(formula_display_core.range())
        print("")

    elif choice == "3":
        p = float(input("Principal ($): "))
        r = float(input("Annual Interest Rate (%): ")) / 100
        t = float(input("Time (years): "))
        print("")
        print(f"Simple Interest = ${statistics.simple_interest(p, r, t):.2f}")
        show_formula(formula_display_core.simple_interest())
        print("")

    elif choice == "4":
        p = float(input("Principal ($): "))
        r = float(input("Annual Interest Rate (%): ")) / 100
        n = int(input("Compounds per year: "))
        t = float(input("Time (years): "))
        print("")
        print(f"Final Amount = ${statistics.compound_interest(p, r, n, t):.2f}")
        show_formula(formula_display_core.compound_interest())
        print("")

    elif choice == "0":
        exit()