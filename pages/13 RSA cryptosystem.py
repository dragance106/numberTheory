import streamlit as st
import functions as fun


def fast_exp(a, b, n):
    if b == 1:
        st.write(f'{a}^1 = {a%n} (mod {n})')
        return a % n
    elif b % 2 == 1:        # b is odd
        st.write(f'*b*: {b} &xrarr; {b-1}')
        r = fast_exp(a, b-1, n)
        st.write(f'{a}^{b} = {a}&centerdot;{a}^{b-1} = {a}&centerdot;{r} = {(a*r)%n} (mod {n})')
        return (a*r) % n
    else:                   # b is even
        st.write(f'*b*: {b} &xrarr; {b//2}')
        r = fast_exp(a, b//2, n)
        st.write(f'{a}^{b} = ({a}^{b//2})^2 = {r}^2 = {(r*r)%n} (mod {n})')
        return (r*r) % n


@st.fragment
def encrypt_fragment(e, n):
    st.number_input("Input number to be encrypted", key='m1', value=100)
    m1 = int(st.session_state.m1)
    st.markdown(f"Encrypted value will be equal to {m1}^{e} mod {n}:")
    m2 = fast_exp(m1, e, n)
    st.markdown(f'Encrypted number is {m2}.')


@st.fragment
def decrypt_fragment(d, n):
    st.number_input("Input number to be decrypted", key='m2', value=213)
    m2 = int(st.session_state.m2)
    st.markdown(f"Decrypted/original value will be equal to {m2}^{d} mod {n}:")
    m1 = fast_exp(m2, d, n)
    st.markdown(f'Original number is {m1}.')


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
     
    $$M = S(M') = (M')^d \mod n.$$
        
    After the user enters $p$, $q$ and $e$,
    the key $(e,n)$ is made *public*, 
    while the key $(d,n)$ and the values $p$, $q$ and $\phi(n)$ are kept *secret*.
    """)

st.number_input("Input prime $p$", key='p', value=17)
st.number_input("Input prime $q$", key='q', value=23)
st.number_input("Input public exponent $e$", key='e', value=3)

po = int(st.session_state.p)
qo = int(st.session_state.q)
eo = int(st.session_state.e)

no = po * qo
fio = fun.phi(no)

if fun.prime(po) is False:
    st.markdown(f"$p$={po} is not a prime")
elif fun.prime(qo) is False:
    st.markdown(f"$q$={qo} is not a prime")
elif fun.gcd(eo, fio) > 1:
    st.markdown(f"$e$={eo} is not relatively prime to $\phi(n)$={fio}")
else:
    st.markdown(f'$n=pq$={no}')
    st.markdown(f'$\phi(n)=(p-1)(q-1)$={fio}')

    do = fun.multiplicative_inverse(eo, fio)
    st.markdown(f'Secret exponent for decryption is $d$={do}')

    encrypt_fragment(eo, no)
    decrypt_fragment(do, no)