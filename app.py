import os

def calculate(a, b):
    """
    Compute the quotient of `a` and `b`, returning 0 when either operand is `None`.
    
    Parameters:
        a (number | None): Numerator; may be None, in which case the function returns 0.
        b (number | None): Denominator; may be None, in which case the function returns 0.
    
    Returns:
        number: The result of `a / b` when both operands are not `None`, or `0` if either is `None`.
    
    Raises:
        ZeroDivisionError: If `b` is `0`.
    """
    if a == None:
        return 0
    if b == None:
        return 0
    return a/b

password = "123456"
print(calculate(10, 0))
