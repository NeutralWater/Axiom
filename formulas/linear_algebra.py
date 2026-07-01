import math
from sympy import Matrix

def dot_product(v1, v2):
    if len(v1) != len(v2):
        return None

    return sum(v1[i] * v2[i] for i in range(len(v1)))


def magnitude(v):
    return math.sqrt(sum(x ** 2 for x in v))


def unit_vector(v):
    mag = magnitude(v)

    if mag == 0:
        return None

    return [x / mag for x in v]


def vector_addition(v1, v2):
    if len(v1) != len(v2):
        return None

    return [v1[i] + v2[i] for i in range(len(v1))]


def vector_subtraction(v1, v2):
    if len(v1) != len(v2):
        return None

    return [v1[i] - v2[i] for i in range(len(v1))]


def scalar_multiplication(c, v):
    return [c * x for x in v]


def cross_product(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        return None

    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]


def same_dimensions(A, B):
    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if len(A[i]) != len(B[i]):
            return False

    return True


def matrix_addition(A, B):
    if not same_dimensions(A, B):
        return None

    return [
        [A[i][j] + B[i][j] for j in range(len(A[i]))]
        for i in range(len(A))
    ]


def matrix_subtraction(A, B):
    if not same_dimensions(A, B):
        return None

    return [
        [A[i][j] - B[i][j] for j in range(len(A[i]))]
        for i in range(len(A))
    ]


def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        return None

    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def transpose(A):
    return [
        [A[i][j] for i in range(len(A))]
        for j in range(len(A[0]))
    ]


def determinant_2x2(A):
    if len(A) != 2 or len(A[0]) != 2 or len(A[1]) != 2:
        return None

    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def trace(A):
    if len(A) == 0:
        return None

    for row in A:
        if len(row) != len(A):
            return None

    return sum(A[i][i] for i in range(len(A)))

def matrix_inverse(A):
    try:
        return Matrix(A).inv()
    except:
        return None


def matrix_rank(A):
    try:
        return Matrix(A).rank()
    except:
        return None


def rref(A):
    try:
        return Matrix(A).rref()[0]
    except:
        return None


def determinant(A):
    try:
        M = Matrix(A)

        if M.rows != M.cols:
            return None

        return M.det()
    except:
        return None


def angle_between_vectors(u, v):
    if len(u) != len(v):
        return None

    dot = sum(a * b for a, b in zip(u, v))
    mag_u = math.sqrt(sum(a * a for a in u))
    mag_v = math.sqrt(sum(b * b for b in v))

    if mag_u == 0 or mag_v == 0:
        return None

    cos_theta = dot / (mag_u * mag_v)
    cos_theta = max(-1, min(1, cos_theta))

    return math.degrees(math.acos(cos_theta))


def vector_projection(u, v):
    if len(u) != len(v):
        return None

    denominator = sum(x * x for x in v)

    if denominator == 0:
        return None

    scalar = sum(a * b for a, b in zip(u, v)) / denominator
    return [scalar * x for x in v]


def distance_between_vectors(u, v):
    if len(u) != len(v):
        return None

    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

def eigenvalues(A):
    try:
        return Matrix(A).eigenvals()
    except:
        return None


def eigenvectors(A):
    try:
        result = []

        for value, mult, vectors in Matrix(A).eigenvects():
            result.append({
                "eigenvalue": value,
                "multiplicity": mult,
                "vectors": vectors
            })

        return result

    except:
        return None


def characteristic_polynomial(A):
    try:
        return Matrix(A).charpoly().as_expr()
    except:
        return None


def null_space(A):
    return Matrix(A).nullspace()


def column_space(A):
    return Matrix(A).columnspace()


def row_space(A):
    return Matrix(A).rowspace()


def gram_schmidt(vectors):
    try:
        matrix_vectors = [Matrix(v) for v in vectors]
        return Matrix.orthogonalize(*matrix_vectors, normalize=False)
    except:
        return None


def linear_independence(vectors):
    try:
        matrix = Matrix(vectors).T
        return matrix.rank() == len(vectors)
    except:
        return None


def lu_decomposition(A):
    try:
        return Matrix(A).LUdecomposition()
    except:
        return None


def qr_decomposition(A):
    try:
        return Matrix(A).QRdecomposition()
    except:
        return None


def matrix_norm(A):
    try:
        return Matrix(A).norm()
    except:
        return None


def is_orthogonal(A):
    try:
        M = Matrix(A)
        return M.T * M == Matrix.eye(M.cols)
    except:
        return None


def is_symmetric(A):
    try:
        M = Matrix(A)
        return M == M.T
    except:
        return None


def is_skew_symmetric(A):
    try:
        M = Matrix(A)
        return M == -M.T
    except:
        return None


def is_diagonalizable(A):
    try:
        return Matrix(A).is_diagonalizable()
    except:
        return None