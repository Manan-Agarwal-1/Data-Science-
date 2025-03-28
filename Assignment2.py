import numpy as np
from scipy.linalg import inv, det, eig
from numpy.linalg import matrix_rank

# Define two matrices
A = np.array([[2, 3], [5, 7]])
B = np.array([[1, 4], [2, 6]])

# Addition
addition = A + B
print("Addition:\n", addition)

# Subtraction
subtraction = A - B
print("Subtraction:\n", subtraction)

# Multiplication (Matrix Multiplication)
multiplication = np.dot(A, B)
print("Matrix Multiplication:\n", multiplication)

# Element-wise Multiplication
element_wise_multiplication = A * B
print("Element-wise Multiplication:\n", element_wise_multiplication)

# Determinant of A
determinant_A = det(A)
print("Determinant of A:", determinant_A)

# Inverse of A (only if determinant is nonzero)
if determinant_A != 0:
    inverse_A = inv(A)
    print("Inverse of A:\n", inverse_A)
else:
    print("Matrix A is singular and does not have an inverse.")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Check Orthogonality of Eigenvectors
orthogonality_check = np.dot(eigenvectors.T, eigenvectors)
print("Orthogonality Check (Eigenvectors^T * Eigenvectors):\n", orthogonality_check)

# Calculate Span and Basis of a Vector Space
def compute_basis(vectors):
    U, S, Vt = np.linalg.svd(vectors, full_matrices=False)
    rank = matrix_rank(vectors)
    basis = U[:, :rank]
    return basis

vectors = np.array([[2, 3], [5, 7]])
basis = compute_basis(vectors)

print("Basis of the vector space:\n", basis)
