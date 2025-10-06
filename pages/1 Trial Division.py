import streamlit as st
import math


def trial_division(n):
    up_to = int(math.floor(math.sqrt(n)))
    for p in range(2, up_to+1):
        if n % p == 0:      # n is divisible by p without a remainder
            st.write(f'{n} is divisible by {p}')
            return False
        else:
            st.write(f'{n} is not divisible by {p}')

    return True


st.markdown(
    """
    # Trial division
    
    For the positive integer *n*, the trial division method determines
    whether it is prime by dividing *n* with all integers not exceeding its square root.
    """)

st.number_input("Input the number *n*", key='n', value=37)
n = int(st.session_state.n)
st.button("Do it", on_click=trial_division, args=[n])

if trial_division(n):
    st.write('* PRIME!')
else:
    st.write('* NOT PRIME!')


