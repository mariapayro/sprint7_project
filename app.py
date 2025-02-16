import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la app
st.header('Análisis de Datos de Vehículos')

# Botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma de kilometraje (odometer)
    fig = px.histogram(car_data, x="odometer", title="Distribución del kilometraje de los vehículos")

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para analizar precio vs. kilometraje')

    # Crear scatter plot (precio vs. kilometraje)
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="condition",
                             title="Relación entre kilometraje y precio",
                             labels={"odometer": "Kilometraje", "price": "Precio (USD)"})

    # Mostrar gráfico en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)


# Casilla de verificación para mostrar el diagrama de cajas
show_boxplot = st.checkbox('Mostrar diagrama de cajas de precios por tipo de vehículo')

# Mostrar box plot si se selecciona la casilla
if show_boxplot:
    st.write('Distribución de precios por tipo de vehículo')

    fig_box = px.box(car_data, x="type", y="price", color="type",
                     title="Distribución de precios por tipo de vehículo")
    st.plotly_chart(fig_box, use_container_width=True)

