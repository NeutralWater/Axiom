from formulas import statistics
from topic_lib import statistics_lib
import math
import formula_display

def show_formula(formula):
    formula_display.display_formula(formula)

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
        print(f"Range = {statistics.range_value(data_list)}")
        show_formula(formula_display.range())
        print("")

    elif choice == "3":
        p = float(input("Principal ($): "))
        r = float(input("Annual Interest Rate (%): ")) / 100
        t = float(input("Time (years): "))
        print("")
        print(f"Simple Interest = ${statistics.simple_interest(p, r, t):.2f}")
        show_formula(formula_display.simple_interest())
        print("")

    elif choice == "4":
        p = float(input("Principal ($): "))
        r = float(input("Annual Interest Rate (%): ")) / 100
        n = int(input("Compounds per year: "))
        t = float(input("Time (years): "))
        print("")
        print(f"Final Amount = ${statistics.compound_interest(p, r, n, t):.2f}")
        show_formula(formula_display.compound_interest())
        print("")

    elif choice == "0":
        exit()