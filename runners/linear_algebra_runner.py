from formulas import linear_algebra
from topic_lib import linear_algebra_lib
import formula_display.display_linear_algebra as fd
import formula_display.core as core

from sympy import N, pretty
from sympy.matrices import MatrixBase

def show_formula(formula):
    core.display_formula(formula)

def clean_value(value, digits=6):
    if isinstance(value, float):
        return round(value, digits)

    if isinstance(value, MatrixBase):
        return N(value, digits)

    if isinstance(value, list):
        return [clean_value(item, digits) for item in value]

    if isinstance(value, tuple):
        return tuple(clean_value(item, digits) for item in value)

    if isinstance(value, dict):
        return {
            clean_value(key, digits): clean_value(val, digits)
            for key, val in value.items()
        }

    try:
        return N(value, digits)
    except Exception:
        return value

def print_result(title, result):
    result = clean_value(result)

    print(f"{title}:")

    if isinstance(result, MatrixBase):
        print(pretty(result))
        print("")
        return

    if isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
        print("")
        return

    if isinstance(result, (list, tuple)):
        if len(result) == 0:
            print("[]")
            print("")
            return

        for i, item in enumerate(result, start=1):
            if isinstance(item, MatrixBase):
                print(f"{i}.")
                print(pretty(item))
            else:
                print(f"{i}. {item}")
        print("")
        return

    print(result)
    print("")


def get_vector(name):
    data = input(f"Enter {name} vector values (comma-separated): ")
    return [float(x.strip()) for x in data.split(",")]

def get_vectors():
    count = int(input("Number of vectors: "))
    vectors = []

    for i in range(count):
        vectors.append(get_vector(f"vector {i + 1}"))

    return vectors

def get_matrix(name):
    rows = int(input(f"Rows in {name}: "))
    cols = int(input(f"Columns in {name}: "))

    matrix = []

    for i in range(rows):
        while True:
            row = [float(x.strip()) for x in input(
                f"{name} row {i + 1} values (comma-separated): "
            ).split(",")]

            if len(row) == cols:
                matrix.append(row)
                break

            print(f"Please enter exactly {cols} values.")

    return matrix

def get_linear_system():
    n = int(input("Number of variables/equations: "))

    A = []
    b = []

    print("")

    for i in range(n):
        while True:
            row = [float(x.strip()) for x in input(
                f"Equation {i + 1} coefficients (comma-separated): "
            ).split(",")]

            if len(row) == n:
                break

            print(f"Please enter exactly {n} coefficients.")

        constant = float(input(f"Equation {i + 1} constant: "))

        A.append(row)
        b.append(constant)

        print("")

    return A, b

