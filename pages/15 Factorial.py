import streamlit as st

st.markdown(
    """
    # Factorial
    
    Computes n! = 1*2*...*(n-1)*n.
    """
)

st.number_input('Input the number *n*', key='n', value=10)
st.button('Compute the factorial')

n = int(st.session_state.n)

f = 1
for i in range(1, n + 1):
    f *= i

st.write(f'{n}! = {f}')

trailing_zeros = 0
while f%10==0:
    trailing_zeros += 1

st.write()
st.write(f'It ends with {trailing_zeros} trailing zeros.')