import streamlit as st
st.title("Prueba de Funcionamiento")
nombre = st.text_input("Escribe el nombre del partido")
if st.button("Analizar"):
    if nombre:
        st.success(f"Analizando el partido: {nombre}")
    else:
        st.error("Por favor escribe un nombre")
