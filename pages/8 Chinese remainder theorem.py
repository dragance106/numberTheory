import streamlit as st


st.markdown(
    """
    # Chinese remainder theorem
    
    This theorem provides a way to solve the system of modular equations
    
    *x* = *a*1 (mod *n*1)
    
    *x* = *a*2 (mod *n*2)

    ...

    *x* = *a*k (mod *n*k)

    provided that the moduli *n*1, *n*2, ..., *n*k are pairwise relatively prime, and
    where the solution is wanted modulo *n*=*n*1&centerdot;&*n*2&centerdot;...&centerdot;*n*k.
    
    The main point is to determine the numbers *c*1, *c*2, ..., *c*k such that
    for *c_i* we have 
    
    *c_i* = 1 (mod *n_i*)
    
    and 
    
    *c_i* = 0 (mod *n_j*)
    
    for any *j* different from *i*. 
    """)

st.number_input("Input the number *a*", key='a', value=2)
st.number_input("Input the number *b*", key='b', value=1001)
st.number_input("Input the number *n*", key='n', value=100)

ao = int(st.session_state.a)
bo = int(st.session_state.b)
no = int(st.session_state.n)

