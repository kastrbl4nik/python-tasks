import numpy as np

# Sample arrays
vec = np.array([1, 2, 3])
mat2x3 = np.array([[1, 2], [3, 4], [5, 6]])
mat3x2 = np.transpose(mat2x3)
tens = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Multiplication of 1d arrays
print(np.dot(vec, vec + 1))
print(np.dot(vec, vec + 2))
print(np.dot(vec, vec + 3))

# Multiplication of 2d arrays
print(np.matmul(mat3x2, mat2x3))
print(np.matmul(mat3x2, mat2x3 + 1))
print(np.matmul(mat2x3, mat3x2))

# Multiplication of 3d arrays
print(np.tensordot(tens, tens))
print(np.tensordot(tens, tens + 1))
print(np.tensordot(tens, tens + 2))