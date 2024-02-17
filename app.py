import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Graficos Utiles para el df vehicles_us.csv')
st.subheader("Visualizador de datos")

st.write("Estamos trabajando con un dataframe con datos de carros en venta, el df contiene información del estado del carro, modelo, color y otras cosas")

data_visualizer = st.button("Visualizar datos")

if data_visualizer:
    car_data

    st.write("El dataframe contiene datos de mas de 50000 carros")

st.divider()

st.subheader("Selecciona los gráficos:")

build_histogram = st.checkbox('Precios(histograma)')

build_disper = st.checkbox('Precio vs Kilometraje')

build_disper_2 = st.checkbox('Precio vs días desde la publicación')

st.divider()

hist_button = st.button('Comenzar') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    if build_histogram:    
        st.subheader("Histograma de precios")
        fig = px.histogram(car_data, x="price", range_x=[0,100000]) # crear un histograma
        
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)

    if build_disper:
        st.subheader("Precio vs Kilometraje")
        fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
        st.plotly_chart(fig, use_container_width=True)

    if build_disper_2:
        st.subheader("Precio vs días en venta")
        fig = px.scatter(car_data, x="days_listed", y="price") # crear un gráfico de dispersión
        
        st.plotly_chart(fig, use_container_width=True)
    