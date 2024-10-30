"""
Auxiliary methods for number theoretic algorithms in this set.
These do not use streamlit.
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
