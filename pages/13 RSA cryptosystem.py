import streamlit as st
from functions import gcd, phi


st.markdown(
    """
    # RSA cryptosystem
    
    Shortly describe the process,
    what is the public key,
    what is the private key,
    how encryption goes,
    how decryption goes.
    
    After the user enters p, q and e,
    report public key (e,n),
    keep secret key (d,n) and keep p, q and $\phi(n)$ secret.
    
    Show extra fields:
    - number input for encrypting M, label for showing encrypted result,
    - number input for decrypting M', label for showing decrypted result.    
    """)

st.number_input("Input prime $p$", key='p', value=17)
st.number_input("Input prime $q$", key='q', value=23)
st.number_input("Input exponent $e$", key='e', value=3)

po = int(st.session_state.p)
qo = int(st.session_state.q)
eo = int(st.session_state.e)

st.info("This is purely informational message")

pass
