import streamlit as st

st.set_page_config(page_title="Analizador Deportivo", layout="wide")
st.title("⚽ Optimizador de Apuestas: Motor de Análisis")

# Lógica flexible: analiza según lo que ingreses
def generar_analisis(g_l, g_v, rat, cuo):
    opciones = []
    
    # Análisis de Goles (Siempre sugiere algo según el promedio)
    promedio = (g_l + g_v) / 2
    if promedio >= 2.5:
        opciones.append("🔥 Alta probabilidad: Over 2.5 Goles")
    elif promedio >= 1.5:
        opciones.append("📈 Probabilidad media: Over 1.5 Goles")
    else:
        opciones.append("⚽ Escenario conservador: Menos de 3.5 Goles")
    
    # Análisis de Rating (Sin juzgar si es bueno o malo, solo indica la tendencia)
    if rat >= 7.5:
        opciones.append("⭐ Delantero con tendencia ofensiva")
    else:
        opciones.append("🛡️ Partido enfocado en control de juego")
        
    # Análisis de Cuota
    if cuo >= 1.8:
        opciones.append("💰 Cuota con valor de riesgo (Value Bet)")
    else:
        opciones.append("🎯 Apuesta de mercado seguro")
        
    return opciones

# Interfaz
st.subheader("Datos del Partido")
nombre = st.text_input("Nombre del Partido (Ej: Equipo A vs Equipo B)")
col1, col2 = st.columns(2)
g_l = col1.number_input("Prom. Goles Local", 0.0, 5.0, 1.5)
g_v = col2.number_input("Prom. Goles Visita", 0.0, 5.0, 1.0)
rat = col1.slider("Rating Delantero", 5.0, 10.0, 7.0)
cuo = col2.number_input("Cuota", 1.0, 5.0, 1.6)

if st.button("Analizar Partido"):
    resultados = generar_analisis(g_l, g_v, rat, cuo)
    st.success(f"Análisis para: {nombre}")
    st.write("### Apuestas disponibles y tendencias:")
    for opt in resultados:
        st.markdown(f"- {opt}")
        
    # Conclusión final
    st.info(f"Lo más probable basado en tus datos: Es un partido con tendencia a {'goles' if (g_l+g_v)/2 > 2 else 'control de juego'}.")
