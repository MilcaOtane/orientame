import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    "<h3 style='text-align: left; color: #0000cc;'><b>OrientaMe ONG</b></h3>",
    unsafe_allow_html=True
)
import streamlit as st
#---Nombre de la pagina
st.set_page_config(page_title="OrientaMe", page_icon="🧭", layout="wide")

# --- Título principal ---
st.markdown(
    "<h2 style='text-align:center; color:#0066cc;'>DESCUBRE TU CAMINO<br>DISEÑA TU FUTURO CON ORIENTAME</h2>",
    unsafe_allow_html=True
)

# --- Distribución de columnas ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("💡 Test Vocacionales")
    st.write("¿Aún no sabes qué carrera elegir?")

with col2:
    st.subheader("🔑 Charlas de Profesionales con Estudiantes")
    st.write("Escucha y conversa con pros de diferentes carreras.")

with col3:
    st.subheader("📚 Apps sobre Cursos Preuniversitarios")
    st.write("Refuerza lo que ya sabes y prepárate para la U.")

with col4:
    st.subheader("🎯 Becas para Estudiar en Universidades")
    st.write("¡Que nada te detenga!")

# --- Espacio ---
st.write("---")

# --- Imagen de ORI con mensaje ---
col_left, col_right = st.columns([2,1])

with col_right:
    st.image("ori.png", width=200)  # Aquí coloca tu imagen de ORI en el mismo folder
    st.info("¡Hey! Soy ORI 🐺 tu compañero en esta aventura")

