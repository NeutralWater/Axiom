from formulas import linear_algebra
from topic_lib import linear_algebra_lib

from formula_display.formula_display_core import display_formula
from formula_display import display_linear_algebra as fd


def show_formula(formula):
    display_formula(formula)


def get_vector(name):
    data = input(f"Enter {name} vector values (comma-separated): ")
    return [float(x.strip()) for x in data.split(",")]


def get_matrix(name):
    rows = int(input(f"Rows in {name}: "))
    matrix = []

    for i in range(rows):
        row = input(f"{name} row {i + 1} values (comma-separated): ")
        matrix.append([float(x.strip()) for x in row.split(",")])

    return matrix


def run_linear_algebra():
    linear_algebra_lib()
    choice = input("Pick a formula: ")
    print("")

    if choice == "1":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.dot_product(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Dot Product = {result}")

        show_formula(fd.dot_product())
        print("")

    elif choice == "2":
        v = get_vector("vector")
        print("")
        print(f"Magnitude = {linear_algebra.magnitude(v)}")
        show_formula(fd.magnitude())
        print("")

    elif choice == "3":
        v = get_vector("vector")
        print("")

        result = linear_algebra.unit_vector(v)

        if result is None:
            print("The zero vector has no unit vector.")
        else:
            print(f"Unit Vector = {result}")

        show_formula(fd.unit_vector())
        print("")

    elif choice == "4":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.vector_addition(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Vector Sum = {result}")

        show_formula(fd.vector_addition())
        print("")

    elif choice == "5":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.vector_subtraction(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print(f"Vector Difference = {result}")

        show_formula(fd.vector_subtraction())
        print("")

    elif choice == "6":
        c = float(input("Scalar: "))
        v = get_vector("vector")
        print("")
        print(f"Scalar Product = {linear_algebra.scalar_multiplication(c, v)}")
        show_formula(fd.scalar_multiplication())
        print("")

    elif choice == "7":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.cross_product(v1, v2)

        if result is None:
            print("Cross product only works for 3D vectors.")
        else:
            print(f"Cross Product = {result}")

        show_formula(fd.cross_product())
        print("")

    elif choice == "8":
        A = get_matrix("A")
        B = get_matrix("B")
        print("")

        result = linear_algebra.matrix_addition(A, B)

        if result is None:
            print("Matrices must have the same dimensions.")
        else:
            print(f"Matrix Sum = {result}")

        show_formula(fd.matrix_addition())
        print("")

    elif choice == "9":
        A = get_matrix("A")
        B = get_matrix("B")
        print("")

        result = linear_algebra.matrix_subtraction(A, B)

        if result is None:
            print("Matrices must have the same dimensions.")
        else:
            print(f"Matrix Difference = {result}")

        show_formula(fd.matrix_subtraction())
        print("")

    elif choice == "10":
        A = get_matrix("A")
        B = get_matrix("B")
        print("")

        result = linear_algebra.matrix_multiplication(A, B)

        if result is None:
            print("Columns of A must equal rows of B.")
        else:
            print(f"Matrix Product = {result}")

        show_formula(fd.matrix_multiplication())
        print("")

    elif choice == "11":
        A = get_matrix("A")
        print("")
        print(f"Transpose = {linear_algebra.transpose(A)}")
        show_formula(fd.transpose())
        print("")

    elif choice == "12":
        A = get_matrix("A")
        print("")

        result = linear_algebra.determinant_2x2(A)

        if result is None:
            print("Determinant option only supports 2x2 matrices right now.")
        else:
            print(f"Determinant = {result}")

        show_formula(fd.determinant_2x2())
        print("")

    elif choice == "13":
        A = get_matrix("A")
        print("")

        result = linear_algebra.trace(A)

        if result is None:
            print("Trace only works for square matrices.")
        else:
            print(f"Trace = {result}")

        show_formula(fd.trace())
        print("")

    elif choice == "0":
        exit()