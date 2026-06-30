from formula_display import *

def fahrenheit_to_celsius():
    return make_formula(
        "C = (F - 32) * 5/9",
        {
            "C": "temperature in Celsius",
            "F": "temperature in Fahrenheit"
        },
        units="°C",
        topic="Fahrenheit to Celsius Conversion"
    )

def celsius_to_fahrenheit():
    return make_formula(
        "F = (C * 9/5) + 32",
        {
            "F": "temperature in Fahrenheit",
            "C": "temperature in Celsius"
        },
        units="°F",
        topic="Celsius to Fahrenheit Conversion"
    )