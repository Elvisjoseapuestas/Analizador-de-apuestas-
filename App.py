import streamlit as st
import pandas as pd

# Configuración de la App
st.set_page_config(page_title="Analizador Deportivo Pro", layout="wide")
st.title("⚽ Optimizador de Apuestas: Motor de Valor")

# --- LÓGICA DE LAS 10 REGLAS ---
def aplicar_reglas(datos):
    sugerencias = []
    # 1. Regla de Goles (Over 2.5)
    if (datos['goles_l'] + datos['goles_v']) / 2 > 2.8 and datos['cuota'] >= 1.45:
        sugerencias.append("✅ Más de 2.5 Goles")
    # 2. Regla de Córneres
    if (datos['corners_l'] + datos['corners_v']) > 10.5 and datos['cuota'] >= 1.45:
        sugerencias.append("✅ Más de 9.5 Córneres")
    # 3. Regla de Forma
    if datos['rating_delantero'] > 7.2:
        sugerencias.append("✅ Gol del Delantero Estrella")
    
    return sugerencias if sugerencias else ["Sin apuesta de valor detectada"]

# --- INTERFAZ ---
st.header("Análisis de 5 Partidos")
resultados_finales = []

for i in range(5):
    st.subheader(f"Partido {i+1}")
    
    # Campo para ingresar el nombre del partido
    nombre_partido = st.text_input(f"Nombre del Partido {i+1}", f"Equipo L vs Equipo V", key=f"nombre_{i}")
    
    col1, col2 = st.columns(2)
    goles_l = col1.number_input(f"Promedio Goles Local {i+1}", 0.0, 5.0, 1.5, key=f"gol_l_{i}")
    goles_v = col2.number_input(f"Promedio Goles Visita {i+1}", 0.0, 5.0, 1.0, key=f"gol_v_{i}")
    rating = col1.slider(f"Rating Delantero {i+1}", 5.0, 10.0, 7.0, key=f"rat_{i}")
    cuota = col2.number_input(f"Cuota Mercado {i+1}", 1.0, 5.0, 1.6, key=f"cuo_{i}")
    
    # Aplicar reglas
    datos = {'goles_l': goles_l, 'goles_v': goles_v, 'corners_l': 5.0, 'corners_v': 5.0, 'rating_delantero': rating, 'cuota': cuota}
    apuestas = aplicar_reglas(datos)
    
    # Guardar con el nombre personalizado
    resultados_finales.append({"Partido": nombre_partido, "Recomendación": ", ".join(apuestas)})

# --- RESULTADO FINAL ---
if st.button("Generar Tabla de Apuestas Más Lógicas"):
    df = pd.DataFrame(resultados_finales)
    st.table(df)
    st.success("Análisis completado. Apuestas optimizadas bajo criterios controlados.")
    
