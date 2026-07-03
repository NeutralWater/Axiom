from formulas import aerospace_engineering as aerospace
from topic_lib import aerospace_lib
import formula_display.core as core
import formula_display.display_aerospace_engineering as fd


def show_formula(formula):
    core.display_formula(formula)


def run_aerospace_engineering():
    aerospace_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        density = float(input("Air Density (kg/m³): "))
        velocity = float(input("Velocity (m/s): "))
        print("")
        print(f"Dynamic Pressure = {aerospace.dynamic_pressure(density, velocity)} Pa")
        show_formula(fd.dynamic_pressure())
        print("")

    elif choice == "2":
        density = float(input("Air Density (kg/m³): "))
        velocity = float(input("Velocity (m/s): "))
        wing_area = float(input("Wing Area (m²): "))
        lift_coefficient = float(input("Lift Coefficient: "))
        print("")
        print(f"Lift = {aerospace.lift(density, velocity, wing_area, lift_coefficient)} N")
        show_formula(fd.lift())
        print("")

    elif choice == "3":
        density = float(input("Air Density (kg/m³): "))
        velocity = float(input("Velocity (m/s): "))
        reference_area = float(input("Reference Area (m²): "))
        drag_coefficient = float(input("Drag Coefficient: "))
        print("")
        print(f"Drag = {aerospace.drag(density, velocity, reference_area, drag_coefficient)} N")
        show_formula(fd.drag())
        print("")

    elif choice == "4":
        lift = float(input("Lift (N): "))
        drag = float(input("Drag (N): "))
        print("")
        print(f"Lift-to-Drag Ratio = {aerospace.lift_to_drag_ratio(lift, drag)}")
        show_formula(fd.lift_to_drag_ratio())
        print("")

    elif choice == "5":
        weight = float(input("Weight (N): "))
        wing_area = float(input("Wing Area (m²): "))
        print("")
        print(f"Wing Loading = {aerospace.wing_loading(weight, wing_area)} N/m²")
        show_formula(fd.wing_loading())
        print("")

    elif choice == "6":
        thrust = float(input("Thrust (N): "))
        weight = float(input("Weight (N): "))
        print("")
        print(f"Thrust-to-Weight Ratio = {aerospace.thrust_to_weight_ratio(thrust, weight)}")
        show_formula(fd.thrust_to_weight_ratio())
        print("")

    elif choice == "7":
        mass_flow_rate = float(input("Mass Flow Rate (kg/s): "))
        exhaust_velocity = float(input("Exhaust Velocity (m/s): "))
        print("")
        print(f"Thrust = {aerospace.thrust(mass_flow_rate, exhaust_velocity)} N")
        show_formula(fd.thrust())
        print("")

    elif choice == "8":
        thrust = float(input("Thrust (N): "))
        exhaust_velocity = float(input("Exhaust Velocity (m/s): "))
        print("")
        print(f"Mass Flow Rate = {aerospace.mass_flow_rate(thrust, exhaust_velocity)} kg/s")
        show_formula(fd.mass_flow_rate())
        print("")

    elif choice == "9":
        thrust = float(input("Thrust (N): "))
        mass_flow_rate = float(input("Mass Flow Rate (kg/s): "))
        print("")
        print(f"Specific Impulse = {aerospace.specific_impulse(thrust, mass_flow_rate)} s")
        show_formula(fd.specific_impulse())
        print("")

    elif choice == "10":
        specific_impulse = float(input("Specific Impulse (s): "))
        print("")
        print(f"Effective Exhaust Velocity = {aerospace.effective_exhaust_velocity(specific_impulse)} m/s")
        show_formula(fd.effective_exhaust_velocity())
        print("")

    elif choice == "11":
        initial_mass = float(input("Initial Mass (kg): "))
        final_mass = float(input("Final Mass (kg): "))
        exhaust_velocity = float(input("Exhaust Velocity (m/s): "))
        print("")
        print(f"Delta-v = {aerospace.rocket_equation(initial_mass, final_mass, exhaust_velocity)} m/s")
        show_formula(fd.rocket_equation())
        print("")

    elif choice == "12":
        mass = float(input("Planet Mass (kg): "))
        radius = float(input("Radius from Center (m): "))
        print("")
        print(f"Escape Velocity = {aerospace.escape_velocity(mass, radius)} m/s")
        show_formula(fd.escape_velocity())
        print("")

    elif choice == "13":
        print("")
        print(f"Earth Escape Velocity = {aerospace.earth_escape_velocity()} m/s")
        show_formula(fd.earth_escape_velocity())
        print("")

    elif choice == "14":
        gravitational_parameter = float(input("Gravitational Parameter μ (m³/s²): "))
        radius = float(input("Orbital Radius (m): "))
        print("")
        print(f"Orbital Velocity = {aerospace.orbital_velocity(gravitational_parameter, radius)} m/s")
        show_formula(fd.orbital_velocity())
        print("")

    elif choice == "15":
        radius = float(input("Orbital Radius from Earth's Center (m): "))
        print("")
        print(f"Earth Orbital Velocity = {aerospace.earth_orbital_velocity(radius)} m/s")
        show_formula(fd.earth_orbital_velocity())
        print("")

    elif choice == "16":
        gravitational_parameter = float(input("Gravitational Parameter μ (m³/s²): "))
        radius = float(input("Orbital Radius (m): "))
        print("")
        print(f"Orbital Period = {aerospace.orbital_period(gravitational_parameter, radius)} s")
        show_formula(fd.orbital_period())
        print("")

    elif choice == "17":
        radius = float(input("Orbital Radius from Earth's Center (m): "))
        print("")
        print(f"Earth Orbital Period = {aerospace.earth_orbital_period(radius)} s")
        show_formula(fd.earth_orbital_period())
        print("")

    elif choice == "18":
        gravitational_parameter = float(input("Gravitational Parameter μ (m³/s²): "))
        semi_major_axis = float(input("Semi-Major Axis (m): "))
        print("")
        print(f"Orbital Energy = {aerospace.orbital_energy(gravitational_parameter, semi_major_axis)} J/kg")
        show_formula(fd.orbital_energy())
        print("")

    elif choice == "19":
        velocity = float(input("Velocity (m/s): "))
        speed_of_sound = float(input("Speed of Sound (m/s): "))
        print("")
        print(f"Mach Number = {aerospace.mach_number(velocity, speed_of_sound)}")
        show_formula(fd.mach_number())
        print("")

    elif choice == "20":
        velocity = float(input("Velocity (m/s): "))
        print("")
        print(f"Earth Mach Number = {aerospace.earth_mach_number(velocity)}")
        show_formula(fd.earth_mach_number())
        print("")

    elif choice == "0":
        exit()