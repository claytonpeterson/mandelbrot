from numba import njit


@njit
def divergence_index(constant, iterations):
    """
    :param constant: A complex number (the position)
    :param iterations: The number of iterations to run at the given constant
    :return: n = the number of stable iterations
    """
    n = 0
    z = 0
    for i in range(iterations):
        if abs(z) > 4:
            break
        z = z**2 + constant
        n += 1
    return n
