import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from models import (
    consumo_proteina, inventario, consumo_nolineal, electrolitos,
    suplementos_acoplados
)

# ===== CONFIGURACIÓN =====
st.set_page_config(
    page_title="DiffEq Fitness - Proyecto Ecuaciones Diferenciales",
    page_icon="images/logo.png",  
    layout="wide"
)
st.image("images/logo.png", width=200)

# ===== ESTILOS =====
st.markdown("""
<style>
    .main { background-color: #F5F7FA; }
    .header {
        background-color: #0B3D91;
        padding: 10px;
        color: white;
        text-align: center;
        border-radius: 8px;
        font-size: 20px;
    }
    .stButton>button {
        background-color: #6B8E23;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 6px 20px;
        border: none;
    }
    .footer {
        background-color: #0B3D91;
        padding: 15px;
        text-align: center;
        color: white;
        border-radius: 8px;
        margin-top: 30px;
    }
    div[role='radiogroup'] > label > div:first-child {
        background-color: black;
        border: 2px solid #6B8E23;
        border-radius: 50%;
    }
    div[role='radiogroup'] > label > div:first-child[aria-checked="true"] {
        background-color: #6B8E23 !important;
        border: 2px solid #6B8E23 !important;
    }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("<div class='header'>📊 DiffEq Fitness - Proyecto Ecuaciones Diferenciales</div>", unsafe_allow_html=True)
st.write("Materia: 2026 1-ECUACIONES DIFERENCIALES-2310-8A MOM 2 VIRTUAL ")
st.write("Realizado por: **David Steven Malagon Luque**")

# ===== MENÚ =====
menu = st.sidebar.radio("📂 MENÚ", [
    "1. Consumo de Proteína",
    "2. Inventario",
    "3. Consumo No Lineal",
    "4. Electrolitos",
    "5. Suplementos Acoplados",

])

# ===== FUNCIÓN PARA MOSTRAR RESULTADOS =====
def mostrar_resultados(t, y, titulo, imagen, explicacion_constante, tema, conclusion):
    col1, col2 = st.columns([2, 1])
    with col1:
        plt.figure(figsize=(6,4))
        plt.plot(t, y, label=titulo, color="#0B6E4F")
        plt.xlabel("Tiempo")
        plt.ylabel("Cantidad")
        plt.title(titulo)
        plt.legend()
        st.pyplot(plt)
    with col2:
        st.image(f"images/{imagen}", caption=titulo)
        st.write(f"**Constante a ingresar:** {explicacion_constante}")
        st.write(f"**Tema de Ecuaciones Diferenciales usado:** {tema}")
        st.write(f"**Conclusión:** {conclusion}")

# ===== CASOS =====
if menu == "1. Consumo de Proteína":
    dosis = st.number_input("💪 Dosis inicial de proteína (g)", min_value=1.0, step=0.5)
    tiempo_total = st.number_input("⏳ Tiempo total (horas)", min_value=1.0, step=0.5)
    k = st.number_input("⚙️ Constante de descomposición (0.1 a 1.0)", min_value=0.1, max_value=1.0, step=0.1)
    if st.button("Simular Consumo de Proteína"):
        t, y = consumo_proteina.simular(dosis, tiempo_total, k)
        mostrar_resultados(
            t, y, "Consumo de Proteína", "proteina.png",
            "k = tasa de absorción o descomposición de la proteína en el cuerpo.",
            "Ecuación diferencial de decaimiento exponencial",
            "La proteína disminuye gradualmente, reflejando el metabolismo natural."
        )

elif menu == "2. Inventario":
    stock_inicial = st.number_input("📦 Inventario inicial (unidades)", min_value=1, step=1)
    demanda = st.number_input("🛒 Demanda diaria (unidades)", min_value=1, step=1)
    dias = st.number_input("⏳ Tiempo total (días)", min_value=1, step=1)
    if st.button("Simular Inventario"):
        t, y = inventario.simular(stock_inicial, demanda, dias)
        mostrar_resultados(
            t, y, "Control de Inventario", "inventario.jpg",
            "Demanda: unidades vendidas por día.",
            "Modelo lineal discreto",
            "El inventario disminuye de forma constante según la demanda."
        )

elif menu == "3. Consumo No Lineal":
    cantidad_inicial = st.number_input("⚡ Cantidad inicial (unidades)", min_value=1.0, step=0.5)
    tiempo_total = st.number_input("⏳ Tiempo total (horas)", min_value=1.0, step=0.5)
    k = st.number_input("⚙️ Constante de consumo no lineal (0.01 a 1.0)", min_value=0.01, max_value=1.0, step=0.01)
    if st.button("Simular Consumo No Lineal"):
        t, y = consumo_nolineal.simular(cantidad_inicial, tiempo_total, k)
        mostrar_resultados(
            t, y, "Consumo No Lineal", "no_lineal.png",
            "k = regula la rapidez de consumo cuando la cantidad es alta o baja.",
            "Ecuación diferencial no lineal",
            "El consumo es más rápido al inicio y se ralentiza con el tiempo."
        )

elif menu == "4. Electrolitos":
    concentracion_inicial = st.number_input("💧 Concentración inicial (mmol/L)", min_value=1.0, step=0.5)
    tiempo_total = st.number_input("⏳ Tiempo total (horas)", min_value=1.0, step=0.5)
    k = st.number_input("⚙️ Constante de equilibrio (0.1 a 1.0)", min_value=0.1, max_value=1.0, step=0.1)
    if st.button("Simular Electrolitos"):
        t, y = electrolitos.simular(concentracion_inicial, k, tiempo_total)
        mostrar_resultados(
            t, y, "Equilibrio de Electrolitos", "electrolitos.png",
            "k = velocidad de regulación hacia un valor de equilibrio.",
            "Ecuación diferencial lineal",
            "La concentración se ajusta hasta alcanzar un nivel estable."
        )

elif menu == "5. Suplementos Acoplados":
    dosis_a = st.number_input("💊 Dosis inicial suplemento A", min_value=1.0, step=0.5)
    dosis_b = st.number_input("💊 Dosis inicial suplemento B", min_value=1.0, step=0.5)
    tiempo_total = st.number_input("⏳ Tiempo total (horas)", min_value=1.0, step=0.5)
    k_a = st.number_input("⚙️ Constante eliminación suplemento A", min_value=0.01, max_value=1.0, step=0.01)
    k_b = st.number_input("⚙️ Constante eliminación suplemento B", min_value=0.01, max_value=1.0, step=0.01)
    if st.button("Simular Suplementos Acoplados"):
        t, y_a, y_b = suplementos_acoplados.simular(dosis_a, dosis_b, tiempo_total, k_a, k_b)
        mostrar_resultados(
            t, y_a, "Suplemento A", "acoplados.png",
            "kA = velocidad de disminución del suplemento A.",
            "Modelo exponencial simple",
            "El suplemento A disminuye progresivamente en el tiempo."
        )
        mostrar_resultados(
            t, y_b, "Suplemento B", "suplemento_b.jpg",
            "kB = velocidad de disminución del suplemento B.",
            "Modelo exponencial simple",
            "El suplemento B disminuye progresivamente en el tiempo."
        )



# ===== FOOTER =====
st.markdown("""
    <div class='footer'>
        Proyecto académico - Fundación Universitaria Compensar
    </div>
""", unsafe_allow_html=True)
