import streamlit as st


def power_list(a, n):
    powers = []


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
    """)

st.number_input("Input the number $a$", key='a', value=3)
st.number_input("Input the number $n$", key='n', value=7)
ao = int(st.session_state.a)
no = int(st.session_state.n)
power_list(ao, no)

