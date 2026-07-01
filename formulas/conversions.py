def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def meters_to_kilometers(m):
    return m / 1000


def kilometers_to_meters(km):
    return km * 1000


def meters_to_centimeters(m):
    return m * 100


def centimeters_to_meters(cm):
    return cm / 100


def inches_to_centimeters(inches):
    return inches * 2.54


def centimeters_to_inches(cm):
    return cm / 2.54


def feet_to_meters(ft):
    return ft * 0.3048


def meters_to_feet(m):
    return m / 0.3048


def miles_to_kilometers(mi):
    return mi * 1.609344


def kilometers_to_miles(km):
    return km / 1.609344