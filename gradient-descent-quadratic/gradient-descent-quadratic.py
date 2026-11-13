def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here

    val = x0

    for i in range(steps):
        x = val
        eq = 2*a*x+b # the derived eq
        new_EQ = x - lr*eq
        val = new_EQ
    return val