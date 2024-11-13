import streamlit as st

st.markdown(
    """
    # Euler's phi function
    
    The function $\phi(n)$ denotes the cardinality of 
    the set $Z_n^*$ of those numbers between 1 and $n-1$
    that are relatively prime to $n$.
    
    This function can be computed according to the formula
    $$\phi(n) = n \prod_{\substack{p\mbox{ is prime} \\ p\div n}} \left(1-\frac{1}{p}\right).$$
    
    It is multiplicative, 
    meaning that $\phi(mn)=\phi(m)\phi(n)$ for relatively prime $m$ and $n$.
    Also if we know the prime decomposition
    $$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdot\dots\cdot p_k^{\alpha_k},$$
    then
    $$\phi(n) = p_1^{\alpha_1-1}(p_1-1) p_2^{\alpha_2-1}(p_2-1) \cdot\dots\cdot p_k^{\alpha_k-1}(p_k-1).$$
    """)

st.number_input("Input the number $n$", key='n', value=10)
no = int(st.session_state.n)
