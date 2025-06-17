import streamlit as st
import pandas as pd 
import plotly.express as px

# Encabezado principal
st.header('Cuadro de mandos de anuncios de vehiculos en USA')

# Cargar los datos desde el CSV 
def load_data():
    df = pd.read_csv("../vehicles_us.csv")
    return df

car_data = load_data()

# Mostrar una vista previa 
st.subheader("Vista previa de los datos")
st.write(car_data.head())

# Botón para mostrar histograma 
hist_button = st.button("Construir histograma de odómetro")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de ventas de coches")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para mostrar gráfico de dispersión 
scatter_button = st.button("Construir gráfico de dispersión: odómetro vs precio")

if scatter_button:
    st.write('Gráfico de dispersión entre el kilometraje (odómetro) y el precio del vehículo')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)