import streamlit as st


st.markdown(
    """
    # Chinese remainder theorem
    
    This theorem provides a way to solve the system of modular equations
    
    *x* = *a*1 (mod *n*1)
    
    *x* = *a*2 (mod *n*2)

    ...

    *x* = *ak* (mod *nk*)

    provided the moduli *n*1, *n*2, ..., *nk* are pairwise relatively prime, and
    that the solution is wanted modulo *n*=*n*1&centerdot;*n*2&centerdot;...&centerdot;*nk*.
    
    The main point is to determine the numbers *c*1, *c*2, ..., *ck* such that
    for *ci* we have 
    
    *ci* = 1 (mod *ni*)
    
    and 
    
    *ci* = 0 (mod *nj*)
    
    for any *j* different from *i*. Then it is obvious that  
    
    *x* = *a*1&centerdot;*c*1 + *a*2&centerdot;*c*2 + ... + *ak*&centerdot;*ck*
    
    is a solution of the above system.
    
    Each number *ci* is obtained by taking the product *mi*=*n*1&centerdot;*n(i-1)n(i+1)*&\centerdot;*nk*
    of all moduli except for *ni*, determining the multiplicative inverse *m'i* of *mi* modulo *ni*,
    and setting
    
    *ci* = *mi*&centerdot;*m'i* (mod *n*).
    """)

st.number_input("Input the number *a*", key='a', value=2)
st.number_input("Input the number *b*", key='b', value=1001)
st.number_input("Input the number *n*", key='n', value=100)

ao = int(st.session_state.a)
bo = int(st.session_state.b)
no = int(st.session_state.n)
