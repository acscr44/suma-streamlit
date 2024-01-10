import streamlit as st

st.title('Suma tres números')

st.write('## Usando `st.number_input`')

n1 = st.number_input("Inserta el primer sumando: ", step=1)
n2 = st.number_input("Inserta el segundo sumando: ", step=1)
n3 = st.number_input("Inserta el tercer sumando: ", step=1)

st.write('La suma de los tres números es ', n1 + n2 + n3)

st.divider()

st.write('## Usando `st.slider`')

p1 = st.slider("Inserta el primer sumando: ", min_value=0, max_value=100, step=1)
p2 = st.slider("Inserta el segundo sumando: ", min_value=0, max_value=100, step=1)
p3 = st.slider("Inserta el tercer sumando: ", min_value=0, max_value=100, step=1)

st.write('La suma de los tres números es ', p1 + p2 + p3)

# if number:
#     st.write('Hola, ', name, ":ok_hand:")
# name = st.text_input("Dime tu nombre: ")