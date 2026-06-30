from formula_display.core import make_formula

def dot_product():
    return make_formula(
        "a · b = Σ(aᵢbᵢ)",
        {
            "a": "first vector",
            "b": "second vector",
            "aᵢ": "component of the first vector",
            "bᵢ": "component of the second vector",
            "Σ": "sum of all component products"
        },
        topic="Dot Product",
        notes="Both vectors must have the same number of components."
    )


def magnitude():
    return make_formula(
        "‖v‖ = √(v₁² + v₂² + ... + vₙ²)",
        {
            "‖v‖": "magnitude of the vector",
            "v": "vector",
            "vᵢ": "component of the vector"
        },
        topic="Vector Magnitude"
    )


def unit_vector():
    return make_formula(
        "u = v / ‖v‖",
        {
            "u": "unit vector",
            "v": "original vector",
            "‖v‖": "magnitude of the original vector"
        },
        topic="Unit Vector",
        notes="The zero vector has no unit vector."
    )


def vector_addition():
    return make_formula(
        "a + b = (a₁ + b₁, a₂ + b₂, ..., aₙ + bₙ)",
        {
            "a": "first vector",
            "b": "second vector",
            "aᵢ": "component of the first vector",
            "bᵢ": "component of the second vector"
        },
        topic="Vector Addition",
        notes="Both vectors must have the same number of components."
    )


def vector_subtraction():
    return make_formula(
        "a - b = (a₁ - b₁, a₂ - b₂, ..., aₙ - bₙ)",
        {
            "a": "first vector",
            "b": "second vector",
            "aᵢ": "component of the first vector",
            "bᵢ": "component of the second vector"
        },
        topic="Vector Subtraction",
        notes="Both vectors must have the same number of components."
    )


def scalar_multiplication():
    return make_formula(
        "c · v = (cv₁, cv₂, ..., cvₙ)",
        {
            "c": "scalar",
            "v": "vector",
            "vᵢ": "component of the vector"
        },
        topic="Scalar Multiplication"
    )


def cross_product():
    return make_formula(
        "a × b = (a₂b₃ - a₃b₂, a₃b₁ - a₁b₃, a₁b₂ - a₂b₁)",
        {
            "a": "first 3D vector",
            "b": "second 3D vector",
            "a₁, a₂, a₃": "components of the first vector",
            "b₁, b₂, b₃": "components of the second vector"
        },
        topic="Cross Product",
        notes="Cross product only works for 3D vectors in this project."
    )


def matrix_addition():
    return make_formula(
        "A + B = [aᵢⱼ + bᵢⱼ]",
        {
            "A": "first matrix",
            "B": "second matrix",
            "aᵢⱼ": "entry in matrix A",
            "bᵢⱼ": "entry in matrix B"
        },
        topic="Matrix Addition",
        notes="Both matrices must have the same dimensions."
    )


def matrix_subtraction():
    return make_formula(
        "A - B = [aᵢⱼ - bᵢⱼ]",
        {
            "A": "first matrix",
            "B": "second matrix",
            "aᵢⱼ": "entry in matrix A",
            "bᵢⱼ": "entry in matrix B"
        },
        topic="Matrix Subtraction",
        notes="Both matrices must have the same dimensions."
    )


def matrix_multiplication():
    return make_formula(
        "(AB)ᵢⱼ = Σ(aᵢₖbₖⱼ)",
        {
            "A": "first matrix",
            "B": "second matrix",
            "(AB)ᵢⱼ": "entry in the product matrix",
            "aᵢₖ": "entry from row i of matrix A",
            "bₖⱼ": "entry from column j of matrix B",
            "Σ": "sum over matching row-column products"
        },
        topic="Matrix Multiplication",
        notes="The number of columns in A must equal the number of rows in B."
    )


def transpose():
    return make_formula(
        "(Aᵀ)ᵢⱼ = Aⱼᵢ",
        {
            "A": "original matrix",
            "Aᵀ": "transpose of matrix A",
            "i, j": "row and column positions"
        },
        topic="Matrix Transpose",
        notes="Rows become columns and columns become rows."
    )


def determinant_2x2():
    return make_formula(
        "det(A) = ad - bc",
        {
            "A": "2x2 matrix [[a, b], [c, d]]",
            "a, b, c, d": "entries of the matrix"
        },
        topic="2x2 Determinant"
    )


def trace():
    return make_formula(
        "tr(A) = a₁₁ + a₂₂ + ... + aₙₙ",
        {
            "tr(A)": "trace of matrix A",
            "aᵢᵢ": "diagonal entry of matrix A"
        },
        topic="Matrix Trace",
        notes="Trace only works for square matrices."
    )