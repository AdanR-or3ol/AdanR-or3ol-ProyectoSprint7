import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el dataset
df = pd.read_csv("train.csv")

# Encabezado de la aplicación
st.header("Análisis Exploratorio de Datos de Vehículos")

# Botón para construir un histograma
if st.button("Construir Histograma"):
    st.write("Histograma de la columna 'clock_speed'")
    if 'clock_speed' in df.columns:
        fig = px.histogram(df, x='clock_speed', title='Histograma de Velocidad del Reloj')
    else:
        fig = px.histogram(df, x=df.columns[0], title=f'Histograma de {df.columns[0]}')
    fig.show()
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
if st.button("Construir Scatter Plot"):
    st.write("Gráfico de dispersión: Poder de Bateria vs Watts Mobile")
    if 'battery_power' in df.columns and 'mobile_wt' in df.columns:
        fig2 = px.scatter(df, x='battery_power', y='mobile_wt', title='Poder de la Bateria vs Watts')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("Las columnas necesarias para el scatter plot no están disponibles.")