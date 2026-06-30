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

    elif choice == "0":
        exit()