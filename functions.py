"""
Auxiliary methods for number theoretic algorithms in this set.
These do not use streamlit.
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y


def multiplicative_inverse(a, n):
    d, x0, y0 = extended_gcd(a, n)

    if d != 1:
        return 0
    else:
        return x0
