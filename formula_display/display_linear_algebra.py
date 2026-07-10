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

def matrix_inverse():
    return make_formula(
        "A⁻¹",
        {
            "A": "Square matrix",
            "A⁻¹": "Inverse of A"
        },
        topic="Matrix Inverse"
    )


def matrix_rank():
    return make_formula(
        "rank(A)",
        {
            "A": "Matrix",
            "rank(A)": "Dimension of the column space"
        },
        topic="Matrix Rank"
    )


def rref():
    return make_formula(
        "RREF(A)",
        {
            "A": "Matrix",
            "RREF(A)": "Reduced row echelon form of A"
        },
        topic="Reduced Row Echelon Form"
    )


def determinant():
    return make_formula(
        "|A|",
        {
            "A": "Square matrix",
            "|A|": "Determinant of A"
        },
        topic="Matrix Determinant"
    )


def angle_between_vectors():
    return make_formula(
        "θ = arccos((u · v)/(|u||v|))",
        {
            "u": "First vector",
            "v": "Second vector",
            "θ": "Angle between vectors"
        },
        units="Degrees",
        topic="Angle Between Vectors"
    )


def vector_projection():
    return make_formula(
        "projᵥ(u) = ((u · v)/(v · v))v",
        {
            "u": "Vector being projected",
            "v": "Projection vector"
        },
        topic="Vector Projection"
    )


def distance_between_vectors():
    return make_formula(
        "d = ||u - v||",
        {
            "u": "First vector",
            "v": "Second vector",
            "d": "Distance between vectors"
        },
        topic="Distance Between Vectors"
    )

def eigenvalues():
    return make_formula(
        "det(A - λI) = 0",
        {
            "A": "Square matrix",
            "λ": "Eigenvalue",
            "I": "Identity matrix"
        },
        topic="Eigenvalues"
    )


def eigenvectors():
    return make_formula(
        "Av = λv",
        {
            "A": "Square matrix",
            "v": "Eigenvector",
            "λ": "Eigenvalue"
        },
        topic="Eigenvectors"
    )


def characteristic_polynomial():
    return make_formula(
        "p(λ) = det(A - λI)",
        {
            "A": "Square matrix",
            "λ": "Eigenvalue variable",
            "p(λ)": "Characteristic polynomial"
        },
        topic="Characteristic Polynomial"
    )


def null_space():
    return make_formula(
        "Ax = 0",
        {
            "A": "Matrix",
            "x": "Vector in the null space"
        },
        topic="Null Space"
    )


def column_space():
    return make_formula(
        "Col(A)",
        {
            "A": "Matrix",
            "Col(A)": "Span of all column vectors"
        },
        topic="Column Space"
    )


def row_space():
    return make_formula(
        "Row(A)",
        {
            "A": "Matrix",
            "Row(A)": "Span of all row vectors"
        },
        topic="Row Space"
    )


def gram_schmidt():
    return make_formula(
        "uᵢ = vᵢ - Σ proj(uⱼ)",
        {
            "vᵢ": "Original vector",
            "uᵢ": "Orthogonal vector"
        },
        topic="Gram-Schmidt Orthogonalization"
    )


def linear_independence():
    return make_formula(
        "rank(A) = number of vectors",
        {
            "A": "Matrix formed by vectors",
            "rank(A)": "Rank of the matrix"
        },
        topic="Linear Independence Test"
    )


def lu_decomposition():
    return make_formula(
        "A = LU",
        {
            "A": "Original matrix",
            "L": "Lower triangular matrix",
            "U": "Upper triangular matrix"
        },
        topic="LU Decomposition"
    )


def qr_decomposition():
    return make_formula(
        "A = QR",
        {
            "A": "Original matrix",
            "Q": "Orthogonal matrix",
            "R": "Upper triangular matrix"
        },
        topic="QR Decomposition"
    )


def matrix_norm():
    return make_formula(
        "||A||",
        {
            "A": "Matrix",
            "||A||": "Norm (size) of the matrix"
        },
        topic="Matrix Norm"
    )


def is_orthogonal():
    return make_formula(
        "AᵀA = I",
        {
            "A": "Matrix",
            "Aᵀ": "Transpose of A",
            "I": "Identity matrix"
        },
        topic="Orthogonal Matrix Check"
    )


def is_symmetric():
    return make_formula(
        "A = Aᵀ",
        {
            "A": "Matrix",
            "Aᵀ": "Transpose of A"
        },
        topic="Symmetric Matrix Check"
    )


def is_skew_symmetric():
    return make_formula(
        "Aᵀ = -A",
        {
            "A": "Matrix",
            "Aᵀ": "Transpose of A"
        },
        topic="Skew-Symmetric Matrix Check"
    )


def is_diagonalizable():
    return make_formula(
        "A = PDP⁻¹",
        {
            "A": "Original matrix",
            "P": "Eigenvector matrix",
            "D": "Diagonal matrix"
        },
        topic="Diagonalization Check"
    )

def system_of_equations():
    return make_formula(
        "Ax = b",
        {
            "A": "coefficient matrix",
            "x": "variable vector",
            "b": "constant vector"
        },
        topic="System of Equations",
        notes="Axiom solves square linear systems with one unique solution."
    )
