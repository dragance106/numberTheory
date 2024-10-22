import streamlit as st


def extended_gcd(a, b, cols):
    if b == 0:
        # st.markdown(f'| {a} | 0 |   | {a} | 1 | 0 |')
        cols[0].write(a)
        cols[1].write('0')
        cols[2].write(' ')
        cols[3].write(a)
        cols[4].write('1')
        cols[5].write('0')

        return a, 1, 0
    else:
        # st.markdown(f'| {a} | {b} | {a//b} |  |  |  |')
        cols[0].write(a)
        cols[1].write(b)
        cols[2].write(a//b)
        cols[3].write(' ')
        cols[4].write(' ')
        cols[5].write(' ')

        (d, x1, y1) = extended_gcd(b, a % b, cols)

        x = y1
        y = x1 - (a//b)*y1

        # st.markdown(f'| {a} | {b} | {a//b} | {d} | {x} | {y} |')
        cols[0].write(a)
        cols[1].write(b)
        cols[2].write(a//b)
        cols[3].write(d)
        cols[4].write(x)
        cols[5].write(y)

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

colso = st.columns(6)

# st.markdown("""
# | *a* | *b* | int(*a/b*) | *d* | *x* | *y* |
# | --- | --- | ---        | --- | --- | --- |
# """)

do = extended_gcd(ao, bo, colso)

