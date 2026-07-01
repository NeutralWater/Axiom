def binary_to_decimal(binary):
    return int(str(binary), 2)


def decimal_to_binary(decimal):
    return bin(int(decimal))[2:]


def binary_to_hex(binary):
    return hex(int(str(binary), 2))[2:].upper()


def hex_to_binary(hex_num):
    return bin(int(str(hex_num), 16))[2:]


def decimal_to_hex(decimal):
    return hex(int(decimal))[2:].upper()


def hex_to_decimal(hex_num):
    return int(str(hex_num), 16)


def decimal_to_octal(decimal):
    return oct(int(decimal))[2:]


def octal_to_decimal(octal):
    return int(str(octal), 8)


def bitwise_and(a, b):
    return int(a) & int(b)


def bitwise_or(a, b):
    return int(a) | int(b)


def bitwise_xor(a, b):
    return int(a) ^ int(b)


def bitwise_not(a):
    return ~int(a)


def left_shift(a, n):
    return int(a) << int(n)


def right_shift(a, n):
    return int(a) >> int(n)


def char_to_ascii(char):
    return ord(char)


def ascii_to_char(code):
    return chr(int(code))