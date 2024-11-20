import streamlit as st
from functions import gcd, phi


def print_orders(sto, n):
    fi = phi(n)
    p_roots = []

    # create two heading rows
    lines = "| Element | "
    for k in range(1, fi+1):
        lines = lines + f'{k} | '
    lines = lines + ' Order |\n| '
    for k in range(1, fi+2):
        lines = lines + "--- | "

    for a in range(1, n):
        if gcd(a, n) == 1:
            k = 1
            b = a
            lines = lines + f'\n| {a} | {b} | '

            # consecutive powers until 1 is reached again
            while b != 1:
                k = k+1
                b = b*a
                lines = lines + f'\n| {b} | '

            # empty cells from the order to phi(n)
            lines = lines + "--- | "*(fi-k)

            # report the order
            lines = lines + f' {k} |'

            # after the table there will be
            # the list of all primitive roots seen along
            if k == fi:
                p_roots.append(a)

    lines = lines + f'\nPrimitive roots: {p_roots}'
    sto.markdown(lines)


st.markdown(
    """
    # Orders of elements in $Z_n^*$

    If $a$ is relatively prime to $n$,
    the *order* of $a$ mod $n$ is the smallest $k$ 
    such that $a^k=1$ mod $n$.
    
    If the order of $a$ mod $n$ is equal to $\phi(n)$,
    then $a$ is a *primitive root* mod $n$,
    since its powers will represent
    all elements of $Z_n^*$ in some order.
    """)

st.number_input("Input the number $n$", key='n', value=7)
no = int(st.session_state.n)

print_orders(st, no)

