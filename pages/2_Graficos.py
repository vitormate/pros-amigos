import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config(
    page_title='Analises', 
    page_icon='random', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

st.title('Analise Preliminares')

nd = pd.read_parquet('dataset_sem_inconsistencias.parquet')

# Esse comando deixa o carregamento muito lento
# media = nd.mean(numeric_only=True)

st.sidebar.title('Barra lateral')
st.sidebar.subheader('Gráfico de Barra Horizontal 1: ')
eixo_x_barra_horizontal_1 = st.sidebar.selectbox(
    'Eixo X - gráfico de barra horizontal 1', (
        'popularidade',
        'duracao(min)',
        'explicita' ,
        'dancabilidade',
        'energia',
        'altura(db)',
        'falada',
        'acustica',
        'instrumental',
        'ao vivo',
        'valencia',
        'bpm',
        'compasso',
    ))

st.sidebar.subheader('Gráfico de Barra Horizontal 2: ')
eixo_y_barra_horizontal_2 = st.sidebar.selectbox(
    'Eixo Y - gráfico de barra horizontal 2', (
        'artistas',
        'album',
        'nome',
        'genero',
    ))

eixo_x_barra_horizontal_2 = st.sidebar.selectbox(
    'Eixo X - gráfico de barra horizontal 2', (
        'popularidade',
        'duracao(min)',
        'explicita' ,
        'dancabilidade',
        'energia',
        'altura(db)',
        'falada',
        'acustica',
        'instrumental',
        'ao vivo',
        'valencia',
        'bpm',
        'compasso',
    ))

# Gráfico de Barra Horizontal
# figsize=(horizontal, vertical) respectivamente
# fig, ax = plt.subplots(figsize=(10, 5))
# genero = ['Comédia', 'Ação', 'Romance', 'Drama', 'SciFi']
# qtde = [30, 20, 40, 15, 25]

# ax.barh(genero, qtde, height=1, color=['purple', 'green'], edgecolor='white', linewidth=3)
# ax.set_title('Gráfico de Filmes', fontsize='16')
# ax.set_xlabel('Notas', fontsize='12')
# ax.set_ylabel('Gêneros', fontsize='12')
# st.pyplot(fig)

# Gráfico de Barra Vertical
# fig, ax = plt.subplots()
# genero = ['Comédia', 'Ação', 'Romance', 'Drama', 'SciFi']
# qtde = [30, 20, 40, 15, 25]

# ax.bar(genero, qtde, width=1, color=['purple', 'green'], edgecolor='white', linewidth=3)
# st.pyplot(fig)

# Gráfico de Linha
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 10, 50]
# fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
# ax.plot(x, y)
# st.pyplot(fig)

st.subheader('Gráfico de Barra Horizontal 1')
st.bar_chart(data=nd, x=eixo_x_barra_horizontal_1, y='genero')


st.subheader('Gráfico de Barra Horizontal 2')
tamanho = len(nd[eixo_y_barra_horizontal_2])
eixo_y = []
eixo_x = []
for i in range(10):
    z = random.randint(0, tamanho-1)

    eixo_y.append(nd[eixo_y_barra_horizontal_2][z])
    eixo_x.append(nd[eixo_x_barra_horizontal_2][z])

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(eixo_y, eixo_x)
st.pyplot(fig)

eixo_y

tamanho
