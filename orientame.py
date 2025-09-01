import streamlit as st

st.set_page_config(page_title="OrientaMe ONG", page_icon="🧭", layout="wide")

# --- Fondo azul ---
st.markdown("""
<style>
.stApp {
    background-color: #42b9f5; /* Celeste */
}
.card {
  background: #fff5f5;   /* Fondo de la tarjeta */
  border-radius: 16px;
  padding: 18px;
  min-height: 160px;
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

# --- Nombre de la ONG ---
st.title("OrientaMe ONG")

# --- Título principal ---
st.markdown(
    "<h2 style='text-align:center; color:white;'>DESCUBRE TU VOCACIÓN<br>ELIGE TU FUTURO CON ORIENTAME</h2>",
    unsafe_allow_html=True
)

# --- Cuatro tarjetas en columnas ---
cards = [
    ("💡", "Test Vocacionales", "¿Aún no sabes qué carrera elegir?"),
    ("🔑", "Charlas de Profesionales con Estudiantes", "Escucha y conversa con pros de diferentes carreras."),
    ("📚", "Apps sobre Cursos Preuniversitarios", "Refuerza lo que ya sabes y prepárate para la U."),
    ("🎯", "Becas para Estudiar en Universidades", "¡Que nada te detenga!"),
]

col1, col2, col3, col4 = st.columns(4)

for col, (icon, title, desc) in zip([col1, col2, col3, col4], cards):
    with col:
        st.markdown(
            f"""
            <div class="card">
              <div style="font-size:28px;">{icon}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


##---AAREGLANDO A ORIORI BOT 
import base64, streamlit as st

def img64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ori_b64 = img64("ori.png")

# 1) CSS (SIN f-string)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Questrial&display=swap');

.ori-container{ 
  position: fixed; bottom: 20px; right: 20px;
  display:flex; align-items:flex-start; gap:4px; z-index:9999;
}
.ori-img{ width:180px; }
.ori-bubble{ 
  font-family:'Questrial', sans-serif;
  background:#fff; color:#0b1b3a;
  border:2px solid #f2d7d7; border-radius:16px;
  padding:10px 14px; box-shadow:0 6px 14px rgba(0,0,0,.12);
  position:relative; min-height:42px;
}
.ori-bubble:after{
  content:""; position:absolute; right:-10px; top:18px;
  width:0;height:0;
  border-left:12px solid #ffffff;
  border-top:12px solid transparent;
  border-bottom:12px solid transparent;
  filter: drop-shadow(1px 0 0 #f2d7d7);
}
.msg-stack{ position:relative; width:260px; height:22px; }
.msg{ position:absolute; top:0; left:0; white-space:nowrap; overflow:hidden; }
.msg::after{ content:"|"; display:inline-block; margin-left:2px; animation: blink .8s step-end infinite; opacity:0; }
@keyframes blink { 50% { opacity:1; } }

.msg1{ animation: type1 12s steps(30,end) infinite; }
@keyframes type1{
  0% { width:0 }
  20% { width:100% }
  30% { width:100% }
  33.33% { width:0 }
  100% { width:0 }
}
.msg1::after{ animation-delay:2.4s; }

.msg2{ animation: type2 12s steps(30,end) infinite; }
@keyframes type2{
  0% { width:0 }
  33.33% { width:0 }
  53.33% { width:100% }
  63.33% { width:100% }
  66.66% { width:0 }
  100% { width:0 }
}
.msg2::after{ animation-delay:6s; }

.msg3{ animation: type3 12s steps(30,end) infinite; }
@keyframes type3{
  0% { width:0 }
  66.66% { width:0 }
  86.66% { width:100% }
  96.66% { width:100% }
  100% { width:0 }
}
.msg3::after{ animation-delay:9.6s; }
</style>
""", unsafe_allow_html=True)

# 2) HTML (AQUÍ sí usamos f-string para insertar la imagen)
st.markdown(f"""
<div class="ori-container">
  <div class="ori-bubble">
    <div class="msg-stack">
      <span class="msg msg1">¡Hey! Soy <b>ORI</b> 😎</span>
      <span class="msg msg2">Te ayudo a elegir tu carrera ✨</span>
      <span class="msg msg3">Explora tests, apps y becas 🚀</span>
    </div>
  </div>
  <img class="ori-img" src="data:image/png;base64,{ori_b64}" alt="ORI"/>
</div>
""", unsafe_allow_html=True)
##--- TITULO DE LA SECCION MERCADO LABORAL

import streamlit as st
import pandas as pd

df = pd.read_csv("Trim_Abr_May_Jun25.csv")

# --- Sección mercado laboral ---
st.markdown(
    "<h2 style='text-align:center; color:white; margin-top:50px;'>"
    "📊 ¿Cómo va el mercado laboral en Perú (Lima Metropolitana)?</h2>",
    unsafe_allow_html=True
)

# KPIs principales
col1, col2, col3 = st.columns(3)

with col1:
    ingreso_prom = df["INGTOT"].mean()
    st.metric("Ingreso Promedio Mensual (S/)", f"{ingreso_prom:,.0f}")

with col2:
    horas_prom = df["whoraT"].mean()
    st.metric("Horas trabajadas por semana", f"{horas_prom:.1f}")

with col3:
    desempleo = (df["OCUP300"]==3).mean()*100   # si 3 = desempleado
    st.metric("Tasa de Desempleo", f"{desempleo:.1f}%")

# Gráfico comparativo ingresos por sexo
sexo_map = {1: "Hombre", 2: "Mujer"}
df["SEXO"] = df["C201"].map(sexo_map)
ingreso_sexo = df.groupby("SEXO")["INGTOT"].mean()
st.bar_chart(ingreso_sexo)

##-----BASE DE DATOS Y WIDGETS

import streamlit as st
import pandas as pd

df = pd.read_csv("Trim_Abr_May_Jun25.csv")

st.title("📊 Indicadores Laborales EPEN 2025")

# Ingreso promedio total
ingreso_prom = df["INGTOT"].mean()
st.metric("Ingreso Promedio Mensual (S/)", f"{ingreso_prom:,.0f}")

# Ingreso promedio por sexo
sexo_map = {1: "Hombre", 2: "Mujer"}
df["SEXO"] = df["C201"].map(sexo_map)
ingreso_sexo = df.groupby("SEXO")["INGTOT"].mean()
st.bar_chart(ingreso_sexo)

# Horas trabajadas promedio
horas_prom = df["whoraT"].mean()
st.metric("Horas trabajadas por semana (prom)", f"{horas_prom:.1f}")



