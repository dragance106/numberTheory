import streamlit as st


def fast_exp(a, b, n):
    if b == 1:
        return a % n, '| 1 |', '| --- |', f'| {a%n} |'
    elif b % 2 == 1:        # b is odd
        r, line1, line2, line3 = fast_exp(a, b-1, n)
        line1 = f'| {b} ' + line1
        line2 = '| --- ' + line2
        line3 = f'| {(a*r)%n} ' + line3
        return (a*r) % n, line1, line2, line3
    else:                   # b is even
        r, line1, line2, line3 = fast_exp(a, b//2, n)
        line1 = f'| {b} ' + line1
        line2 = '| --- ' + line2
        line3 = f'| {(r*r)%n} ' + line3
        return (r*r) % n, line1, line2, line3


# def fast_exp(a, b, n):
#     if b == 1:
#         st.write(f'{a}^1 = {a%n} (mod {n})')
#         return a % n
#     elif b % 2 == 1:        # b is odd
#         st.write(f'*b*: {b} &xrarr; {b-1}')
#         r = fast_exp(a, b-1, n)
#         st.write(f'{a}^{b} = {a}&centerdot;{a}^{b-1} = {a}&centerdot;{r} = {(a*r)%n} (mod {n})')
#         return (a*r) % n
#     else:                   # b is even
#         st.write(f'*b*: {b} &xrarr; {b//2}')
#         r = fast_exp(a, b//2, n)
#         st.write(f'{a}^{b} = ({a}^{b//2})^2 = {r}^2 = {(r*r)%n} (mod {n})')
#         return (r*r) % n


st.markdown(
    """
    # Fast modular exponentiation

    This algorithm relies on the fact that the following recursive way
    of computing *a*^*b* (mod *n*) will take about log(*b*) multiplications:
    
    *a*^1 = *a* (mod *n*) when *b*=1
    
    *a*^*b* = *a*^(*b*-1) &centerdot; *a* (mod *n*) when *b* is odd
    
    *a*^*b* = (*a*^(*b*/2))^2 (mod *n*) when *b* is even  
    """)

st.number_input("Input the number *a*", key='a', value=2)
st.number_input("Input the number *b*", key='b', value=1001)
st.number_input("Input the number *n*", key='n', value=100)
st.button("Just do it")

ao = int(st.session_state.a)
bo = int(st.session_state.b)
no = int(st.session_state.n)

ro, line1, line2, line3 = fast_exp(ao, bo, no)
table = '| exp ' + line1 + '\n| --- ' + line2 + f'\n| {ao}^exp mod {no} ' + line3 + '\n'
st.markdown(table)
