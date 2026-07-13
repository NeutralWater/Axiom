from topic_lib import *
from runners import *

def main():
    menu()
    choice = input("Select Module > ")
    print()

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
    elif choice == "8":
        run_linear_algebra()
    elif choice == "9":
        run_chemistry()
    elif choice == "10":
        run_astronomy()
    elif choice == "11":
        run_computer_science()
    elif choice == "12":
        run_electrical_engineering()
    elif choice == "13":
        run_digital_electronics()
    elif choice == "14":
        run_aerospace_engineering()
    elif choice == "15":
        run_mechanical_engineering()
    elif choice == "0":
        return
    elif choice == "16":
        run_graphing()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()