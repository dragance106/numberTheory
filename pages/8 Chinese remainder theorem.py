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
    for each *ci* we have 
    
    *ci* = 1 (mod *ni*)
    
    and 
    
    *ci* = 0 (mod *nj*)
    
    for any *j* different from *i*. Then it is obvious that  
    
    *x* = *a*1&centerdot;*c*1 + *a*2&centerdot;*c*2 + ... + *ak*&centerdot;*ck*
    
    is a solution of the above system.
    
    Each number *ci* is obtained by taking the product 
    
    *mi*=*n1*&centerdot;...&centerdot;*n*(*i*-1)&centerdot;*n*(*i*+1)&centerdot;...&centerdot;*nk*
    
    of all moduli except for *ni*, determining the multiplicative inverse *m'i* of *mi* modulo *ni*,
    and setting
    
    *ci* = *mi*&centerdot;*m'i* (mod *n*).
    """)

st.number_input("Input the number *k*", key='k', value=2)
ko = int(st.session_state.k)

c1, c2 = st.columns(2)

with c1:
    a_values = [st.number_input(f'*a*{i}', key=f'a{i}', value=1) for i in range(ko)]

with c2:
    n_values = [st.number_input(f'*n*{i}', key=f'n{i}', value=1) for i in range(ko)]

# for i in range(1, ko+1):
#     c1.number_input(f'*a*{i}', key=f'a{i}', value=1)
#     c2.number_input(f'*n*{i}', key=f'n{i}', value=1)

st.markdown("Values entered are: ")
st.markdown("a values: " + str(a_values))
st.markdown("n values: " + str(n_values))

# a = [int(st.session_state.a) for i in range(1, ko+1)]
# n = [int(st.session_state.n) for i in range(1, ko+1)]

