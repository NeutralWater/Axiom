from formula_display.core import *


def binary_to_decimal():
    return make_formula(
        "Decimal = Σ(bitᵢ × 2ⁱ)",
        {
            "bitᵢ": "binary digit",
            "2ⁱ": "place value",
            "Σ": "sum of all place values"
        },
        topic="Binary to Decimal"
    )


def decimal_to_binary():
    return make_formula(
        "Decimal → Binary",
        {
            "Decimal": "base 10 number",
            "Binary": "base 2 number"
        },
        topic="Decimal to Binary",
        notes="Repeatedly divide by 2 and read the remainders from bottom to top."
    )


def binary_to_hex():
    return make_formula(
        "Binary → Decimal → Hexadecimal",
        {
            "Binary": "base 2 number",
            "Decimal": "base 10 number",
            "Hexadecimal": "base 16 number"
        },
        topic="Binary to Hexadecimal"
    )


def hex_to_binary():
    return make_formula(
        "Hexadecimal → Decimal → Binary",
        {
            "Hexadecimal": "base 16 number",
            "Decimal": "base 10 number",
            "Binary": "base 2 number"
        },
        topic="Hexadecimal to Binary"
    )


def decimal_to_hex():
    return make_formula(
        "Decimal → Hexadecimal",
        {
            "Decimal": "base 10 number",
            "Hexadecimal": "base 16 number"
        },
        topic="Decimal to Hexadecimal",
        notes="Repeatedly divide by 16."
    )


def hex_to_decimal():
    return make_formula(
        "Decimal = Σ(digitᵢ × 16ⁱ)",
        {
            "digitᵢ": "hexadecimal digit",
            "16ⁱ": "place value",
            "Σ": "sum of all place values"
        },
        topic="Hexadecimal to Decimal"
    )


def decimal_to_octal():
    return make_formula(
        "Decimal → Octal",
        {
            "Decimal": "base 10 number",
            "Octal": "base 8 number"
        },
        topic="Decimal to Octal",
        notes="Repeatedly divide by 8."
    )


def octal_to_decimal():
    return make_formula(
        "Decimal = Σ(digitᵢ × 8ⁱ)",
        {
            "digitᵢ": "octal digit",
            "8ⁱ": "place value",
            "Σ": "sum of all place values"
        },
        topic="Octal to Decimal"
    )


def bitwise_and():
    return make_formula(
        "a AND b",
        {
            "a": "first integer",
            "b": "second integer",
            "AND": "returns 1 only if both bits are 1"
        },
        topic="Bitwise AND"
    )


def bitwise_or():
    return make_formula(
        "a OR b",
        {
            "a": "first integer",
            "b": "second integer",
            "OR": "returns 1 if either bit is 1"
        },
        topic="Bitwise OR"
    )


def bitwise_xor():
    return make_formula(
        "a XOR b",
        {
            "a": "first integer",
            "b": "second integer",
            "XOR": "returns 1 only when bits differ"
        },
        topic="Bitwise XOR"
    )


def bitwise_not():
    return make_formula(
        "~a = -(a + 1)",
        {
            "~": "bitwise NOT operator",
            "a": "integer"
        },
        topic="Bitwise NOT",
        notes="Python represents integers using signed arithmetic."
    )


def left_shift():
    return make_formula(
        "a << n = a × 2ⁿ",
        {
            "a": "integer",
            "n": "number of bit positions shifted"
        },
        topic="Left Shift"
    )


def right_shift():
    return make_formula(
        "a >> n = floor(a / 2ⁿ)",
        {
            "a": "integer",
            "n": "number of bit positions shifted"
        },
        topic="Right Shift"
    )


def char_to_ascii():
    return make_formula(
        "Code = ord(Character)",
        {
            "Code": "ASCII/Unicode value",
            "Character": "input character",
            "ord()": "Python function returning a character's code"
        },
        topic="Character to ASCII"
    )


def ascii_to_char():
    return make_formula(
        "Character = chr(Code)",
        {
            "Character": "output character",
            "Code": "ASCII/Unicode value",
            "chr()": "Python function converting a code to a character"
        },
        topic="ASCII to Character"
    )