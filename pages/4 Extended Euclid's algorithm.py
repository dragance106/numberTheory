import streamlit as st


def extended_gcd(a, b):
    if b == 0:
        st.write(f'gcd({a}, 0) = {a}')
        return a, 1, 0
    else:
        (d, x1, y1) = gcd(b, a%b)
        x = y1
        y = x1 - (a//b)*y1
        st.write(f'gcd({a}, {b}) = ' + '&nbsp;' * 20 + f'// note: {a} = {a // b} * {b} + {a % b}')
        return d, x, y


st.markdown(
    """
    # Extended Euclid's algorithm

    This algorithm extends the usual Euclid's algorithm so that,
    besides the value of the greatest common divisor *d*=gcd(*a*, *b*),
    it also returns the values of *x* and *y* such that *d* = *ax* + *by*.
    
    The gcd is computed in the forward phase, 
    based on the relation gcd(*a*, *b*) = gcd(*b*, *a* mod *b*),
    as in the usual Euclid's algorithm.
    
    However, 
    the values of *x* and *y* are computed in the backward phase.
    The algorithm starts with 
    
    *d* = 1&centerdot;*d* + 0&centerdot;0
    
    which is valid it reaches the point gcd(*d*, 0) = *d*,
    and then at each step it moves backwards from
    
    *d* = *bx*' + (*a* mod *b*)*y*'
        
    to
    
    *d* = *ay*' + *b*(*x*'-*y*'int(*a*/*b*))
    """)

st.number_input("Input the number *a*", key='a', value=30)
st.number_input("Input the number *b*", key='b', value=24)

ao = int(st.session_state.a)
bo = int(st.session_state.b)

d = extended_gcd(ao, bo)

