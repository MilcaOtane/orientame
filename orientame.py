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
#
import streamlit as st
import pandas as pd
import numpy as np

# =========================
# Cargar EPEN (usa tu ruta)
# =========================
df = pd.read_csv("Trim_Abr_May_Jun25.csv")

# ================
# Mapeos juguetones
# ================
sexo_map = {1: "Hombre", 2: "Mujer"}
df["SEXO_TXT"] = df["C201"].map(sexo_map).fillna("Otro/NR")

# “Edad” en bandas lúdicas (basado en C203 por categorías de la encuesta)
def band_age(x):
    if pd.isna(x): return "NR"
    try:
        x = int(x)
    except:
        return "NR"
    if x <= 2:      # categorías bajas ~ “adolescentes”
        return "15-19"
    elif x <= 4:
        return "20-24"
    elif x >= 5:
        return "25+"
    return "NR"

df["EDAD_BAND"] = df["C203"].apply(band_age)

# ===========
# Sección UI
# ===========
st.markdown(
    "<h3 style='text-align:center; color:white; margin: 36px 0 6px;'>🕹️ Zona de Juego: Mercado Laboral (Lima/Callao)</h3>",
    unsafe_allow_html=True
)
st.caption("Filtra, compara y descubre datos clave del trabajo en tu ciudad. *Mini-widgets para decidir mejor tu camino.*")

# -------------
# Filtros Chips
# -------------
cols_f = st.columns(3)
with cols_f[0]:
    sex_pick = st.segmented_control("Sexo", options=["Todos", "Hombre", "Mujer", "Otro/NR"], default="Todos")
with cols_f[1]:
    age_pick = st.segmented_control("Edad", options=["Todas", "15-19", "20-24", "25+", "NR"], default="Todas")
with cols_f[2]:
    view_pick = st.segmented_control("Comparar por", options=["Nada", "Sexo", "Edad"], default="Nada")

fdf = df.copy()
if sex_pick != "Todos":
    fdf = fdf[fdf["SEXO_TXT"] == sex_pick]
if age_pick != "Todas":
    fdf = fdf[fdf["EDAD_BAND"] == age_pick]

# =====================
# Mini-KPIs (compactos)
# =====================
def mini_card(label, value, suffix=""):
    st.markdown(
        f"""
        <div style="
          background: rgba(255,255,255,0.92);
          border:1px solid #e7eefc;
          border-radius:14px;
          padding:10px 12px;
          text-align:center;
          min-height:70px;">
          <div style="font-size:12px; color:#334155; margin-bottom:4px;">{label}</div>
          <div style="font-size:18px; font-weight:800; color:#0f172a;">
            {value}{suffix}
          </div>
        </div>
        """, unsafe_allow_html=True
    )

c1, c2, c3 = st.columns(3)

ing_prom = float(np.nanmean(fdf["INGTOT"])) if "INGTOT" in fdf.columns else np.nan
with c1:
    mini_card("💰 Ingreso prom. (S/)", f"{ing_prom:,.0f}" if not np.isnan(ing_prom) else "—")

if "whoraT" in fdf.columns:
    horas = float(np.nanmean(fdf["whoraT"]))
    with c2:
        mini_card("⏱️ Horas/sem prom.", f"{horas:.1f}" if not np.isnan(horas) else "—")
else:
    with c2:
        mini_card("⏱️ Horas/sem prom.", "—")

# “Participación ocupada” simple si OCUP300==1 mayormente
if "OCUP300" in fdf.columns:
    part = float((fdf["OCUP300"] == 1).mean() * 100)
    with c3:
        mini_card("👩‍💼 Ocupación (muestra)", f"{part:.0f}", "%")
else:
    with c3:
        mini_card("👩‍💼 Ocupación (muestra)", "—")

st.write("")  # respiro

# ==========================
# Modo Comparar (barras mini)
# ==========================
if view_pick == "Sexo":
    grp = fdf.groupby("SEXO_TXT")["INGTOT"].mean().sort_values(ascending=False)
    st.markdown("<div style='font-size:13px; color:white; text-align:center;'>💡 Ingreso promedio por sexo</div>", unsafe_allow_html=True)
    st.bar_chart(grp)

elif view_pick == "Edad":
    grp = fdf.groupby("EDAD_BAND")["INGTOT"].mean().reindex(["15-19","20-24","25+","NR"]).dropna()
    st.markdown("<div style='font-size:13px; color:white; text-align:center;'>💡 Ingreso promedio por grupo etario</div>", unsafe_allow_html=True)
    st.bar_chart(grp)

##
##
## SOLUCION¿?
import streamlit as st
import pandas as pd
import numpy as np

# Carga
df = pd.read_csv("Trim_Abr_May_Jun25.csv")

# ====== Opcional: mapping de ocupación (si lo subes) ======
# Estructura esperada: columnas ["codigo","ocupacion"]
try:
    map_ocu = pd.read_csv("ciuo_mapping.csv")  # <-- súbelo cuando lo tengas
    map_ocu["codigo"] = map_ocu["codigo"].astype(str)
except Exception:
    map_ocu = None

