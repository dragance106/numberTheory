import streamlit as st

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


st.markdown(
    """
    # Euclid's algorithm
    
    Finds the greatest common divisor of two numbers $a$ and $b$
    by recursively using the relation $\\gcd(a,b) = \\gcd(b, a \\mathrm{mod } b)$.
    Recursion stops with $\\gcd(a, 0) = a$.
    """)
