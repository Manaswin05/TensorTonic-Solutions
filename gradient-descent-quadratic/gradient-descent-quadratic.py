def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    df = lambda x : 2*a*x + b
    X = x0
    for i in range (steps) :
        X-= lr*df(X)

    return X