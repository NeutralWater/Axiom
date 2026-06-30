from topic_lib import constant_topic_lib, constants_mathematical_lib, constants_physical_lib, constants_planck_lib, constants_astronomical_lib
import formula_display

def show_formula(formula):
    formula_display.display_formula(formula)
def show_formula(formula):
    formula_display.display_formula(formula)

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