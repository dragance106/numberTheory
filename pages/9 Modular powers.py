import streamlit as st
from functions import gcd


def power_list(a, n):
    prd = 1
    powers = []

    for k in range(n):
        st.markdown(f'${a}^{{{k}}}$ mod {n} = {prd}')

        if prd in powers:
            l = powers.index(prd)
            st.markdown(f'The first repetition is ${a}^{{{k}}}={a}^{{{l}}}$ mod {n}')

            if gcd(a, n) == 1:
                st.markdown(f"""Since {a} and {n} are relatively prime,
                                the order of {a} mod {n} is equal to {k}.""")
                if k == n-1:
                    st.markdown(f'Hence {a} is a primitive root mod {n}.')

            break
        else:
            powers.append(prd)

        prd = (prd*a) % n




st.markdown(
    """
    # Powers of $a$ mod $n$

    For every $a$ and $n$,
    the list of powers
    $a^0=1$, $a^1$, $a^2$, $a^3$, ... mod $n$
    will eventually start to repeat itself,
    since there are only $n$ possible different values mod $n$.
    
    If $a$ is relatively prime to $n$,
    the first such repetition will necessarily be $a^k=a^0=1$.
    Smallest such $k$ is then called the *order* of $a$ mod $n$.
    In such case we also have *Euler's theorem* which states
    that necessarily $a^{\phi(n)}=1$ mod $n$,
    implying that the order of $a$ will be a divisor of $\phi(n)$.
    """)

st.number_input("Input the number $a$", key='a', value=3)
st.number_input("Input the number $n$", key='n', value=7)
ao = int(st.session_state.a)
no = int(st.session_state.n)
power_list(ao, no)

