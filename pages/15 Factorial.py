import streamlit as st


def factorial(n):
  f=1
  for i in range(1, n+1):
    f*=i

  g=f
  trailing_zeros=0
  while g%10==0:
    trailing_zeros+=1
    g//=10

  return f, trailing_zeros


st.markdown(
    """
    # Factorial and the number of trailing zeros
    
    Computes n! = 1*2*...*n and the number of zeros that it ends with.
    """)

st.number_input('Input the number *n*', key='n', value=100)
st.button('Compute')

n = int(st.session_state.n)
f, trailing_zeros = factorial(n)

st.write(f'{n}! = {f}')
st.write(f'It ends with {trailing_zeros} trailing zeros.')
