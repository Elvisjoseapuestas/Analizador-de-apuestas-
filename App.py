import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analizador Deportivo", layout="wide")
st.title("⚽ Optimizador de Apuestas: Motor de Valor")

# Lógica de reglas sin cambios
def aplicar_reglas(datos):
    sugerencias = []
    if (datos['goles_l'] + datos['goles_v']) / 2 > 2.8 and datos['cuota'] >= 1.45:
        sugerencias.append("✅ Más de 2.5 Goles")
    if 10.0 > 10.5: # Ejemplo simplificado
        sugerencias.append("✅ Más de 9.5 Córneres")
    if datos['rating'] > 7.2:
        sugerencias.append("✅ Gol del Delantero Estrella")
    return ", ".join(sugerencias) if sugerencias else "Sin apuesta de valor"

resultados = []

# Interfaz simplificada
for i in range(5):
    st.markdown("---")
    st.subheader(f"Partido {i+1}")
    nombre = st.text_input(f"Nombre del Partido {i+1}", key=f"nombre_{i}")
    
    col1, col2 = st.columns(2)
    g_l = col1.number_input(f"Prom. Goles Local {i+1}", 0.0, 5.0, 1.5, key=f"gl_{i}")
    g_v = col2.number_input(f"Prom. Goles Visita {i+1}", 0.0, 5.0, 1.0, key=f"gv_{i}")
    rat = col1.slider(f"Rating {i+1}", 5.0, 10.0, 7.0, key=f"rt_{i}")
    cuo = col2.number_input(f"Cuota {i+1}", 1.0, 5.0, 1.6, key=f"ct_{i}")
    
    # Aquí procesamos el resultado al momento
    datos = {'goles_l': g_l, 'goles_v': g_v, 'rating': rat, 'cuota': cuo}
    resultados.append({"Partido": nombre, "Recomendación": aplicar_reglas(datos)})

# Botón final
if st.button("Generar Tabla"):
    df = pd.DataFrame(resultados)
    st.table(df)
    
