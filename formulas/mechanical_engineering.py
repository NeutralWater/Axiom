import math

def torque(force, radius):
    return force * radius

def angular_velocity(theta, time):
    return theta / time

def angular_acceleration(final_omega, initial_omega, time):
    return (final_omega - initial_omega) / time

def rotational_kinetic_energy(moment_of_inertia, angular_velocity):
    return 0.5 * moment_of_inertia * angular_velocity ** 2

def moment_of_inertia(mass, radius):
    return mass * radius ** 2

def rotational_power(torque, angular_velocity):
    return torque * angular_velocity

def mechanical_advantage(output_force, input_force):
    return output_force / input_force

def gear_ratio(driven_teeth, driver_teeth):
    return driven_teeth / driver_teeth

def stress(force, area):
    return force / area

def strain(change_length, original_length):
    return change_length / original_length

def youngs_modulus(stress, strain):
    return stress / strain

def shear_stress(force, area):
    return force / area

def shear_strain(displacement, height):
    return displacement / height

def spring_force(spring_constant, displacement):
    return spring_constant * displacement

def spring_potential_energy(spring_constant, displacement):
    return 0.5 * spring_constant * displacement ** 2

def hookes_law(spring_constant, displacement):
    return spring_constant * displacement

def thermal_expansion(alpha, original_length, delta_temperature):
    return alpha * original_length * delta_temperature

def linear_expansion(alpha, original_length, delta_temperature):
    return original_length * (1 + alpha * delta_temperature)

def safety_factor(material_strength, applied_stress):
    return material_strength / applied_stress

def beam_bending_stress(moment, distance, inertia):
    return (moment * distance) / inertia