def run_linear_algebra():
    linear_algebra_lib()
    choice = input("Select a formula: ")
    print("")

    if choice == "1":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")

        result = linear_algebra.dot_product(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print_result("Dot Product", result)

        show_formula(fd.dot_product())
        print("")

    elif choice == "2":
        v = get_vector("vector")
        print("")
        print_result("Magnitude", linear_algebra.magnitude(v))
        show_formula(fd.magnitude())
        print("")

    elif choice == "3":
        v = get_vector("vector")
        print("")

        result = linear_algebra.unit_vector(v)

        if result is None:
            print("The zero vector has no unit vector.")
        else:
            print_result("Unit Vector", result)

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
            print_result("Vector Sum", result)

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
            print_result("Vector Difference", result)

        show_formula(fd.vector_subtraction())
        print("")

    elif choice == "6":
        c = float(input("Scalar: "))
        v = get_vector("vector")
        print("")
        print_result("Scalar Product", linear_algebra.scalar_multiplication(c, v))
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
            print_result("Cross Product", result)

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
            print_result("Matrix Sum", result)

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
            print_result("Matrix Difference", result)

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
            print_result("Matrix Product", result)

        show_formula(fd.matrix_multiplication())
        print("")

    elif choice == "11":
        A = get_matrix("A")
        print("")
        print_result("Transpose", linear_algebra.transpose(A))
        show_formula(fd.transpose())
        print("")

    elif choice == "12":
        A = get_matrix("A")
        print("")

        result = linear_algebra.determinant_2x2(A)

        if result is None:
            print("Determinant option only supports 2x2 matrices right now.")
        else:
            print_result("Determinant", result)

        show_formula(fd.determinant_2x2())
        print("")

    elif choice == "13":
        A = get_matrix("A")
        print("")

        result = linear_algebra.trace(A)

        if result is None:
            print("Trace only works for square matrices.")
        else:
            print_result("Trace", result)

        show_formula(fd.trace())
        print("")

    elif choice == "14":
        A = get_matrix("A")
        print("")
        result = linear_algebra.matrix_inverse(A)

        if result is None:
            print("Matrix must be square and invertible.")
        else:
            print_result("Inverse", result)

        show_formula(fd.matrix_inverse())
        print("")

    elif choice == "15":
        A = get_matrix("A")
        print("")
        print_result("Rank", linear_algebra.matrix_rank(A))
        show_formula(fd.matrix_rank())
        print("")

    elif choice == "16":
        A = get_matrix("A")
        print("")
        print_result("RREF", linear_algebra.rref(A))
        show_formula(fd.rref())
        print("")

    elif choice == "17":
        A = get_matrix("A")
        print("")
        result = linear_algebra.determinant(A)

        if result is None:
            print("Determinant only works for square matrices.")
        else:
            print_result("Determinant", result)

        show_formula(fd.determinant())
        print("")

    elif choice == "18":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")
        result = linear_algebra.angle_between_vectors(v1, v2)

        if result is None:
            print("Vectors must have same dimensions and cannot be zero vectors.")
        else:
            print_result("Angle (degrees)", result)

        show_formula(fd.angle_between_vectors())
        print("")

    elif choice == "19":
        v1 = get_vector("vector")
        v2 = get_vector("projection target")
        print("")
        result = linear_algebra.vector_projection(v1, v2)

        if result is None:
            print("Projection target cannot be the zero vector.")
        else:
            print_result("Projection", result)

        show_formula(fd.vector_projection())
        print("")

    elif choice == "20":
        v1 = get_vector("first")
        v2 = get_vector("second")
        print("")
        result = linear_algebra.distance_between_vectors(v1, v2)

        if result is None:
            print("Vectors must have the same number of components.")
        else:
            print_result("Distance", result)

        show_formula(fd.distance_between_vectors())
        print("")

    elif choice == "21":
        A = get_matrix("A")
        print("")
        print_result("Eigenvalues", linear_algebra.eigenvalues(A))
        show_formula(fd.eigenvalues())
        print("")
    
    elif choice == "22":
        A = get_matrix("A")
        print("")

        result = linear_algebra.eigenvectors(A)

        if result is None:
            print("Unable to compute eigenvectors.")
        else:
            print("Eigenvectors:\n")

            for i, item in enumerate(result, start=1):
                eigenvalue = round(float(item["eigenvalue"]), 6)

                print(f"Eigenvalue {i}: {eigenvalue}")
                print(f"Multiplicity: {item['multiplicity']}")

                for j, vec in enumerate(item["vectors"], start=1):
                    print(f"Vector {j}:")

                    values = [round(float(x), 6) for x in list(vec)]

                    for value in values:
                        print(f"[{value}]")

                    print("")

        show_formula(fd.eigenvectors())
        print("")

    elif choice == "23":
        A = get_matrix("A")
        print("")
        print_result("Characteristic Polynomial", linear_algebra.characteristic_polynomial(A))
        show_formula(fd.characteristic_polynomial())
        print("")

    elif choice == "24":
        A = get_matrix("A")
        print("")
        print_result("Null Space", linear_algebra.null_space(A))
        show_formula(fd.null_space())
        print("")

    elif choice == "25":
        A = get_matrix("A")
        print("")
        print_result("Column Space", linear_algebra.column_space(A))
        show_formula(fd.column_space())
        print("")

    elif choice == "26":
        A = get_matrix("A")
        print("")
        print_result("Row Space", linear_algebra.row_space(A))
        show_formula(fd.row_space())
        print("")

    elif choice == "27":
        vectors = get_vectors()
        print("")
        print_result("Gram-Schmidt Result", linear_algebra.gram_schmidt(vectors))
        show_formula(fd.gram_schmidt())
        print("")

    elif choice == "28":
        vectors = get_vectors()
        print("")
        result = linear_algebra.linear_independence(vectors)

        if result is None:
            print("Could not determine linear independence.")
        elif result:
            print("The vectors are linearly independent.")
        else:
            print("The vectors are linearly dependent.")

        show_formula(fd.linear_independence())
        print("")

    elif choice == "29":
        A = get_matrix("A")
        print("")
        print_result("LU Decomposition", linear_algebra.lu_decomposition(A))
        show_formula(fd.lu_decomposition())
        print("")

    elif choice == "30":
        A = get_matrix("A")
        print("")
        print_result("QR Decomposition", linear_algebra.qr_decomposition(A))
        show_formula(fd.qr_decomposition())
        print("")

    elif choice == "31":
        A = get_matrix("A")
        print("")
        print_result("Matrix Norm", linear_algebra.matrix_norm(A))
        show_formula(fd.matrix_norm())
        print("")

    elif choice == "32":
        A = get_matrix("A")
        print("")
        print_result("Orthogonal", linear_algebra.is_orthogonal(A))
        show_formula(fd.orthogonal_matrix_check())
        print("")

    elif choice == "33":
        A = get_matrix("A")
        print("")
        print_result("Symmetric", linear_algebra.is_symmetric(A))
        show_formula(fd.symmetric_matrix_check())
        print("")

    elif choice == "34":
        A = get_matrix("A")
        print("")
        print_result("Skew-Symmetric", linear_algebra.is_skew_symmetric(A))
        show_formula(fd.skew_symmetric_matrix_check())
        print("")

    elif choice == "35":
        A = get_matrix("A")
        print("")
        print_result("Diagonalizable", linear_algebra.is_diagonalizable(A))
        show_formula(fd.diagonalization_check())
        print("")

    elif choice == "36":
        A, b = get_linear_system()
        print("")

        result = linear_algebra.system_of_equations(A, b)

        if result is None:
            print("System must be square and have one unique solution.")
        else:
            print_result("Solution", result)

        show_formula(fd.systems_of_equations())
        print("")

    elif choice == "0":
        exit()

    else:
        print("Invalid option.")