from formulas import geometry
from topic_lib import geometry_lib

import formula_display.core as core
import formula_display.display_geometry as fd


def show_formula(formula):
    core.display_formula(formula)

def run_geometry():
    geometry_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        r = float(input("Radius: "))
        print("")
        print(f"Area of Circle = {geometry.circle_area(r)}")
        show_formula(fd.circle_area())
        print("")
    
    elif choice == "2":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("")
        print(f"Area of Rectangle = {geometry.rectangle_area(l, w)}")
        show_formula(fd.rectangle_area())
        print("")

    elif choice == "3":
        b = float(input("Base: "))
        h = float(input("Height: "))
        print("")
        print(f"Area of Triangle = {geometry.triangle_area(b, h)}")
        show_formula(fd.triangle_area())
        print("")

    elif choice == "4":
        r = float(input("Radius: "))
        print("")
        print(f"Circumference of Circle = {geometry.circle_circumference(r)}")
        show_formula(fd.circle_circumference())
        print("")

    elif choice == "5":
        l = float(input("Length: "))
        w = float(input("Width: "))
        print("")
        print(f"Perimeter of Rectangle = {geometry.rectangle_perimeter(l, w)}")
        show_formula(fd.rectangle_perimeter())
        print("")
    
    elif choice == "6":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        print("")
        print(f"Hypotenuse = {geometry.pythagorean(a, b)}")
        show_formula(fd.pythagorean())
        print("")

    #3d volumes
    elif choice == "7":
        r = float(input("Radius: "))
        print("")
        print(f"Volume of Sphere = {geometry.sphere_volume(r)}")
        show_formula(fd.sphere_volume())
        print("")

    elif choice == "8":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Cylinder = {geometry.cylinder_volume(r, h)}")
        show_formula(fd.cylinder_volume())
        print("")
    
    elif choice == "9":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Cone = {geometry.cone_volume(r, h)}")
        show_formula(fd.cone_volume())
        print("")

    elif choice == "10":
        base_area = float(input("Base Area: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Prism = {geometry.prism_volume(base_area, h)}")
        show_formula(fd.prism_volume())
        print("")
    
    elif choice == "11":
        base_area = float(input("Base Area: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Pyramid = {geometry.pyramid_volume(base_area, h)}")
        show_formula(fd.pyramid_volume())
        print("")

    elif choice == "12":
        R = float(input("Major Radius: "))
        r = float(input("Minor Radius: "))
        print("")
        print(f"Volume of Torus = {geometry.torus_volume(R, r)}")
        show_formula(fd.torus_volume())
        print("")

    elif choice == "13":
        a = float(input("Semi-axis a: "))
        b = float(input("Semi-axis b: "))
        c = float(input("Semi-axis c: "))
        print("")
        print(f"Volume of Ellipsoid = {geometry.ellipsoid_volume(a, b, c)}")
        show_formula(fd.ellipsoid_volume())
        print("")

    elif choice == "14":
        r1 = float(input("Radius 1: "))
        r2 = float(input("Radius 2: "))
        h = float(input("Height: "))
        print("")
        print(f"Volume of Frustum = {geometry.frustum_volume(r1, r2, h)}")
        show_formula(fd.frustum_volume())
        print("")
    
    #3d surface area
    elif choice == "15":
        r = float(input("Radius: "))
        print("")
        print(f"Surface Area of Sphere = {geometry.sphere_surface_area(r)}")
        show_formula(fd.sphere_surface_area())
        print("")
    
    elif choice == "16":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Cylinder = {geometry.cylinder_surface_area(r, h)}")
        show_formula(fd.cylinder_surface_area())
        print("")
    
    elif choice == "17":
        r = float(input("Radius: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Cone = {geometry.cone_surface_area(r, h)}")
        show_formula(fd.cone_surface_area())
        print("")

    elif choice == "18":
        base_perimeter = float(input("Base Perimeter: "))
        base_area = float(input("Base Area: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Prism = {geometry.prism_surface_area(base_perimeter, base_area, h)}")
        show_formula(fd.prism_surface_area())
        print("")

    elif choice == "19":
        base_perimeter = float(input("Base Perimeter: "))
        base_area = float(input("Base Area: "))
        slant_height = float(input("Slant Height: "))
        print("")
        print(f"Surface Area of Pyramid = {geometry.pyramid_surface_area(base_perimeter, base_area, slant_height)}")
        show_formula(fd.pyramid_surface_area())
        print("")

    elif choice == "20":
        R = float(input("Major Radius: "))
        r = float(input("Minor Radius: "))
        print("")
        print(f"Surface Area of Torus = {geometry.torus_surface_area(R, r)}")
        show_formula(fd.torus_surface_area())
        print("")

    elif choice == "21":
        a = float(input("Semi-axis a: "))
        b = float(input("Semi-axis b: "))
        c = float(input("Semi-axis c: "))
        print("")
        print(f"Surface Area of Ellipsoid = {geometry.ellipsoid_surface_area(a, b, c)}")
        show_formula(fd.ellipsoid_surface_area())
        print("")

    elif choice == "22":
        r1 = float(input("Radius 1: "))
        r2 = float(input("Radius 2: "))
        h = float(input("Height: "))
        print("")
        print(f"Surface Area of Frustum = {geometry.frustum_surface_area(r1, r2, h)}")
        show_formula(fd.frustum_surface_area())
        print("")
    
    
    elif choice == "0":
        exit()