import streamlit as st
import pandas as pd
import numpy as np

# --- Cambiar color de fondo ---
page_bg = """
<style>
.stApp {
    background-color: #42b9f5; /* Celeste */
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

#---Nomnbre de la ONG izquierda
st.title("OrientaMe ONG")

import streamlit as st
#---Nombre de la pagina
st.set_page_config(page_title="OrientaMe", page_icon="🧭", layout="wide")

# --- Título principal ---
st.markdown(
    "<h2 style='text-align:center; color:white;'>DESCUBRE TU CAMINO<br>DISEÑA TU FUTURO CON ORIENTAME</h2>",
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
    st.image("ori.png", width=200)  
    st.info("¡Hey! Soy ORI 🐺 tu compañero en esta aventura")

##---MODO TARJETAS
import streamlit as st

st.set_page_config(page_title="OrientaMe ONG", page_icon="🧭", layout="wide")

# --- CSS tarjetas con color ---
st.markdown("""
<style>
.stApp { background: #42b9f5; }

.card {
  background: #fff5f5;   /* 👈 aquí el colorcito del fondo de la tarjeta */
  border-radius: 16px;
  padding: 18px;
  min-height: 140px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: transform .15s ease, box-shadow .15s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
.card h3 {
  margin: 0;
  font-size: 18px;
  font-weight: bold;
}
.card p {
  margin-top: 8px;
  font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# --- Ejemplo tarjeta ---
st.markdown("""
<div class="card">
  <div style="font-size:28px;">💡</div>
  <h3>Test Vocacionales</h3>
  <p>¿Aún no sabes qué carrera elegir?</p>
</div>
""", unsafe_allow_html=True)
