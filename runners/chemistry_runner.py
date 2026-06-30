from formulas import chemistry
from topic_lib import chemistry_lib

import formula_display.core as core
import formula_display.display_chemistry as fd


def show_formula(formula):
    core.display_formula(formula)


def run_chemistry():
    chemistry_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        mass = float(input("Mass: "))
        volume = float(input("Volume: "))
        print("")
        print(f"Density = {chemistry.density(mass, volume)}")
        show_formula(fd.density())
        print("")

    elif choice == "2":
        moles = float(input("Moles of solute: "))
        liters = float(input("Liters of solution: "))
        print("")
        print(f"Molarity = {chemistry.molarity(moles, liters)} M")
        show_formula(fd.molarity())
        print("")

    elif choice == "3":
        moles = float(input("Moles of solute: "))
        kilograms = float(input("Kilograms of solvent: "))
        print("")
        print(f"Molality = {chemistry.molality(moles, kilograms)} m")
        show_formula(fd.molality())
        print("")

    elif choice == "4":
        M1 = float(input("Initial molarity M1: "))
        V1 = float(input("Initial volume V1: "))

        print("")
        print("Solve for:")
        print("1. Final molarity M2")
        print("2. Final volume V2")
        solve = input("Choice: ")

        if solve == "1":
            V2 = float(input("Final volume V2: "))
            result = chemistry.dilution(M1, V1, V2=V2)
            print(f"M2 = {result}")

        elif solve == "2":
            M2 = float(input("Final molarity M2: "))
            result = chemistry.dilution(M1, V1, M2=M2)
            print(f"V2 = {result}")

        show_formula(fd.dilution())
        print("")

    elif choice == "5":
        mass = float(input("Mass: "))
        specific_heat = float(input("Specific heat: "))
        delta_temp = float(input("Change in temperature ΔT: "))
        print("")
        print(f"Heat = {chemistry.heat(mass, specific_heat, delta_temp)} J")
        show_formula(fd.heat())
        print("")

    elif choice == "6":
        q = float(input("Heat q: "))
        mass = float(input("Mass: "))
        delta_temp = float(input("Change in temperature ΔT: "))
        print("")
        print(f"Specific Heat = {chemistry.specific_heat(q, mass, delta_temp)}")
        show_formula(fd.specific_heat())
        print("")

    elif choice == "7":
        P1 = float(input("Initial pressure P1: "))
        V1 = float(input("Initial volume V1: "))

        print("")
        print("Solve for:")
        print("1. Final pressure P2")
        print("2. Final volume V2")
        solve = input("Choice: ")

        if solve == "1":
            V2 = float(input("Final volume V2: "))
            print(f"P2 = {chemistry.boyles_law(P1, V1, V2=V2)}")

        elif solve == "2":
            P2 = float(input("Final pressure P2: "))
            print(f"V2 = {chemistry.boyles_law(P1, V1, P2=P2)}")

        show_formula(fd.boyles_law())
        print("")

    elif choice == "8":
        V1 = float(input("Initial volume V1: "))
        T1 = float(input("Initial temperature T1 (K): "))

        print("")
        print("Solve for:")
        print("1. Final volume V2")
        print("2. Final temperature T2")
        solve = input("Choice: ")

        if solve == "1":
            T2 = float(input("Final temperature T2 (K): "))
            print(f"V2 = {chemistry.charles_law(V1, T1, T2=T2)}")

        elif solve == "2":
            V2 = float(input("Final volume V2: "))
            print(f"T2 = {chemistry.charles_law(V1, T1, V2=V2)}")

        show_formula(fd.charles_law())
        print("")

    elif choice == "9":
        P1 = float(input("Initial pressure P1: "))
        T1 = float(input("Initial temperature T1 (K): "))

        print("")
        print("Solve for:")
        print("1. Final pressure P2")
        print("2. Final temperature T2")
        solve = input("Choice: ")

        if solve == "1":
            T2 = float(input("Final temperature T2 (K): "))
            print(f"P2 = {chemistry.gay_lussac_law(P1, T1, T2=T2)}")

        elif solve == "2":
            P2 = float(input("Final pressure P2: "))
            print(f"T2 = {chemistry.gay_lussac_law(P1, T1, P2=P2)}")

        show_formula(fd.gay_lussac_law())
        print("")

    elif choice == "10":
        P1 = float(input("Initial pressure P1: "))
        V1 = float(input("Initial volume V1: "))
        T1 = float(input("Initial temperature T1 (K): "))

        print("")
        print("Solve for:")
        print("1. Final pressure P2")
        print("2. Final volume V2")
        print("3. Final temperature T2")
        solve = input("Choice: ")

        if solve == "1":
            V2 = float(input("Final volume V2: "))
            T2 = float(input("Final temperature T2 (K): "))
            print(f"P2 = {chemistry.combined_gas_law(P1, V1, T1, V2=V2, T2=T2)}")

        elif solve == "2":
            P2 = float(input("Final pressure P2: "))
            T2 = float(input("Final temperature T2 (K): "))
            print(f"V2 = {chemistry.combined_gas_law(P1, V1, T1, P2=P2, T2=T2)}")

        elif solve == "3":
            P2 = float(input("Final pressure P2: "))
            V2 = float(input("Final volume V2: "))
            print(f"T2 = {chemistry.combined_gas_law(P1, V1, T1, P2=P2, V2=V2)}")

        show_formula(fd.combined_gas_law())
        print("")

    elif choice == "11":
        print("Solve for:")
        print("1. Pressure P")
        print("2. Volume V")
        print("3. Moles n")
        print("4. Temperature T")
        solve = input("Choice: ")
        print("")

        if solve == "1":
            V = float(input("Volume V: "))
            n = float(input("Moles n: "))
            T = float(input("Temperature T (K): "))
            print(f"P = {chemistry.ideal_gas_law(V=V, n=n, T=T)}")

        elif solve == "2":
            P = float(input("Pressure P: "))
            n = float(input("Moles n: "))
            T = float(input("Temperature T (K): "))
            print(f"V = {chemistry.ideal_gas_law(P=P, n=n, T=T)}")

        elif solve == "3":
            P = float(input("Pressure P: "))
            V = float(input("Volume V: "))
            T = float(input("Temperature T (K): "))
            print(f"n = {chemistry.ideal_gas_law(P=P, V=V, T=T)}")

        elif solve == "4":
            P = float(input("Pressure P: "))
            V = float(input("Volume V: "))
            n = float(input("Moles n: "))
            print(f"T = {chemistry.ideal_gas_law(P=P, V=V, n=n)}")

        show_formula(fd.ideal_gas_law())
        print("")

    elif choice == "0":
        exit()