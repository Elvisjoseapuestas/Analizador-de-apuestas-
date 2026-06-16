import streamlit as st

st.set_page_config(page_title="Analizador Pro", layout="wide")
st.title("⚽ Optimizador Pro: Goles y Córneres")

def analizar_todo(g_l, g_v, c_l, c_v, rat, cuo):
    resultados = []
    
    # Análisis de Goles
    promedio_g = (g_l + g_v) / 2
    if promedio_g >= 2.5: resultados.append("🔥 Goles: Alta probabilidad Over 2.5")
    else: resultados.append("⚽ Goles: Tendencia conservadora (Under 3.5)")
    
    # Análisis de Córneres (Nueva Lógica)
    total_c = c_l + c_v
    if total_c >= 9.5: resultados.append("🚩 Córneres: Alta probabilidad Over 8.5")
    elif total_c >= 7.5: resultados.append("🚩 Córneres: Escenario estándar (Over 7.5)")
    else: resultados.append("🛡️ Córneres: Partido cerrado/poca actividad")
    
    # Análisis de Cuota/Valor
    if cuo >= 1.7: resultados.append("💰 Cuota: Valor detectado")
    
    return resultados

# Interfaz
nombre = st.text_input("Nombre del Partido")
col1, col2 = st.columns(2)

st.subheader("Datos de Goles")
g_l = col1.number_input("Goles Local", 0.0, 5.0, 1.5)
g_v = col2.number_input("Goles Visita", 0.0, 5.0, 1.0)

st.subheader("Datos de Córneres")
c_l = col1.number_input("Córneres Local (promedio)", 0.0, 15.0, 5.0)
c_v = col2.number_input("Córneres Visita (promedio)", 0.0, 15.0, 4.5)

rat = st.slider("Rating Delantero", 5.0, 10.0, 7.0)
cuo = st.number_input("Cuota", 1.0, 10.0, 1.6)

if st.button("Generar Análisis Completo"):
    res = analizar_todo(g_l, g_v, c_l, c_v, rat, cuo)
    st.success(f"Resultados para: {nombre}")
    for item in res:
        st.markdown(f"- {item}")
