import streamlit as st
from functions import gcd


def phi_list(n):
    zn = []
    for a in range(1, n):
        d = gcd(a, n)
        if d > 1:
            st.markdown(f'{a} is NOT in $Z_{n}^*$ since gcd({a}, {n})={d}>1')
        else:
            st.markdown(f'{a} is in $Z_{n}^*$')
            zn.append(a)

    st.markdown(f'Elements of $Z_{n}^*$ are: {zn}')
    st.markdown(f'$\phi({n})=|Z_{n}^*|={len(zn)}')


st.markdown(
    """
    # Euler's phi function
    
    The function $\phi(n)$ denotes the cardinality of 
    the set $Z_n^*$ of those numbers between 1 and $n-1$
    that are relatively prime to $n$.
    
    This function can be computed according to the formula

    $$\\phi(n) = n \\prod_{\\textrm{prime }p|n} \\left(1-\\frac1p\\right).$$
        
    It is multiplicative, 
    meaning that $\phi(mn)=\phi(m)\phi(n)$ for relatively prime $m$ and $n$.
    Also if we know the prime decomposition
    
    $$n = p_1^{\\alpha_1} p_2^{\\alpha_2} \\cdot\\dots\\cdot p_k^{\\alpha_k},$$
    
    then
    
    $$\\phi(n) = p_1^{\\alpha_1-1}(p_1-1) p_2^{\\alpha_2-1}(p_2-1) \\cdot\\dots\\cdot p_k^{\\alpha_k-1}(p_k-1).$$
    """)

# $$\\phi(n) = n \\prod_{\\substack{p\\mbox{ is prime, }\\p|n} \\left(1-\\frac1p\\right).$$

st.number_input("Input the number $n$", key='n', value=10)
no = int(st.session_state.n)
phi_list(no)

