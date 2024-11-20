import streamlit as st
from functions import gcd, phi


def print_logarithms(sto, n, a):
    # determine discrete logarithms
    logs = {1: 0}

    k = 1
    b = a
    while b != 1:
        logs[b] = k

        k = k+1
        b = (b*a) % n

    # was it a primitive root?
    if k != phi(n):
        sto.markdown(f'{a} is not a primitive root modulo {n}!')
        sto.markdown(f'Go to [Modular orders](https://aasu-number-theory.streamlit.app/Modular_orders) page...')
        return

    # create the output table
    lines = "| $b$ | $ind_{n,a}(b)$ \n| --- | --- |\n"
    for b in range(1, n):
        if gcd(b, n) == 1:
            lines = lines + f'| {b} | {logs[b]} |\n'
    sto.markdown(lines)


st.markdown(
    """
    # Discrete logarithms

    Suppose that $a$ is a primitive root modulo $n$,
    i.e., 
    $a$ is relatively prime to $n$ ($a\in Z^*_n$) 
    and 
    the smallest $k$ such that $a^k=1$ modulo $n$ is equal to $\phi(n)$.
    Then the powers $a$, $a^2$, ..., $a^{\phi(n)}=1$ modulo $n$
    necessarily range through all elements of $Z^*_n$ in some order.
    
    In such case, the discrete logarithm of $b$ with base $a$ modulo $n$ is defined
    as that value $k$ for which $b=a^k$ modulo $n$.
    This value is denoted by $\mathrm{ind}_{n,a}(b)$.

    Note that a primitive root exists only if $n$ is either 2 or 4
    or $p^e$ or $2p^e$ for some odd prime $p$ and positive integer $e$.
    You may use [Modular orders](https://aasu-number-theory.streamlit.app/Modular_orders) page
    to see the list of all primitive roots for such values of *n*
    (at the bottom of that page). 
    """)

st.number_input("Input the number $n$", key='n', value=17)
st.number_input("Input the primitive root $a$", key='a', value=3)

no = int(st.session_state.n)
ao = int(st.session_state.a)

print_logarithms(st, no, ao)

