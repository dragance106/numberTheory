import streamlit as st
from functions import gcd, phi, prime


st.markdown(
    """
    # RSA cryptosystem
    
    Safety of this public key cryptographic protocol is based on the assumption
    that it is *computationally hard* to find 
    either the prime number decomposition of a large number $n$ 
    or the value of $\phi(n)$, 
    especially when $n$ has only two large prime factors $p$ and $q$.

    RSA works as follows.
    For different primes $p$ and $q$, let $n=pq$, so that $\phi(n)=(p-1)(q-1)$.
    Let $e$ be a small odd integer that is relatively prime to $\phi(n)$,
    and let $d$ be the multiplicative inverse of $e$ modulo $\phi(n)$.
    The pair $(e,n)$ forms the *public key*, and
    the pair $(d,n)$ forms the *secret key*.
    
    It is assumed that a message consists of a sequence of numbers (modulo $n$),
    each of which is encrypted and decrypted separately.
    Number $M$ is encrypted by $M'$ where
    $$M' = P(M) = M^e \mod n,$$
    while it is decrypted back to $M$ using 
    $$M = S(M') = M'^d \mod n.$$
        
    After the user enters $p$, $q$ and $e$,
    the key $(e,n)$ is made public, 
    while the key $(d,n)$ and the values $p$, $q$ and $\phi(n)$ are kept secret.
    """)

st.number_input("Input prime $p$", key='p', value=17)
st.number_input("Input prime $q$", key='q', value=23)
st.number_input("Input public exponent $e$", key='e', value=3)

po = int(st.session_state.p)
qo = int(st.session_state.q)
eo = int(st.session_state.e)

no = po * qo
fio = phi(no)

if prime(po) is False:
    st.markdown(f"$p$={po} is not a prime")
elif prime(qo) is False:
    st.markdown(f"$q$={qo} is not a prime")
elif gcd(eo, fio) > 1:
    st.markdown(f"$e$={eo} is not relatively prime to $\phi(n)$={fio}")
else:
    st.markdown("Be right there!")