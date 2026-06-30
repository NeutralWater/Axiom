from formulas import astronomy
from topic_lib import astronomy_lib
import formula_display.core as core
import formula_display.display_astronomy as fd


def show_formula(formula):
    core.display_formula(formula)


def run_astronomy():
    astronomy_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        M = float(input("Mass of body (kg): "))
        r = float(input("Distance from center (m): "))
        print("")
        print(f"Escape Velocity = {astronomy.escape_velocity(M, r)} m/s")
        show_formula(fd.escape_velocity())

    elif choice == "2":
        M = float(input("Mass of central body (kg): "))
        r = float(input("Orbital radius (m): "))
        print("")
        print(f"Orbital Velocity = {astronomy.orbital_velocity(M, r)} m/s")
        show_formula(fd.orbital_velocity())

    elif choice == "3":
        M = float(input("Mass of central body (kg): "))
        r = float(input("Orbital radius (m): "))
        print("")
        print(f"Orbital Period = {astronomy.orbital_period(M, r)} s")
        show_formula(fd.orbital_period())

    elif choice == "4":
        m1 = float(input("Mass 1 (kg): "))
        m2 = float(input("Mass 2 (kg): "))
        r = float(input("Distance between centers (m): "))
        print("")
        print(f"Gravitational Force = {astronomy.gravitational_force(m1, m2, r)} N")
        show_formula(fd.gravitational_force())

    elif choice == "5":
        M = float(input("Mass of body (kg): "))
        r = float(input("Radius (m): "))
        print("")
        print(f"Surface Gravity = {astronomy.surface_gravity(M, r)} m/s²")
        show_formula(fd.surface_gravity())

    elif choice == "6":
        M = float(input("Mass of black hole (kg): "))
        print("")
        print(f"Schwarzschild Radius = {astronomy.schwarzschild_radius(M)} m")
        show_formula(fd.schwarzschild_radius())

    elif choice == "7":
        d = float(input("Distance (m): "))
        print("")
        print(f"Light Travel Time = {astronomy.light_travel_time(d)} s")
        show_formula(fd.light_travel_time())

    elif choice == "8":
        p = float(input("Parallax angle (arcseconds): "))
        print("")
        print(f"Distance = {astronomy.parallax_distance(p)} parsecs")
        show_formula(fd.parallax_distance())

    elif choice == "9":
        R = float(input("Radius (m): "))
        T = float(input("Temperature (K): "))
        print("")
        print(f"Luminosity = {astronomy.luminosity(R, T)} W")
        show_formula(fd.luminosity())

    elif choice == "10":
        L = float(input("Luminosity (W): "))
        d = float(input("Distance (m): "))
        print("")
        print(f"Flux = {astronomy.flux(L, d)} W/m²")
        show_formula(fd.flux())

    elif choice == "11":
        m = float(input("Apparent Magnitude: "))
        M = float(input("Absolute Magnitude: "))
        print("")
        print(f"Distance = {astronomy.distance_modulus(m, M)} parsecs")
        show_formula(fd.distance_modulus())

    elif choice == "12":
        H0 = float(input("Hubble Constant: "))
        d = float(input("Distance: "))
        print("")
        print(f"Recession Velocity = {astronomy.hubbles_law(H0, d)}")
        show_formula(fd.hubbles_law())

    elif choice == "13":
        z = float(input("Redshift: "))
        print("")
        print(f"Velocity = {astronomy.redshift_velocity(z)} m/s")
        show_formula(fd.redshift_velocity())

    elif choice == "14":
        M = float(input("Mass of central body (kg): "))
        r = float(input("Orbital radius (m): "))
        print("")
        print(f"Orbital Period = {astronomy.keplers_third_law(M, r)} s")
        show_formula(fd.keplers_third_law())

    elif choice == "15":
        T = float(input("Temperature (K): "))
        print("")
        print(f"Peak Wavelength = {astronomy.wiens_law(T)} m")
        show_formula(fd.wiens_law())

    elif choice == "16":
        A = float(input("Surface Area (m²): "))
        T = float(input("Temperature (K): "))
        print("")
        print(f"Power Radiated = {astronomy.stefan_boltzmann(A, T)} W")
        show_formula(fd.stefan_boltzmann())

    elif choice == "17":
        m = float(input("Mass (kg): "))
        print("")
        print(f"Energy = {astronomy.mass_energy(m)} J")
        show_formula(fd.mass_energy())

    elif choice == "18":
        delta_lambda = float(input("Change in Wavelength (m): "))
        wavelength = float(input("Original Wavelength (m): "))
        print("")
        print(f"Velocity = {astronomy.doppler_shift(delta_lambda, wavelength)} m/s")
        show_formula(fd.doppler_shift())

    elif choice == "19":
        R = float(input("Radius of Larger Body (m): "))
        M = float(input("Mass of Larger Body (kg): "))
        m = float(input("Mass of Smaller Body (kg): "))
        print("")
        print(f"Roche Limit = {astronomy.roche_limit(R, M, m)} m")
        show_formula(fd.roche_limit())

    elif choice == "20":
        a = float(input("Orbital Distance (m): "))
        M = float(input("Planet Mass (kg): "))
        m = float(input("Star Mass (kg): "))
        print("")
        print(f"Hill Sphere Radius = {astronomy.hill_sphere(a, M, m)} m")
        show_formula(fd.hill_sphere())

    elif choice == "21":
        Ve = float(input("Exhaust Velocity (m/s): "))
        m0 = float(input("Initial Mass (kg): "))
        mf = float(input("Final Mass (kg): "))
        print("")
        print(f"Δv = {astronomy.rocket_equation(Ve, m0, mf)} m/s")
        show_formula(fd.rocket_equation())

    elif choice == "22":
        M = float(input("Mass of Body (kg): "))
        m = float(input("Mass of Object (kg): "))
        r = float(input("Distance from Center (m): "))
        print("")
        print(f"Escape Energy = {astronomy.escape_energy(M, m, r)} J")
        show_formula(fd.escape_energy())
    
    elif choice == "0":
        exit()

    else:
        print("Invalid option.")