# ====== Campos clave con tolerancia de nombres ======
COL_OCU = "C308_COD" if "C308_COD" in df.columns else None      # ocupación principal (código)
COL_SEX = "C207" if "C207" in df.columns else ("C201" if "C201" in df.columns else None)
COL_AGE = "C208" if "C208" in df.columns else None
COL_HRS = "whoraT" if "whoraT" in df.columns else None
COL_INC = "INGTOT" if "INGTOT" in df.columns else ("INGTOTP" if "INGTOTP" in df.columns else None)

# ====== Enriquecimiento ======
# Sexo
sexo_map = {1: "Hombre", 2: "Mujer"}
if COL_SEX:
    df["SEXO_TXT"] = df[COL_SEX].map(sexo_map).fillna("Otro/NR")
else:
    df["SEXO_TXT"] = "NR"

# Edad (bandas reales si hay C208 en años; si no, NR)
def band_age_years(x):
    if pd.isna(x): return "NR"
    try:
        x = int(x)
    except:
        return "NR"
    if x <= 19: return "15-19"
    if x <= 24: return "20-24"
    if x <= 29: return "25-29"
    if x <= 39: return "30-39"
    return "40+"

if COL_AGE:
    df["EDAD_BAND"] = df[COL_AGE].apply(band_age_years)
else:
    df["EDAD_BAND"] = "NR"

# Ocupación: etiqueta = código (o nombre si existe mapping)
if COL_OCU:
    df["_OCU_COD_TXT"] = df[COL_OCU].astype("Int64").astype(str)
    if map_ocu is not None:
        df = df.merge(map_ocu, left_on="_OCU_COD_TXT", right_on="codigo", how="left")
        df["_OCU_ETQ"] = df["ocupacion"].fillna(df["_OCU_COD_TXT"])
    else:
        df["_OCU_ETQ"] = df["_OCU_COD_TXT"]
else:
    df["_OCU_ETQ"] = "NR"

# ====== UI: sección compacta y lúdica ======
st.markdown(
    "<h3 style='text-align:center; color:white; margin:28px 0 8px;'>🎮 Explora por ocupación</h3>",
    unsafe_allow_html=True
)
st.caption("Elige una ocupación y compara ingresos/horas por sexo y edad. (Datos EPEN 2025 – Lima/Callao)")

# Selector de ocupación (muestra top más frecuentes para que sea ágil)
top_ocu = (
    df[df["_OCU_ETQ"]!="NR"]
    .groupby("_OCU_ETQ")
    .size()
    .sort_values(ascending=False)
    .head(30)
    .index.tolist()
)
ocu_sel = st.selectbox("Ocupación (código o nombre)", ["(todas)"] + top_ocu, index=0)

fdf = df.copy()
if ocu_sel != "(todas)":
    fdf = fdf[fdf["_OCU_ETQ"] == ocu_sel]

# ====== Mini-KPIs ======
def mini(label, value):
    st.markdown(
        f"""
        <div style="background: rgba(255,255,255,0.92); border:1px solid #e7eefc;
        border-radius:14px; padding:10px 12px; text-align:center; min-height:64px;">
          <div style="font-size:12px; color:#334155; margin-bottom:4px;">{label}</div>
          <div style="font-size:18px; font-weight:800; color:#0f172a;">{value}</div>
        </div>
        """, unsafe_allow_html=True
    )

c1,c2,c3 = st.columns(3)

# Ingreso promedio
if COL_INC and fdf[COL_INC].notna().any():
    ing = float(np.nanmean(fdf[COL_INC]))
    mini("💰 Ingreso prom. (S/)", f"{ing:,.0f}")
else:
    mini("💰 Ingreso prom. (S/)", "—")

# Horas semanales
if COL_HRS and fdf[COL_HRS].notna().any():
    hrs = float(np.nanmean(fdf[COL_HRS]))
    mini("⏱️ Horas/sem prom.", f"{hrs:.1f}")
else:
    mini("⏱️ Horas/sem prom.", "—")

# Tamaño muestra
mini("📦 Muestra", f"{len(fdf):,}")

st.write("")

# ====== Comparadores compactos ======
cols = st.columns(2)

# Por sexo
with cols[0]:
    st.markdown("<div style='font-size:13px; color:white; text-align:center;'>💡 Ingreso por sexo</div>", unsafe_allow_html=True)
    if COL_INC:
        by_sex = fdf.groupby("SEXO_TXT")[COL_INC].mean().dropna()
        st.bar_chart(by_sex)

# Por edad
with cols[1]:
    st.markdown("<div style='font-size:13px; color:white; text-align:center;'>💡 Ingreso por edad</div>", unsafe_allow_html=True)
    if COL_INC:
        order_age = ["15-19","20-24","25-29","30-39","40+","NR"]
        by_age = fdf.groupby("EDAD_BAND")[COL_INC].mean().reindex(order_age).dropna()
        st.bar_chart(by_age)

# ====== Nota para devs (oculta si quieres) ======
with st.expander("ℹ️ Notas de datos"):
    st.write("""
- *C308_COD* = Ocupación principal (código). Si cargas `ciuo_mapping.csv` se verán los nombres.
- *C309_COD* = Actividad/sector del negocio.
- *OCUP300* = Condición de actividad.
- *C207* = Sexo; *C208* = Edad.
- *whoraT* = Horas trabajadas totales; *INGTOT* = Ingreso total mensual.
    """)





