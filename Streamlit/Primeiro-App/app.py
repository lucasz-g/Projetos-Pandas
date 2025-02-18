import streamlit as st
import pandas as pd
import plotly.express as px

st.title('File Reader')

st.text('Esse é um app que retorna informações sobre gotas cortadas.')

arquivo = st.file_uploader('Faça o upload do seu arquivo.')

if arquivo:
    st.header('Data Statistics')

    df = pd.read_csv(arquivo, encoding='UTF-8')
    st.write(df.describe().round(2))

    st.header('Data Header')
    st.write(df.head())

    fig = px.scatter(df, x='Comprimento médio (mm)', y='Diâmetro',
                     labels={'x': 'Comprimento médio', 'y': 'Diâmetro'},
                     title='Dispersão entre Comprimento médio e Diâmetro')

    st.plotly_chart(fig)
