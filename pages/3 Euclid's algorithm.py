import streamlit as st


def gcd(a, b):
    if b == 0:
        st.write(f'gcd({a}, 0) = {a}')
        return a
    else:
        st.write(f'gcd({a}, {b}) = &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \# {a} = {a//b} * {b} + {a % b}')
        return gcd(b, a % b)


st.markdown(
    """
    # Euclid's algorithm
    
    Finds the greatest common divisor of two numbers *a* and *b*
    by recursively using the relation gcd(*a*, *b*) = gcd(*b*, *a* mod *b*).
    Recursion stops with gcd(*a*, 0) = *a*.
    """)

st.number_input("Input the number *a*", key='a', value=30)
st.number_input("Input the number *b*", key='b', value=24)

ao = int(st.session_state.a)
bo = int(st.session_state.b)

d = gcd(ao, bo)

