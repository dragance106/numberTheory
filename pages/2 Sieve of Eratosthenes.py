import streamlit as st
import math


def sieve(n):
    the_list = list(range(2, n+1))      # the list of all numbers from 2 to n
    first_unmarked = 0                  # the index of the first unmarked entry

    st.write("Initial list: " + str(the_list))

    while the_list[first_unmarked] <= int(math.floor(math.sqrt(n))):
        # mark all multiples of the first unmarked entry
        for i in range(first_unmarked+1, len(the_list)):
            if the_list[i] % the_list[first_unmarked] == 0:
                the_list[i] = 0

        st.write("Next prime is " + str(the_list[first_unmarked]))
        st.write("Remaining list: " + str(the_list))

        # find the next unmarked entry
        j = first_unmarked+1
        while the_list[j] == 0:     # this entry is already marked
            j = j+1
        first_unmarked = j

    st.write("Process completed.")
    st.write()

    return [p for p in the_list if p>0]


st.markdown(
    """
    # Sieve of Eratosthenes
    
    Starting with the initial unmarked list of numbers from 2 to *n*,
    the sieve of Eratosthenes iteratively 
    proclaims the smallest unmarked number *k* in the list as a *prime*,
    marks all the multiples of *k* in the list,
    and then repeats the process with the next unmarked number.
    The process ends when the smallest unmarked entry exceeds the square root of *n*,
    as then all the remaining unmarked numbers are also prime. 
    """)

st.number_input("Input the number *n*", key='n', value=10)
st.button("Just do it")

n = int(st.session_state.n)
primes = sieve(n)
st.write("Primes up to *n* are: " + str(primes))
