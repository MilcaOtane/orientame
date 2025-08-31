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
    "<h2 style='text-align:center; color:white;'>DESCUBRE TU CAMINO<br>DISEÑA TU FUTURO CON ORIENTAME</h2>",
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

# --- Imagen de ORI ---
col_left, col_right = st.columns([2,1])
with col_right:
    st.image("ori.png", width=200)
    st.info("¡Hey! Soy ORI 🐺 tu compañero en esta aventura")


##---AAREGLANDO EL BOT 
# === ORI con globo de diálogo con cola ===
st.markdown("""
<style>
.ori-bubble {
  position: relative;
  display: inline-block;
  background: #ffffff;
  color: #0b1b3a;
  border: 2px solid #f2d7d7;
  border-radius: 16px;
  padding: 10px 14px;
  max-width: 220px;
  line-height: 1.35;
  box-shadow: 0 6px 14px rgba(0,0,0,.12);
}
.ori-bubble:after {
  content: "";
  position: absolute;
  right: -10px;          /* mueve la cola (izq/der) */
  top: 18px;             /* altura de la cola */
  width: 0; height: 0;
  border-left: 12px solid #ffffff;   /* color centro de la cola */
  border-top: 12px solid transparent;
  border-bottom: 12px solid transparent;
  filter: drop-shadow(1px 0 0 #f2d7d7); /* bordecito de la cola */
}
.ori-row {display:flex; align-items:flex-end; gap:12px;}
.ori-row .ori-left {order: 1;}
.ori-row .ori-right {order: 2;}
.ori2 {width:210px;}
</style>

<div class="ori-row">
  <div class="ori-left">
    <div class="ori-bubble">¡Hey! Soy <b>ORI</b> 😎<br>tu compañero en esta aventura</div>
  </div>
  <div class="ori-right">
    <img class="ori2" src="ori.png" alt="ORI"/>
  </div>
</div>
""", unsafe_allow_html=True)
