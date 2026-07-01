from formulas import computer_science
from topic_lib import computer_science_lib
import formula_display.core as core
import formula_display.display_computer_science as fd


def show_formula(formula):
    core.display_formula(formula)


def run_computer_science():
    computer_science_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        binary = input("Binary: ")
        print(f"Decimal = {computer_science.binary_to_decimal(binary)}")
        show_formula(fd.binary_to_decimal())

    elif choice == "2":
        decimal = int(input("Decimal: "))
        print(f"Binary = {computer_science.decimal_to_binary(decimal)}")
        show_formula(fd.decimal_to_binary())

    elif choice == "3":
        binary = input("Binary: ")
        print(f"Hex = {computer_science.binary_to_hex(binary)}")
        show_formula(fd.binary_to_hex())

    elif choice == "4":
        hex_num = input("Hex: ")
        print(f"Binary = {computer_science.hex_to_binary(hex_num)}")
        show_formula(fd.hex_to_binary())

    elif choice == "5":
        decimal = int(input("Decimal: "))
        print(f"Hex = {computer_science.decimal_to_hex(decimal)}")
        show_formula(fd.decimal_to_hex())

    elif choice == "6":
        hex_num = input("Hex: ")
        print(f"Decimal = {computer_science.hex_to_decimal(hex_num)}")
        show_formula(fd.hex_to_decimal())

    elif choice == "7":
        decimal = int(input("Decimal: "))
        print(f"Octal = {computer_science.decimal_to_octal(decimal)}")
        show_formula(fd.decimal_to_octal())

    elif choice == "8":
        octal = input("Octal: ")
        print(f"Decimal = {computer_science.octal_to_decimal(octal)}")
        show_formula(fd.octal_to_decimal())

    elif choice == "9":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"Result = {computer_science.bitwise_and(a, b)}")
        show_formula(fd.bitwise_and())

    elif choice == "10":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"Result = {computer_science.bitwise_or(a, b)}")
        show_formula(fd.bitwise_or())

    elif choice == "11":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"Result = {computer_science.bitwise_xor(a, b)}")
        show_formula(fd.bitwise_xor())

    elif choice == "12":
        a = int(input("Number: "))
        print(f"Result = {computer_science.bitwise_not(a)}")
        show_formula(fd.bitwise_not())

    elif choice == "13":
        a = int(input("Number: "))
        n = int(input("Shift amount: "))
        print(f"Result = {computer_science.left_shift(a, n)}")
        show_formula(fd.left_shift())

    elif choice == "14":
        a = int(input("Number: "))
        n = int(input("Shift amount: "))
        print(f"Result = {computer_science.right_shift(a, n)}")
        show_formula(fd.right_shift())

    elif choice == "15":
        char = input("Character: ")
        print(f"ASCII Code = {computer_science.char_to_ascii(char)}")
        show_formula(fd.char_to_ascii())

    elif choice == "16":
        code = int(input("ASCII code: "))
        print(f"Character = {computer_science.ascii_to_char(code)}")
        show_formula(fd.ascii_to_char())

    else:
        print("Invalid option.")