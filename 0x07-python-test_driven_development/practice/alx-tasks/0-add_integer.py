#!/usr/bin/python

def add_integer(a, b=98):
    """
    Returns the sum of a and b

    Arguments:
		a: first integer
		b: second integer (Default value of 98)

	Raises:
		TypeError: when Operands given are not valid integers

	Returns:
		int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    try:
        int(a)
        int(b)
    except Exception as e:
        raise e

    return int(a) + int(b)


