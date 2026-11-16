import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.asarray(A,dtype=int)
    dimensions = np.shape(A)
    T = np.empty((dimensions[1],dimensions[0]),dtype=A.dtype)
    for i in range(dimensions[1]):
        for j in range(dimensions[0]):
            T[i][j] = A[j][i]

    return T