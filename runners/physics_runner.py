from formulas import physics
from topic_lib import physics_lib
import formula_display.core as core
import formula_display.display_physics as fd


def show_formula(formula):
    core.display_formula(formula)


def get_resistors():
    count = int(input("Number of resistors: "))
    resistors = []

    for i in range(count):
        resistance = float(input(f"Resistance {i + 1} (Ω): "))
        resistors.append(resistance)

    return resistors


def run_physics():
    physics_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("")
        print(f"Kinetic Energy = {physics.kinetic_energy(m, v)} J")
        show_formula(fd.kinetic_energy())
        print("")

    elif choice == "2":
        m = float(input("Mass (kg): "))
        a = float(input("Acceleration (m/s²): "))
        print("")
        print(f"Force = {physics.force(m, a)} N")
        show_formula(fd.force())
        print("")

    elif choice == "3":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        print("")
        print(f"Momentum = {physics.momentum(m, v)} kg·m/s")
        show_formula(fd.momentum())
        print("")

    elif choice == "4":
        f = float(input("Force (N): "))
        d = float(input("Distance (m): "))
        print("")
        print(f"Work = {physics.work(f, d)} J")
        show_formula(fd.work())
        print("")

    elif choice == "5":
        d = float(input("Distance (m): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Speed = {physics.speed(d, t)} m/s")
        show_formula(fd.speed())
        print("")

    elif choice == "6":
        vf = float(input("Final Velocity (m/s): "))
        vi = float(input("Initial Velocity (m/s): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Acceleration = {physics.acceleration(vf, vi, t)} m/s²")
        show_formula(fd.acceleration())
        print("")

    elif choice == "7":
        vi = float(input("Initial Velocity (m/s): "))
        vf = float(input("Final Velocity (m/s): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Displacement = {physics.displacement_average_velocity(vi, vf, t)} m")
        show_formula(fd.displacement_average_velocity())
        print("")

    elif choice == "8":
        vi = float(input("Initial Velocity (m/s): "))
        t = float(input("Time (s): "))
        a = float(input("Acceleration (m/s²): "))
        print("")
        print(f"Displacement = {physics.displacement_acceleration(vi, t, a)} m")
        show_formula(fd.displacement_acceleration())
        print("")

    elif choice == "9":
        vi = float(input("Initial Velocity (m/s): "))
        a = float(input("Acceleration (m/s²): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Final Velocity = {physics.final_velocity(vi, a, t)} m/s")
        show_formula(fd.final_velocity())
        print("")

    elif choice == "10":
        vi = float(input("Initial Velocity (m/s): "))
        a = float(input("Acceleration (m/s²): "))
        d = float(input("Displacement (m): "))
        print("")
        print(f"Final Velocity = {physics.final_velocity_squared(vi, a, d)} m/s")
        show_formula(fd.final_velocity_squared())
        print("")

    elif choice == "11":
        h = float(input("Height (m): "))
        print("")
        print(f"Free Fall Time = {physics.free_fall_time(h)} s")
        show_formula(fd.free_fall_time())
        print("")

    elif choice == "12":
        m = float(input("Mass (kg): "))
        print("")
        print(f"Weight = {physics.weight(m)} N")
        show_formula(fd.weight())
        print("")

    elif choice == "13":
        mu = float(input("Coefficient of Friction: "))
        fn = float(input("Normal Force (N): "))
        print("")
        print(f"Friction = {physics.friction(mu, fn)} N")
        show_formula(fd.friction())
        print("")

    elif choice == "14":
        m = float(input("Mass (kg): "))
        print("")
        print(f"Normal Force = {physics.normal_force(m)} N")
        show_formula(fd.normal_force())
        print("")

    elif choice == "15":
        m1 = float(input("Mass 1 (kg): "))
        m2 = float(input("Mass 2 (kg): "))
        r = float(input("Distance (m): "))
        print("")
        print(f"Gravitational Force = {physics.gravitational_force(m1, m2, r)} N")
        show_formula(fd.gravitational_force())
        print("")

    elif choice == "16":
        m = float(input("Mass (kg): "))
        v = float(input("Velocity (m/s): "))
        r = float(input("Radius (m): "))
        print("")
        print(f"Centripetal Force = {physics.centripetal_force(m, v, r)} N")
        show_formula(fd.centripetal_force())
        print("")

    elif choice == "17":
        v = float(input("Velocity (m/s): "))
        r = float(input("Radius (m): "))
        print("")
        print(f"Centripetal Acceleration = {physics.centripetal_acceleration(v, r)} m/s²")
        show_formula(fd.centripetal_acceleration())
        print("")

    elif choice == "18":
        m = float(input("Mass (kg): "))
        h = float(input("Height (m): "))
        print("")
        print(f"Potential Energy = {physics.potential_energy(m, h)} J")
        show_formula(fd.potential_energy())
        print("")

    elif choice == "19":
        ke = float(input("Kinetic Energy (J): "))
        pe = float(input("Potential Energy (J): "))
        print("")
        print(f"Mechanical Energy = {physics.mechanical_energy(ke, pe)} J")
        show_formula(fd.mechanical_energy())
        print("")

    elif choice == "20":
        w = float(input("Work (J): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Power = {physics.power(w, t)} W")
        show_formula(fd.power())
        print("")

    elif choice == "21":
        output_work = float(input("Output Work (J): "))
        input_work = float(input("Input Work (J): "))
        print("")
        print(f"Efficiency = {physics.efficiency(output_work, input_work)}%")
        show_formula(fd.efficiency())
        print("")

    elif choice == "22":
        f = float(input("Force (N): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Impulse = {physics.impulse(f, t)} N·s")
        show_formula(fd.impulse())
        print("")

    elif choice == "23":
        pf = float(input("Final Momentum (kg·m/s): "))
        pi = float(input("Initial Momentum (kg·m/s): "))
        print("")
        print(f"Change in Momentum = {physics.change_in_momentum(pf, pi)} kg·m/s")
        show_formula(fd.change_in_momentum())
        print("")

    elif choice == "24":
        f = float(input("Frequency (Hz): "))
        wavelength = float(input("Wavelength (m): "))
        print("")
        print(f"Wave Speed = {physics.wave_speed(f, wavelength)} m/s")
        show_formula(fd.wave_speed())
        print("")

    elif choice == "25":
        v = float(input("Wave Speed (m/s): "))
        wavelength = float(input("Wavelength (m): "))
        print("")
        print(f"Frequency = {physics.frequency(v, wavelength)} Hz")
        show_formula(fd.frequency())
        print("")

    elif choice == "26":
        v = float(input("Wave Speed (m/s): "))
        f = float(input("Frequency (Hz): "))
        print("")
        print(f"Wavelength = {physics.wavelength(v, f)} m")
        show_formula(fd.wavelength())
        print("")

    elif choice == "27":
        f = float(input("Frequency (Hz): "))
        print("")
        print(f"Period = {physics.period(f)} s")
        show_formula(fd.period())
        print("")

    elif choice == "28":
        t = float(input("Period (s): "))
        print("")
        print(f"Frequency = {physics.frequency_from_period(t)} Hz")
        show_formula(fd.frequency_from_period())
        print("")

    elif choice == "29":
        v = float(input("Voltage (V): "))
        r = float(input("Resistance (Ω): "))
        print("")
        print(f"Current = {physics.ohms_law(v, r)} A")
        show_formula(fd.ohms_law())
        print("")

    elif choice == "30":
        i = float(input("Current (A): "))
        r = float(input("Resistance (Ω): "))
        print("")
        print(f"Voltage = {physics.voltage(i, r)} V")
        show_formula(fd.voltage())
        print("")

    elif choice == "31":
        v = float(input("Voltage (V): "))
        i = float(input("Current (A): "))
        print("")
        print(f"Resistance = {physics.resistance(v, i)} Ω")
        show_formula(fd.resistance())
        print("")

    elif choice == "32":
        v = float(input("Voltage (V): "))
        i = float(input("Current (A): "))
        print("")
        print(f"Electrical Power = {physics.electrical_power_vi(v, i)} W")
        show_formula(fd.electrical_power_vi())
        print("")

    elif choice == "33":
        i = float(input("Current (A): "))
        r = float(input("Resistance (Ω): "))
        print("")
        print(f"Electrical Power = {physics.electrical_power_i2r(i, r)} W")
        show_formula(fd.electrical_power_i2r())
        print("")

    elif choice == "34":
        v = float(input("Voltage (V): "))
        r = float(input("Resistance (Ω): "))
        print("")
        print(f"Electrical Power = {physics.electrical_power_v2r(v, r)} W")
        show_formula(fd.electrical_power_v2r())
        print("")

    elif choice == "35":
        i = float(input("Current (A): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Charge = {physics.charge(i, t)} C")
        show_formula(fd.charge())
        print("")

    elif choice == "36":
        q = float(input("Charge (C): "))
        t = float(input("Time (s): "))
        print("")
        print(f"Current = {physics.current(q, t)} A")
        show_formula(fd.current())
        print("")

    elif choice == "37":
        resistors = get_resistors()
        print("")
        print(f"Series Resistance = {physics.resistance_series(*resistors)} Ω")
        show_formula(fd.resistance_series())
        print("")

    elif choice == "38":
        resistors = get_resistors()
        print("")
        print(f"Parallel Resistance = {physics.resistance_parallel(*resistors)} Ω")
        show_formula(fd.resistance_parallel())
        print("")

    elif choice == "39":
        q1 = float(input("Charge 1 (C): "))
        q2 = float(input("Charge 2 (C): "))
        r = float(input("Distance (m): "))
        print("")
        print(f"Electric Force = {physics.coulombs_law(q1, q2, r)} N")
        show_formula(fd.coulombs_law())
        print("")

    elif choice == "40":
        f = float(input("Force (N): "))
        q = float(input("Charge (C): "))
        print("")
        print(f"Electric Field = {physics.electric_field(f, q)} N/C")
        show_formula(fd.electric_field())
        print("")

    elif choice == "0":
        exit()