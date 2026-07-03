import math
from formulas import constant_values as c 


def kinetic_energy(m, v):
    return 0.5 * m * v ** 2


def force(m, a):
    return m * a


def momentum(m, v):
    return m * v


def work(f, d):
    return f * d


def speed(distance, time):
    return distance / time


def acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time


def displacement_average_velocity(initial_velocity, final_velocity, time):
    return ((initial_velocity + final_velocity) / 2) * time


def displacement_acceleration(initial_velocity, time, acceleration):
    return initial_velocity * time + 0.5 * acceleration * time ** 2


def final_velocity(initial_velocity, acceleration, time):
    return initial_velocity + acceleration * time


def final_velocity_squared(initial_velocity, acceleration, displacement):
    return math.sqrt(initial_velocity ** 2 + 2 * acceleration * displacement)


def free_fall_time(height):
    return math.sqrt((2 * height) / c.GRAVITY)


def weight(mass):
    return mass * c.GRAVITY


def friction(coefficient, normal_force):
    return coefficient * normal_force


def normal_force(mass):
    return mass * c.GRAVITY


def gravitational_force(mass1, mass2, distance):
    return c.GRAVITATIONAL_CONSTANT * mass1 * mass2 / distance ** 2


def centripetal_force(mass, velocity, radius):
    return mass * velocity ** 2 / radius


def centripetal_acceleration(velocity, radius):
    return velocity ** 2 / radius


def potential_energy(mass, height):
    return mass * c.GRAVITY * height


def mechanical_energy(kinetic_energy, potential_energy):
    return kinetic_energy + potential_energy


def power(work, time):
    return work / time


def efficiency(output_work, input_work):
    return (output_work / input_work) * 100


def impulse(force, time):
    return force * time


def change_in_momentum(final_momentum, initial_momentum):
    return final_momentum - initial_momentum


def wave_speed(frequency, wavelength):
    return frequency * wavelength


def frequency(wave_speed, wavelength):
    return wave_speed / wavelength


def wavelength(wave_speed, frequency):
    return wave_speed / frequency


def period(frequency):
    return 1 / frequency


def frequency_from_period(period):
    return 1 / period


def ohms_law(voltage, resistance):
    return voltage / resistance


def voltage(current, resistance):
    return current * resistance


def resistance(voltage, current):
    return voltage / current


def electrical_power_vi(voltage, current):
    return voltage * current


def electrical_power_i2r(current, resistance):
    return current ** 2 * resistance


def electrical_power_v2r(voltage, resistance):
    return voltage ** 2 / resistance


def charge(current, time):
    return current * time


def current(charge, time):
    return charge / time


def resistance_series(*resistors):
    return sum(resistors)


def resistance_parallel(*resistors):
    return 1 / sum(1 / r for r in resistors)


def coulombs_law(charge1, charge2, distance):
    return c.COULOMBS_CONSTANT * charge1 * charge2 / distance ** 2


def electric_field(force, charge):
    return force / charge