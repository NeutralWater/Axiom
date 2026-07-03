import math
from formulas.constant_values import *


def dynamic_pressure(density, velocity):
    return 0.5 * density * velocity ** 2


def lift(density, velocity, wing_area, lift_coefficient):
    return 0.5 * density * velocity ** 2 * wing_area * lift_coefficient


def drag(density, velocity, reference_area, drag_coefficient):
    return 0.5 * density * velocity ** 2 * reference_area * drag_coefficient


def lift_to_drag_ratio(lift, drag):
    return lift / drag


def wing_loading(weight, wing_area):
    return weight / wing_area


def thrust_to_weight_ratio(thrust, weight):
    return thrust / weight


def thrust(mass_flow_rate, exhaust_velocity):
    return mass_flow_rate * exhaust_velocity


def mass_flow_rate(thrust, exhaust_velocity):
    return thrust / exhaust_velocity


def specific_impulse(thrust, mass_flow_rate):
    return thrust / (mass_flow_rate * GRAVITY)


def effective_exhaust_velocity(specific_impulse):
    return specific_impulse * GRAVITY


def rocket_equation(initial_mass, final_mass, exhaust_velocity):
    return exhaust_velocity * math.log(initial_mass / final_mass)


def escape_velocity(mass, radius):
    return math.sqrt((2 * GRAVITATIONAL_CONSTANT * mass) / radius)


def earth_escape_velocity():
    return math.sqrt((2 * EARTH_MU) / EARTH_RADIUS)


def orbital_velocity(gravitational_parameter, radius):
    return math.sqrt(gravitational_parameter / radius)


def earth_orbital_velocity(radius):
    return math.sqrt(EARTH_MU / radius)


def orbital_period(gravitational_parameter, radius):
    return 2 * PI * math.sqrt(radius ** 3 / gravitational_parameter)


def earth_orbital_period(radius):
    return 2 * PI * math.sqrt(radius ** 3 / EARTH_MU)


def orbital_energy(gravitational_parameter, semi_major_axis):
    return -gravitational_parameter / (2 * semi_major_axis)


def mach_number(velocity, speed_of_sound):
    return velocity / speed_of_sound


def earth_mach_number(velocity):
    return velocity / SPEED_OF_SOUND
