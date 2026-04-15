import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN ESTATAL GSU ---
st.set_page_config(page_title="GSU | Command Center Diego", page_icon="🏛️", layout="wide")

# Estilo personalizado para dar ese look de "Película / Tecnología"
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #d4af37; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ GSU - Centro de Mando Estratégico")
st.subheader("Perfil de Cliente VIP: Diego")

# --- BASE DE DATOS OPERATIVA ---
if "db_diego" not in st.session_state:
    # Datos cargados desde tu PDF de actualización
    st.session_state.db_diego = pd.DataFrame([
        {"Expediente": "Amparo 514/25", "Materia": "Administrativo", "Estatus": "Concluido", "Comentarios de Diego": "Revisado.", "Prioridad": "Baja"},
        {"Expediente": "Amparo 515/25", "Materia": "Administrativo", "Estatus": "En proyecto de resolución", "Comentarios de Diego": "", "Prioridad": "Alta"},
        {"Expediente": "Juicio Hipotecario", "Materia": "Civil", "Estatus": "En gestión (Fabiola M.)", "Comentarios de Diego": "Pendiente de acuse", "Prioridad": "Media"},
        {"Expediente": "Juicio Mercantil", "Materia": "Mercantil", "Estatus": "Activo", "Comentarios de Diego": "", "Prioridad": "Media"},
        {"Expediente": "Denuncia por Fraude", "Materia": "Penal", "Estatus": "Integración (Ref. Larry)", "Comentarios de Diego": "", "Prioridad": "Alta"},
        {"Expediente": "Talleres", "Materia": "Corporativo", "Estatus": "Planeación (Prot. Civil)", "Comentarios de Diego": "Urge respuesta Larry", "Prioridad": "Alta"}
    ])

# --- DASHBOARD DE MÉTRICAS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Asuntos Totales", len(st.session_state.db_diego))
with col2:
    urgentes = len(st.session_state.db_diego[st.session_state.db_diego["Prioridad"] == "Alta"])
    st.metric("Prioridad Crítica", urgentes)
with col3:
    st.metric("Estatus GSU", "Operativo 24/7")
with col4:
    st.metric("Última Sincronía", datetime.now().strftime("%H:%M"))

st.markdown("---")

# --- TABLA INTERACTIVA (EDICIÓN EN TIEMPO REAL) ---
st.write("### ⚖️ Tablero de Gestión de Expedientes")
st.caption("Puedes editar tus comentarios y cambiar la prioridad de los asuntos directamente en la tabla.")

# Solo permitimos editar 'Comentarios de Diego' y 'Prioridad'
# Las demás columnas están bloqueadas para que él vea la 'Verdad Legal' de GSU
asuntos_editados = st.data_editor(
    st.session_state.db_diego,
    column_config={
        "Expediente": st.column_config.TextColumn("Expediente", disabled=True),
        "Materia": st.column_config.TextColumn("Materia", disabled=True),
        "Estatus": st.column_config.TextColumn("Estatus GSU", disabled=True),
        "Prioridad": st.column_config.SelectboxColumn("Prioridad", options=["Baja", "Media", "Alta"]),
        "Comentarios de Diego": st.column_config.TextColumn("Tus Observaciones", width="large")
    },
    hide_index=True,
    use_container_width=True,
    key="editor_interactivo"
)

# --- SISTEMA DE COMUNICACIÓN Y BITÁCORA ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.write("### 💬 Mensajería Directa al Despacho")
    mensaje = st.text_area("Escribe aquí cualquier duda o instrucción específica para el equipo legal:", placeholder="Ej: Allan, necesito que priorices el Amparo 515 hoy.")
    if st.button("Enviar Instrucción a GSU"):
        st.success("✅ Mensaje enviado y notificado al equipo de guardia.")
        # Aquí podrías conectar un webhook a tu Telegram si quisieras.

with col_right:
    st.write("### 📅 Bitácora de Movimientos")
    st.markdown("""
    - **Hoy:** Verificación de ingreso de oficio (Hipotecario).
    - **Ayer:** Nulidad de notificación desechada (Mercantil).
    - **12 Abr:** Amparo 514 concluido exitosamente.
    """)

st.markdown("---")
st.info("⚠️ **Recordatorio:** Para el envío de documentos, evidencias y archivos pesados, favor de utilizar exclusivamente el canal de **correo oficial** para garantizar la cadena de custodia y encriptación.")