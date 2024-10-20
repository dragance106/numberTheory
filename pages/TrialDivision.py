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
            return False, p

    return True


st.markdown("Trial division")
st.sidebar.markdown("Trial division")


if __name__=="__main__":
    print(trial_division(101))
    print(trial_division(121))
