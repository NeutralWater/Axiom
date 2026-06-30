from formulas import geometry
from topic_lib import geometry_lib
import math
import formula_display

def show_formula(formula):
    formula_display.display_formula(formula)

def run_geometry():
    geometry_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        r = float(input("Radius: "))
        print("")
        print(f"Area of Circle = {geometry.circle_area(r)}")
        show_formula(formula_display.circle_area())
        print("")
    
    elif choice == "2":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("")
        print(f"Area of Rectangle = {geometry.rectangle_area(l, w)}")
        show_formula(formula_display.rectangle_area())
        print("")

    elif choice == "3":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("")
        print(f"Area of Triangle = {geometry.triangle_area(b, h)}")
        show_formula(formula_display.triangle_area())
        print("")

    elif choice == "4":
        r = float(input("Radius: "))
        print("")
        print(f"Circumference of Circle = {geometry.circle_circumference(r)}")
        show_formula(formula_display.circle_circumference())
        print("")

    elif choice == "5":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("")
        print(f"Perimeter of Rectangle = {geometry.perimeter_of_rectangle(l, w)}")
        show_formula(formula_display.perimeter_of_rectangle())
        print("")
    
    elif choice == "6":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        print("")
        print(f"Hypotenuse = {geometry.pythagorean_theorem(a, b)}")
        show_formula(formula_display.pythagorean_theorem())
        print("")

    elif choice == "7":
        r = float(input("Radius: "))
        print("")
        print(f"Volume of Sphere = {geometry.volume_of_sphere(r)}")
        show_formula(formula_display.volume_of_sphere())
        print("")

    elif choice == "8":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Cylinder = {geometry.volume_of_cylinder(r, h)}")
        show_formula(formula_display.volume_of_cylinder())
        print("")
    
    elif choice == "9":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Cone = {geometry.volume_of_cone(r, h)}")
        show_formula(formula_display.volume_of_cone())
        print("")

    elif choice == "10":
        base_area = float(input("Base Area: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Prism = {geometry.volume_of_prism(base_area, h)}")
        show_formula(formula_display.volume_of_prism())
        print("")
    
    elif choice == "11":
        base_area = float(input("Base Area: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Pyramid = {geometry.volume_of_pyramid(base_area, h)}")
        show_formula(formula_display.volume_of_pyramid())
        print("")

    elif choice == "12":
        R = float(input("Major Radius: "))
        r = float(input("Minor Radius: "))
        print("")
        print(f"Volume of Torus = {geometry.volume_of_torus(R, r)}")
        show_formula(formula_display.volume_of_torus())
        print("")

    elif choice == "13":
        a = float(input("Semi-axis a: "))
        b = float(input("Semi-axis b: "))
        c = float(input("Semi-axis c: "))
        print("")
        print(f"Volume of Ellipsoid = {geometry.volume_of_ellipsoid(a, b, c)}")
        show_formula(formula_display.volume_of_ellipsoid())
        print("")

    elif choice == "14":
        r1 = float(input("Radius 1: "))
        r2 = float(input("Radius 2: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Frustum = {geometry.volume_of_frustum(r1, r2, h)}")
        show_formula(formula_display.volume_of_frustum())
        print("")

    elif choice == "15":
        r = float(input("Radius: "))
        print("")
        print(f"Surface Area of Sphere = {geometry.surface_area_of_sphere(r)}")
        show_formula(formula_display.surface_area_of_sphere())
        print("")
    
    elif choice == "16":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Cylinder = {geometry.surface_area_of_cylinder(r, h)}")
        show_formula(formula_display.surface_area_of_cylinder())
        print("")
    
    elif choice == "17":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Cone = {geometry.surface_area_of_cone(r, h)}")
        show_formula(formula_display.surface_area_of_cone())
        print("")
    elif choice == "18":
        base_perimeter = float(input("Base Perimeter: "))
        base_area = float(input("Base Area: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Prism = {geometry.surface_area_of_prism(base_perimeter, base_area, h)}")
        show_formula(formula_display.surface_area_of_prism())
        print("")

    elif choice == "19":
        base_perimeter = float(input("Base Perimeter: "))
        base_area = float(input("Base Area: "))
        slant_height = float(input("Slant Height: "))
        print("")
        print(f"Surface Area of Pyramid = {geometry.surface_area_of_pyramid(base_perimeter, base_area, slant_height)}")
        show_formula(formula_display.surface_area_of_pyramid())
        print("")

    elif choice == "20":
        R = float(input("Major Radius: "))
        r = float(input("Minor Radius: "))
        print("")
        print(f"Surface Area of Torus = {geometry.surface_area_of_torus(R, r)}")
        show_formula(formula_display.surface_area_of_torus())
        print("")

    elif choice == "21":
        a = float(input("Semi-axis a: "))
        b = float(input("Semi-axis b: "))
        c = float(input("Semi-axis c: "))
        print("")
        print(f"Surface Area of Ellipsoid = {geometry.surface_area_of_ellipsoid(a, b, c)}")
        show_formula(formula_display.surface_area_of_ellipsoid())
        print("")

    elif choice == "22":
        r1 = float(input("Radius 1: "))
        r2 = float(input("Radius 2: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Frustum = {geometry.surface_area_of_frustum(r1, r2, h)}")
        show_formula(formula_display.surface_area_of_frustum())
        print("")
    
    
    elif choice == "0":
        exit()