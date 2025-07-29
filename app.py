import pandas as pd
import plotly.express as px
import streamlit as st

# Cabeçalho do app
st.header('Análise de Vendas de Carros nos EUA')

# Lê o conjunto de dados
car_data = pd.read_csv('vehicles.csv')

# Botão para 
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre preço e ano do carro')
    fig = px.scatter(car_data, x="model_year", y="price", title="Preço vs Ano do Modelo")
    st.plotly_chart(fig, use_container_width=True)
