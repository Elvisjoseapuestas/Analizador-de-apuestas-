import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analizador Deportivo", layout="wide")
st.title("⚽ Optimizador de Apuestas: Motor de Valor")

# Lógica de reglas
def aplicar_reglas(g_l, g_v, rat, cuo):
    sugerencias = []
    if (g_l + g_v) / 2 > 2.8 and cuo >= 1.45:
        sugerencias.append("✅ Más de 2.5 Goles")
    if rat > 7.2:
        sugerencias.append("✅ Gol del Delantero Estrella")
    return ", ".join(sugerencias) if sugerencias else "Sin apuesta de valor"

# Interfaz
st.subheader("Análisis de Partido")
nombre = st.text_input("Nombre del Partido")
col1, col2 = st.columns(2)
g_l = col1.number_input("Prom. Goles Local", 0.0, 5.0, 1.5)
g_v = col2.number_input("Prom. Goles Visita", 0.0, 5.0, 1.0)
rat = col1.slider("Rating Delantero", 5.0, 10.0, 7.0)
cuo = col2.number_input("Cuota", 1.0, 5.0, 1.6)

if st.button("Generar Análisis"):
    resultado = aplicar_reglas(g_l, g_v, rat, cuo)
    st.success(f"Análisis para {nombre}: {resultado}")
