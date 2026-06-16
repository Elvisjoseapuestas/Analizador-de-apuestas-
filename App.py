import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analizador Automático", layout="wide")
st.title("⚽ Optimizador Pro: Analizador de Datos CSV")

# Paso 1: Cargar el archivo
uploaded_file = st.sidebar.file_uploader("Sube tu archivo (CSV)", type="csv")

if uploaded_file is not None:
    # Leer el archivo
    df = pd.read_csv(uploaded_file)
    st.write("### Vista previa de tus datos")
    st.dataframe(df.head())
    
    # Seleccionar partido
    partido = st.selectbox("Elige el partido a analizar:", df['nombre_partido'])
    datos = df[df['nombre_partido'] == partido].iloc[0]
    
    # Análisis automático
    st.subheader(f"Análisis para: {partido}")
    
    # Reglas automáticas basadas en las columnas del CSV
    goles_promedio = (datos['goles_local'] + datos['goles_visita']) / 2
    corners_total = datos['corners_local'] + datos['corners_visita']
    
    # Resultados
    if goles_promedio >= 2.5: st.success("✅ Goles: Alta probabilidad Over 2.5")
    else: st.warning("⚽ Goles: Tendencia conservadora (Under 3.5)")
        
    if corners_total >= 9.5: st.success("✅ Córneres: Alta probabilidad Over 8.5")
    else: st.warning("🚩 Córneres: Poca actividad esperada")
        
    st.info(f"Cuota sugerida basada en datos: {datos['cuota_referencia']}")
else:
    st.info("Por favor, sube un archivo CSV en el menú lateral para comenzar.")
