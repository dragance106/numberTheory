import streamlit as st


def fast_exp(a, b, n):
    if b == 1:
        return a % n, '| 1 |', '| --- |', f'| {a % n} |'
    elif b % 2 == 1:  # b is odd
        r, line1, line2, line3 = fast_exp(a, b - 1, n)
        line1 = f'| {b} ' + line1
        line2 = '| --- ' + line2
        line3 = f'| {(a * r) % n} ' + line3
        return (a * r) % n, line1, line2, line3
    else:  # b is even
        r, line1, line2, line3 = fast_exp(a, b // 2, n)
        line1 = f'| {b} ' + line1
        line2 = '| --- ' + line2
        line3 = f'| {(r * r) % n} ' + line3
        return (r * r) % n, line1, line2, line3


st.markdown(
    """
    # Miller-Rabin randomized primality testing

    This algorithm checks whether the given number *n* is prime
    by checking whether it satisfies Fermat's theorem
    for several random values of $a$ between 2 and $n-2$.
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

st.number_input("Input the number *a*", key='a', value=2)
st.number_input("Input the number *b*", key='b', value=1001)
st.number_input("Input the number *n*", key='n', value=100)

ao = int(st.session_state.a)
bo = int(st.session_state.b)
no = int(st.session_state.n)

ro, line1, line2, line3 = fast_exp(ao, bo, no)
table = '| exp ' + line1 + '\n| --- ' + line2 + f'\n| {ao}^exp mod {no} ' + line3 + '\n'
st.markdown(table)
