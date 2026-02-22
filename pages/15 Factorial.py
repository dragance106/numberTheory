import streamlit as st

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i

    trailing_zeros = 0
    g = f
    while g % 10 == 0:
        trailing_zeros = trailing_zeros + 1
        g = g//10

    return f, trailing_zeros

st.markdown(
    """
    # Factorial and trailing zeros
    
    Computes factorial n! = 1*2*...*(n-1)*n, and
    then finds the number of trailing zeros.
    """
)

st.number_input('Input the number *n*', key='n', value=10)
st.button('Compute factorial')

n=int(st.session_state.n)
f, t = factorial(n)
st.write(f'The factorial of {n} is {f}.')
st.write(f'The factorial of {n} has {trailing_zeros} trailing zeros.')
