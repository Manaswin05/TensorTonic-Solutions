import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    x = np.array(X,dtype=float)
    mu = np.mean(x,axis=axis,keepdims=True)
    sigma = np.std(x,axis=axis,keepdims=True)
    return (x-mu)/np.maximum(sigma,eps)