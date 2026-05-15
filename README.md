# Proyecto Streamlit - Casos de Estudio

Esta es una aplicación interactiva desarrollada en **Python** con **Streamlit** para visualizar y gestionar casos de estudio.  
Cuenta con una interfaz personalizada con colores verde y azul, y elementos gráficos adaptados.

## 📌 Características
- Botones verdes personalizados.
- Encabezados y pie de página con fondo azul.
- Radio buttons con puntos de selección en verde.
- Diseño adaptado para una experiencia visual agradable.

## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/proyecto-streamlit.git
   cd proyecto-streamlit
   
Instala las dependencias:
pip install -r requirements.txt

Ejecuta la aplicación:
python -m streamlit run app.py

📂 Estructura del Proyecto
DIFFEQ_FITNESS/
│
├── app.py              # Código principal de la aplicación
├── models.py           # Funciones y modelos usados
├── requirements.txt    # Dependencias
├── README.md           # Documentación
└── images/             # Carpeta con imágenes usadas

🖌 Personalización
Los estilos CSS personalizados están incluidos en app.py usando st.markdown con HTML y CSS.
Ejemplo de personalización de radio buttons:

div[role='radiogroup'] > label > div:first-child {
    background-color: white;
    border: 2px solid #6B8E23;
}

📄 Licencia
Este proyecto se distribuye bajo la licencia MIT.