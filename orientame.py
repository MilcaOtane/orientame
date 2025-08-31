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

# --- convierte tu imagen a base64 
def img64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ori_b64 = img64("ori.png")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Questrial&display=swap');

/* contenedor fijo abajo-derecha */
.ori-container{
  position: fixed; bottom: 20px; right: 20px;
  display:flex; align-items:flex-start; gap: 4px; z-index: 9999;
}

/* imagen de ORI */
.ori-img{ width: 180px; }

/* globo base */
.ori-bubble{
  font-family: 'Questrial', sans-serif;
  background:#fff; color:#0b1b3a;
  border:2px solid #f2d7d7; border-radius:16px;
  padding:10px 14px; box-shadow:0 6px 14px rgba(0,0,0,.12);
  position:relative; min-height: 42px;
}
/* cola del globo */
.ori-bubble:after{
  content:""; position:absolute; right:-10px; top:18px;
  width:0;height:0;
  border-left:12px solid #ffffff;
  border-top:12px solid transparent;
  border-bottom:12px solid transparent;
  filter: drop-shadow(1px 0 0 #f2d7d7);
}

/* stack de mensajes (se superponen) */
.msg-stack{ position:relative; width: 260px; height: 22px; } /* alto de una línea */
.msg{ 
  position:absolute; top:0; left:0;
  white-space:nowrap; overflow:hidden;
  border-right:2px solid #0b1b3a; /* cursor */
}

/* parpadeo del cursor */
@keyframes blink{50%{ border-color: transparent; }}

/* ---  ROTACIÓN + TYPING (3 mensajes, ciclo 12s)  --- */
/* MSG 1: 0-30% visible con typing */
.msg1{ animation: type1 12s steps(30,end) infinite, blink .8s step-end infinite; }
@keyframes type1{
  0%{width:0}
  20%{width:100%}   /* escribe */
  30%{width:100%}   /* pausa leído */
  33.33%{width:0}   /* borra y oculta */
  100%{width:0}
}
/* MSG 2: 33%-66% */
.msg2{ animation: type2 12s steps(30,end) infinite, blink .8s step-end infinite; }
@keyframes type2{
  0%{width:0}
  33.33%{width:0}
  53.33%{width:100%}
  63.33%{width:100%}
  66.66%{width:0}
  100%{width:0}
}
/* MSG 3: 66%-100% */
.msg3{ animation: type3 12s steps(30,end) infinite, blink .8s step-end infinite; }
@keyframes type3{
  0%{width:0}
  66.66%{width:0}
  86.66%{width:100%}
  96.66%{width:100%}
  100%{width:0}
}
</style>

<div class="ori-container">
  <div class="ori-bubble">
    <div class="msg-stack">
      <span class="msg msg1">¡Hey! Soy <b>ORI</b> 😎</span>
      <span class="msg msg2">Te ayudo a elegir tu carrera ✨</span>
      <span class="msg msg3">Explora tests, apps y becas 🚀</span>
    </div>
  </div>
  <img class="ori-img" src="data:image/png;base64,{{B64}}" alt="ORI" />
</div>
""".replace("{{B64}}", ori_b64), unsafe_allow_html=True)


