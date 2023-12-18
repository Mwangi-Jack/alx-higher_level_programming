#!/usr/bin/python3

def safe_print_division(a, b):
    """Safe print division.
    Args:
        a (int): value to divide with
        b (int): value to divide with
    Returns:
        returns the quotient.
    """

    try:
        quotient = a / b
    except (ZeroDivisionError, TypeError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
