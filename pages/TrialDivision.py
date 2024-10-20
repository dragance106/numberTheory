import streamlit as st
import math


def trial_division(n):
    """
    Given a positive integer n, the method determines whether it is prime
    using trial division of n by all integers not exceeding its square root.

    :param n: The integer to be tested whether it is prime.
    :return:  True if n is prime, and False if n is not prime.
              In such case, the method also returns the smallest divisor found.
    """

    up_to = int(math.floor(math.sqrt(n)))
    for p in range(2, up_to+1):
        if n % p == 0:     # n is divisible by p without a remainder
            st.write(f'{n} is divisible by {p}!')
            return False, p
        else:
            st.write(f'{n} is not divisibly by {p}')

    return True


st.sidebar.markdown("Trial division")
st.write("# Trial division")
st.markdown(
    """
    For the positive integer *n*, the trial division method determines
    whether it is prime by dividing *n* with all integers not exceeding its square root.
    """)

st.text_input("Input the number *n*", key='n')
n = int(st.session_state.n)
if trial_division(n):
    st.write('* PRIME!')
else:
    st.write('* NOT PRIME!')


if __name__=="__main__":
    print(trial_division(101))
    print(trial_division(121))
