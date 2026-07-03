from formulas import mechanical_engineering
from topic_lib import mechanical_engineering_lib
import formula_display.core as core
import formula_display.display_mechanical_engineering as fd


def show_formula(formula):
    core.display_formula(formula)


def run_mechanical_engineering():
    mechanical_engineering_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        force = float(input("Force (N): "))
        radius = float(input("Lever Arm (m): "))
        print("")
        print(f"Torque = {mechanical_engineering.torque(force, radius)} N·m")
        show_formula(fd.torque())
        print("")

    elif choice == "2":
        theta = float(input("Angular Displacement (rad): "))
        time = float(input("Time (s): "))
        print("")
        print(f"Angular Velocity = {mechanical_engineering.angular_velocity(theta, time)} rad/s")
        show_formula(fd.angular_velocity())
        print("")

    elif choice == "3":
        final_omega = float(input("Final Angular Velocity (rad/s): "))
        initial_omega = float(input("Initial Angular Velocity (rad/s): "))
        time = float(input("Time (s): "))
        print("")
        print(f"Angular Acceleration = {mechanical_engineering.angular_acceleration(final_omega, initial_omega, time)} rad/s²")
        show_formula(fd.angular_acceleration())
        print("")

    elif choice == "4":
        moment_of_inertia = float(input("Moment of Inertia (kg·m²): "))
        angular_velocity = float(input("Angular Velocity (rad/s): "))
        print("")
        print(f"Rotational Kinetic Energy = {mechanical_engineering.rotational_kinetic_energy(moment_of_inertia, angular_velocity)} J")
        show_formula(fd.rotational_kinetic_energy())
        print("")

    elif choice == "5":
        mass = float(input("Mass (kg): "))
        radius = float(input("Radius (m): "))
        print("")
        print(f"Moment of Inertia = {mechanical_engineering.moment_of_inertia(mass, radius)} kg·m²")
        show_formula(fd.moment_of_inertia())
        print("")

    elif choice == "6":
        torque = float(input("Torque (N·m): "))
        angular_velocity = float(input("Angular Velocity (rad/s): "))
        print("")
        print(f"Rotational Power = {mechanical_engineering.rotational_power(torque, angular_velocity)} W")
        show_formula(fd.rotational_power())
        print("")

    elif choice == "7":
        output_force = float(input("Output Force (N): "))
        input_force = float(input("Input Force (N): "))
        print("")
        print(f"Mechanical Advantage = {mechanical_engineering.mechanical_advantage(output_force, input_force)}")
        show_formula(fd.mechanical_advantage())
        print("")

    elif choice == "8":
        driven_teeth = float(input("Driven Gear Teeth: "))
        driver_teeth = float(input("Driver Gear Teeth: "))
        print("")
        print(f"Gear Ratio = {mechanical_engineering.gear_ratio(driven_teeth, driver_teeth)}")
        show_formula(fd.gear_ratio())
        print("")

    elif choice == "9":
        force = float(input("Force (N): "))
        area = float(input("Area (m²): "))
        print("")
        print(f"Stress = {mechanical_engineering.stress(force, area)} Pa")
        show_formula(fd.stress())
        print("")

    elif choice == "10":
        change_length = float(input("Change in Length (m): "))
        original_length = float(input("Original Length (m): "))
        print("")
        print(f"Strain = {mechanical_engineering.strain(change_length, original_length)}")
        show_formula(fd.strain())
        print("")

    elif choice == "11":
        stress = float(input("Stress (Pa): "))
        strain = float(input("Strain: "))
        print("")
        print(f"Young's Modulus = {mechanical_engineering.youngs_modulus(stress, strain)} Pa")
        show_formula(fd.youngs_modulus())
        print("")

    elif choice == "12":
        force = float(input("Force (N): "))
        area = float(input("Area (m²): "))
        print("")
        print(f"Shear Stress = {mechanical_engineering.shear_stress(force, area)} Pa")
        show_formula(fd.shear_stress())
        print("")

    elif choice == "13":
        displacement = float(input("Lateral Displacement (m): "))
        height = float(input("Height (m): "))
        print("")
        print(f"Shear Strain = {mechanical_engineering.shear_strain(displacement, height)}")
        show_formula(fd.shear_strain())
        print("")

    elif choice == "14":
        spring_constant = float(input("Spring Constant (N/m): "))
        displacement = float(input("Displacement (m): "))
        print("")
        print(f"Spring Force = {mechanical_engineering.spring_force(spring_constant, displacement)} N")
        show_formula(fd.spring_force())
        print("")

    elif choice == "15":
        spring_constant = float(input("Spring Constant (N/m): "))
        displacement = float(input("Displacement (m): "))
        print("")
        print(f"Spring Potential Energy = {mechanical_engineering.spring_potential_energy(spring_constant, displacement)} J")
        show_formula(fd.spring_potential_energy())
        print("")

    elif choice == "16":
        spring_constant = float(input("Spring Constant (N/m): "))
        displacement = float(input("Displacement (m): "))
        print("")
        print(f"Hooke's Law Force = {mechanical_engineering.hookes_law(spring_constant, displacement)} N")
        show_formula(fd.hookes_law())
        print("")

    elif choice == "17":
        alpha = float(input("Coefficient of Linear Expansion (1/°C): "))
        original_length = float(input("Original Length (m): "))
        delta_temperature = float(input("Change in Temperature (°C): "))
        print("")
        print(f"Thermal Expansion = {mechanical_engineering.thermal_expansion(alpha, original_length, delta_temperature)} m")
        show_formula(fd.thermal_expansion())
        print("")

    elif choice == "18":
        alpha = float(input("Coefficient of Linear Expansion (1/°C): "))
        original_length = float(input("Original Length (m): "))
        delta_temperature = float(input("Change in Temperature (°C): "))
        print("")
        print(f"Final Length = {mechanical_engineering.linear_expansion(alpha, original_length, delta_temperature)} m")
        show_formula(fd.linear_expansion())
        print("")

    elif choice == "19":
        material_strength = float(input("Material Strength (Pa): "))
        applied_stress = float(input("Applied Stress (Pa): "))
        print("")
        print(f"Safety Factor = {mechanical_engineering.safety_factor(material_strength, applied_stress)}")
        show_formula(fd.safety_factor())
        print("")

    elif choice == "20":
        moment = float(input("Bending Moment (N·m): "))
        distance = float(input("Distance from Neutral Axis (m): "))
        inertia = float(input("Area Moment of Inertia (m⁴): "))
        print("")
        print(f"Beam Bending Stress = {mechanical_engineering.beam_bending_stress(moment, distance, inertia)} Pa")
        show_formula(fd.beam_bending_stress())
        print("")

    elif choice == "0":
        exit()