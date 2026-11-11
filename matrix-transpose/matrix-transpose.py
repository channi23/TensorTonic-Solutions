import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    m = len(A)
    n = len(A[0])
    newA = np.zeros((n,m),dtype=int)
    for i in range(m):
        for j in range(n):
            newA[j][i] = A[i][j]
    return newA
            
