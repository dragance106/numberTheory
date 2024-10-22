import streamlit as st


def print_extended_gcd(sto, a, b):
    do, xo, yo, lineso = extended_gcd(ao, bo)

    lineso = '| *a* | *b* | int(*a/b*) | *d* | *x* | *y* |  \n' \
             + '| --- | --- | ---        | --- | --- | --- |  \n' \
             + lineso

    sto.markdown(lineso)
    return do, xo, yo


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0, f'| {a} | 0 | &xrarr; | {a} | 1 | 0 |  \n'
    else:
        d, x1, y1, lines = extended_gcd(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        lines = f'| {a} | {b} | {a // b} |  |  |  |  \n' \
                + lines \
                + f'| {a} | {b} | {a // b} | {d} | {x} | {y} |  \n'

        return d, x, y, lines


def solve_lde(a, b, c):
    st.markdown(f'Extended Euclid\'s algorithm to find gcd({a}, {b}):')
    d, x0, y0 = print_extended_gcd(st, a, b)

    if c % d != 0:
        st.markdown(f'gcd({a},{b})={d} does not divide {c}, so **there are no solutions**')


st.markdown(
    """
    # Linear Diophantine equations
    
    Equation *ax* + *by* = *c* with the known *integer* values *a*, *b* and *c*,
    for which the unknown solutions *x* and *y* should also be integers,
    is called the linear Diophantine equation. 
    It is solved through a simple observation:
    *d*=gcd(*a*, *b*) divides any linear combination *ax*+*by*.
    Hence if *d* does not divide *c*, there are no solutions.
    On the other hand, 
    if *d*|*c*, there will be infinitely many solutions,
    which are derived from the basic linear combination *ax*0+*by*0=*d*
    returned by the extended Euclid's algorithm.
    """)

st.number_input("Input the number *a*", key='a', value=30)
st.number_input("Input the number *b*", key='b', value=24)
st.number_input("Input the number *c*", key='c', value=3)

ao = int(st.session_state.a)
bo = int(st.session_state.b)
co = int(st.session_state.c)

solve_lde(ao, bo, co)
