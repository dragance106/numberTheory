import streamlit as st

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


st.markdown("Euclid algorithm")
st.sidebar.markdown("Euclid algorithm")


if __name__=="__main__":
    print(gcd(364105, 832139))
