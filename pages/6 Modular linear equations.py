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


def solve_mle(a, b, c):
    st.markdown(f'Extended Euclid\'s algorithm to find gcd({a}, {b}):')
    d, x0, y0 = print_extended_gcd(st, a, b)

    if c % d != 0:
        st.markdown(f'gcd({a}, {b})={d} does not divide {c}, so **there are no solutions**')
    else:
        x = (c // d) * x0
        y = (c // d) * y0
        st.markdown(f'Hence gcd({a}, {b}) = *d* = {d} = {a}&centerdot;({x0}) + {b}&centerdot;({y0}).')
        st.markdown(f'Since *c* = {c} = {c // d}&centerdot;({d}) for c/d={c // d} we have that')
        st.markdown(f'{c} = {a}&centerdot;({c // d}&centerdot;({x0})) + {b}&centerdot;({c // d}&centerdot;({y0}))' +
                    f' = {a}&centerdot;({x}) + {b}&centerdot;({y}) is one particular solution.')
        st.markdown(f'All solutions are of the form')
        st.markdown(f'*x* = {x} + *bk*/*d* = {x} + {b // d}&centerdot;*k*')
        st.markdown(f'*y* = {y} - *ak*/*d* = {y} - {a // d}&centerdot;*k*')
        st.markdown(f'for arbitrary integer *k*.')


st.markdown(
    """
    # Modular linear equations

    Modular equation *ax* = *b* (mod *n*) for the known integer values *a*, *b* and *n*
    is obviously closely related to the linear Diophantine equation *ax* + *ny* = *b*,
    so it is solved in a similar fashion.
    First, 
    use the extended Euclid's algorithm to determine *d* = gcd(*a*, *n)
    and the linear combination *d* = *ax*0 + *by*0.
    Then if *d* does not divide *b*, there are no solutions,
    while if *d* divides *b*,
    one particular solution is given by *a*(*x*0&centerdot;*b*/*d*) = *b* (mod *n*),
    and all other solutions are of the form *x*0&centerdot;*b*/*d* + *k*&centerdot;*n*/*d*
    for *k*=1,...,*d*-1.
    """)

st.number_input("Input the number *a*", key='a', value=5)
st.number_input("Input the number *b*", key='b', value=1)
st.number_input("Input the number *n*", key='n', value=8)

ao = int(st.session_state.a)
bo = int(st.session_state.b)
no = int(st.session_state.n)

solve_mle(ao, n0, bo)

