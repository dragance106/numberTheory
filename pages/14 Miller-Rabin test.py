import streamlit as st
import functions as fun
import numpy as np


def miller_rabin(n, s):
    # determine t and u
    t=0
    u=n-1
    while u%2 == 0:
        t=t+1
        u=u//2
    st.write(f'$$n-1={n-1}=2^{t}\cdot{u}$$')

    for _ in range(s):
        a = np.random.randint(low=2, high=n-1)
        if witness(a, n, t, u):
            return True

    st.write(f'$n$ is likely to be prime...')
    return False


def witness(a, n, t, u):
    st.write(f'Testing $a^{{n-1}}\mod n$ for $a={a}\dots$')
    x = fun.fast_exp(a, u, n)
    for _ in range(t):
        y = (x*x) % n
        if y==1 and not (x==1 or x==n-1):
            st.write(f'Found a non-trivial square root of 1 during the modular exponentiation $a^{{n-1}} \mod n$:')
            st.write(f'$x^2=1$ modulo for $x={x}$ modulo $n$.')
            st.write(f'Hence ${n}$ is composite.')
            return True
        x = y

    if x!=1:
        st.write(f'Fermat\'s theorem not satisfied:')
        st.write(f'${a}^{{{n-1}}}={x} \\neq 1$ modulo $n$.')
        st.write(f'Hence ${n}$ is composite.')
        return True

    st.write(f'  Test passed: ${a}^{{{n-1}}}=1$ modulo $n$.')
    return False


st.markdown(
    """
    # Miller-Rabin randomized primality testing

    This algorithm checks whether the given number *n* is prime
    by checking whether it satisfies Fermat's theorem
    for $s$ random values of $a$ between 2 and $n-2$.
    If $a^{n-1}$ is not 1 modulo $n$ for any such value of $a$,
    then $n$ is not prime. 
    
    Additionally, the algorithm checks the existence of
    non-trivial square roots of 1 modulo $n$ during modular exponentiation.
    Namely, it determines maximum $t$ and odd $u$ such that 
    
    $$n-1=2^t\cdot u$$
    
    and then it first computes 
    
    $$x_0 = a^u \mod n,$$
    
    after which it goes through the sequence of squarings:
    
    $$x_i = x_i^2 \mod n$$,
    
    so that $x_1=a^{2u},\dots,x_t=a^{2^tu}=a^{n-1} \mod n$.
    If it happens that one of these numbers is 1 modulo $n$,
    while the previous number is neither 1 nor $n-1$ modulo $n$,
    then the previous number is a non-trivial square root of 1 modulo $n$,
    and $n$ is not prime.
    """)

st.number_input("Input the number *n*", key='n', value=12345678901)
st.number_input("Input the number *s*", key='s', value=10)

no = int(st.session_state.n)
so = int(st.session_state.s)

miller_rabin(no, so)
