import streamlit as st
from functions import multiplicative_inverse
from functions import gcd


def chinese_remainder_theorem(st, k, a_values, n_values):
    for i in range(k):
        for j in range(i+1, k):
            d = gcd(n_values[i], n_values[j])
            if d > 1:
                st.markdown(f'Numbers n{i} and n{j} are not relatively prime - their gcd is {d}.')
                st.markdown(f'There are no solutions.')

    n = 1
    s = ''
    for i in range(k):
        n = n * n_values[i]
        s = s + str(n_values[i])
        if i!=k-1:
            s = s + '&centerdot;'
    st.markdown(f'The product *n* of all *ni* values is *n*={s}={n}')

    m = [n//ni for ni in n_values]
    m_inverse = [multiplicative_inverse(m[i], n_values[i]) for i in range(k)]
    c = [(m[i]*m_inverse[i]) % n for i in range(k)]

    for i in range(k):
        st.markdown(f'For *i*={i}:')
        st.markdown(f'The product *N*{i} of all moduli other than *n*{i} is *N*{i}={n}/{n_values[i]}={m[i]}.')
        st.markdown(f'The multiplicative inverse *M*{i} of *N*{i}={m[i]} modulo *n*{i}={n_values[i]} is {m_inverse[i]}.')
        st.markdown(f'The coefficient *c*{i} is *M*{i}&centerdot;*N*{i}=({m_inverse[i]})&centerdot;{m[i]}={c[i]} mod {n}.')

    x = 0
    s1 = ''
    s2 = ''
    for i in range(k):
        x = (x + a_values[i]*c[i]) % n
        s1 = s1 + f'*a*{i}&centerdot;*c*{i}'
        s2 = s2 + f'{a_values[i]}&centerdot;{c[i]}'
        if i != k-1:
            s1 = s1 + ' + '
            s2 = s2 + ' + '

    st.markdown(f'Finally:')
    st.markdown(f'The solution is x={s1}={s2}={x} mod *n*={n}.')


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
    
    is a solution of the above system (which is also unique modulo n).
    
    Each number *ci* is obtained by taking the product *Ni* = *n*/*ni* of all moduli except for *ni*, 
    determining the multiplicative inverse *Mi* of *Ni* modulo *ni*,
    and setting
    
    *ci* = *Mi*&centerdot;*Ni* (mod *n*).
    """)

st.number_input("Input the number *k*", key='k', value=2)
ko = int(st.session_state.k)

c1, c2 = st.columns(2)

with c1:
    ao_values = [st.number_input(f'*a*{i}', key=f'a{i}', value=1) for i in range(ko)]
    ao_values = [int(a) for a in ao_values]

with c2:
    no_values = [st.number_input(f'*n*{i}', key=f'n{i}', value=1) for i in range(ko)]
    no_values = [int(n) for n in no_values]

chinese_remainder_theorem(st, ko, ao_values, no_values)

