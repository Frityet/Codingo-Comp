"""
This function takes in an integer, x, and returns x / 2 if
x is even and 3x + 1 if x is odd.

Arguments:
    num (Int): An integer
Returns:
    x / 2 if x is even and 3x + 1 if x is odd.
Examples:
    10 => 5
    3 => 10
"""
def iseven(num):
    if num % 2 == 0:
        return True
    return False

def number_transform(num):
    if iseven(num):
        return num * 0.5
    else:
        return num * 3 + 1
    pass
