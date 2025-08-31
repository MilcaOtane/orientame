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
# Tarjetas
cards = [
    ("https://ejemplo.com/tests", "💡", "Test Vocacionales",
     "¿Aún no sabes qué carrera elegir?"),
    ("https://ejemplo.com/charlas", "🗝️", "Charlas de Profesionales con Estudiantes",
     "Escucha y conversa con pros de diferentes carreras."),
    ("https://ejemplo.com/apps", "🗂️", "Apps sobre Cursos Preuniversitarios",
     "Refuerza lo que ya sabes y prepárate para la U."),
    ("https://ejemplo.com/becas", "🎯", "Becas para Estudiar en Universidades",
     "¡Que nada te detenga!"),
]

c1,c2,c3,c4 = st.columns(4)
for col, (url, icon, title, desc) in zip([c1,c2,c3,c4], cards):
    with col:
        st.markdown(
            f"""
            <a class="cardlink" href="{url}" target="_blank">
              <div class="card">
                <h3><span class="emoji">{icon}</span>{title}</h3>
                <p>{desc}</p>
              </div>
            </a>
            """,
            unsafe_allow_html=True
        )

