import streamlit as st

st.title("App em Python – Demonstração")

st.write("Exemplo simples de entrada, decisão e saída")

idade = st.number_input("Digite sua idade", min_value=0, step=1)

if st.button("Verificar"):
    if idade >= 18:
        st.success("Maior de idade")
    else:
        st.warning("Menor de idade")
