import streamlit as st


def print_extended_gcd(sto, a, b):
    do, xo, yo, lineso = extended_gcd(a, b)

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


def solve_mle(a, n, b):
    st.markdown(f'Extended Euclid\'s algorithm to find gcd({a}, {n}):')
    d, x0, y0 = print_extended_gcd(st, a, n)

    if b % d != 0:
        st.markdown(f'gcd({a}, {n})={d} does not divide {b}, so **there are no solutions**')
    else:
        x = (b // d) * x0
        st.markdown(f'Hence gcd({a}, {n}) = *d* = {d} = {a}&centerdot;({x0}) + {n}&centerdot;({y0}), ' +
                    f'so {a}&centerdot;({x0}) = {d} (mod {n}).')
        st.markdown(f'Since *b* = {b} = {b//d}&centerdot;*d*, we have that')
        st.markdown(f'{a}&centerdot;({b//d}&centerdot;({x0})) = {b} (mod {n})')
        st.markdown(f'so that x0 = {x} is one particular solution of the modular equation {a}&centerdot;*x* = {b} (mod {n}).')
        if d==1:
            st.markdown(f'Since *d* = 1, this is the unique solution.')
        else:
            st.markdown(f'Since *d* > 1, all solutions are of the form')
            st.markdown(f'*x* = {x} + (*n*/*d*)&centerdot;*k* = {x} + {n//d}&centerdot;*k* (mod {n})')
            st.markdown(f'for integers *k*=0,1,...,{d-1}.')


st.markdown(
    """
    # Modular linear equations

    Modular equation *ax* = *b* (mod *n*) for the known integer values *a*, *b* and *n*
    is obviously closely related to the linear Diophantine equation *ax* + *ny* = *b*,
    so it is solved in a similar fashion.
    First, 
    use the extended Euclid's algorithm to determine *d* = gcd(*a*, *n*)
    and the linear combination *d* = *ax*0 + *ny*0.
    Then if *d* does not divide *b*, there are no solutions,
    while if *d* divides *b*,
    one particular solution is given by *a*(*x*0&centerdot;*b*/*d*) = *b* (mod *n*),
    and all other solutions are of the form (*x*0&centerdot;*b*/*d*) + *k*&centerdot;*n*/*d*
    for *k*=1,...,*d*-1.
    
    This way we can also find the multiplicative inverse of *a* modulo *n*
    by solving the equation *ax* = 1 (mod *n*).
    """)

st.number_input("Input the number *a*", key='a', value=5)
st.number_input("Input the number *b*", key='b', value=1)
st.number_input("Input the number *n*", key='n', value=8)

ao = int(st.session_state.a)
bo = int(st.session_state.b)
no = int(st.session_state.n)

solve_mle(ao, no, bo)

