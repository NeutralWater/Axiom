from formula_display.core import *


def fahrenheit_to_celsius():
    return make_formula(
        "°C = (°F - 32) × 5/9",
        {
            "°C": "temperature in Celsius",
            "°F": "temperature in Fahrenheit"
        },
        units="°C",
        topic="Fahrenheit to Celsius"
    )


def celsius_to_fahrenheit():
    return make_formula(
        "°F = (°C × 9/5) + 32",
        {
            "°F": "temperature in Fahrenheit",
            "°C": "temperature in Celsius"
        },
        units="°F",
        topic="Celsius to Fahrenheit"
    )


def celsius_to_kelvin():
    return make_formula(
        "K = °C + 273.15",
        {
            "K": "temperature in Kelvin",
            "°C": "temperature in Celsius"
        },
        units="kelvin",
        topic="Celsius to Kelvin"
    )


def kelvin_to_celsius():
    return make_formula(
        "°C = K - 273.15",
        {
            "°C": "temperature in Celsius",
            "K": "temperature in Kelvin"
        },
        units="°C",
        topic="Kelvin to Celsius"
    )


def fahrenheit_to_kelvin():
    return make_formula(
        "K = (°F - 32) × 5/9 + 273.15",
        {
            "K": "temperature in Kelvin",
            "°F": "temperature in Fahrenheit"
        },
        units="kelvin",
        topic="Fahrenheit to Kelvin"
    )


def kelvin_to_fahrenheit():
    return make_formula(
        "°F = (K - 273.15) × 9/5 + 32",
        {
            "°F": "temperature in Fahrenheit",
            "K": "temperature in Kelvin"
        },
        units="°F",
        topic="Kelvin to Fahrenheit"
    )


def meters_to_kilometers():
    return make_formula(
        "km = m / 1000",
        {
            "km": "kilometers",
            "m": "meters"
        },
        units="kilometers",
        topic="Meters to Kilometers"
    )


def kilometers_to_meters():
    return make_formula(
        "m = km × 1000",
        {
            "m": "meters",
            "km": "kilometers"
        },
        units="meters",
        topic="Kilometers to Meters"
    )


def meters_to_centimeters():
    return make_formula(
        "cm = m × 100",
        {
            "cm": "centimeters",
            "m": "meters"
        },
        units="centimeters",
        topic="Meters to Centimeters"
    )


def centimeters_to_meters():
    return make_formula(
        "m = cm / 100",
        {
            "m": "meters",
            "cm": "centimeters"
        },
        units="meters",
        topic="Centimeters to Meters"
    )


def inches_to_centimeters():
    return make_formula(
        "cm = in × 2.54",
        {
            "cm": "centimeters",
            "in": "inches"
        },
        units="centimeters",
        topic="Inches to Centimeters"
    )


def centimeters_to_inches():
    return make_formula(
        "in = cm / 2.54",
        {
            "in": "inches",
            "cm": "centimeters"
        },
        units="inches",
        topic="Centimeters to Inches"
    )


def feet_to_meters():
    return make_formula(
        "m = ft × 0.3048",
        {
            "m": "meters",
            "ft": "feet"
        },
        units="meters",
        topic="Feet to Meters"
    )


def meters_to_feet():
    return make_formula(
        "ft = m / 0.3048",
        {
            "ft": "feet",
            "m": "meters"
        },
        units="feet",
        topic="Meters to Feet"
    )


def miles_to_kilometers():
    return make_formula(
        "km = mi × 1.609344",
        {
            "km": "kilometers",
            "mi": "miles"
        },
        units="kilometers",
        topic="Miles to Kilometers"
    )


def kilometers_to_miles():
    return make_formula(
        "mi = km / 1.609344",
        {
            "mi": "miles",
            "km": "kilometers"
        },
        units="miles",
        topic="Kilometers to Miles"
    )