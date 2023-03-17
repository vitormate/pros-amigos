import streamlit as st
import pandas as pd


st.set_page_config(
    page_title='Limpeza', 
    page_icon='random', 
    layout='wide', 
    initial_sidebar_state='auto', 
    menu_items=None
)

antigo_dataset = pd.read_csv('dataset.csv')

st.title('Limpeza do dataset')

st.subheader('Dataset inicial')
st.write(antigo_dataset)

st.markdown('#### Observando a tabela acima vemos que ela poderia ser mais fácil de ser compreendida.')
st.markdown('#### Com esse objetivo faremos as seguintes alterações:')
st.markdown('''
    ###### 1. Colocar os nomes das colunas em português
    ###### 2. Remover colunas que não agregam 
        a. Unnamed: 0 -> Por ser apenas um contador de linhas
        b. Key(Tom) -> Por não sem aplicar as necessidades desse projeto
        c. Mode(Modalidade) -> Devido a sua característica técnica também não se aplicar aqui
    ###### 3. Transformar a unidade de medida da coluna duração de milisegundos para minutos
    ###### 4. Transformar o dataset em um arquivo .parquet para melhorar o desempenho
''')

antigo_dataset = antigo_dataset.rename(columns={
    'track_id':'ID Spotify',
    'explicit':'explicita',
    'track_name':'nome',
    'album_name':'album',
    'artists':'artistas',
    'track_genre':'genero',
    'time_signature':'compasso',
    'tempo':'bpm',
    'valence':'valencia',
    'liveness':'ao vivo',
    'instrumentalness':'instrumental',
    'acousticness':'acustica',
    'speechiness':'falada',
    'loudness':'altura(db)',
    'key':'tom',
    'energy':'energia',
    'danceability':'dancabilidade',
    'duration_ms':'duracao(ms)',
    'popularity':'popularidade',
    'mode':'modalidade',
})

antigo_dataset = antigo_dataset.drop(columns = ['Unnamed: 0', 'tom', 'modalidade'])

# Tentar descobrir como fazer a tabela mostrar só 1 número decimal
antigo_dataset['duracao(ms)'] = round(antigo_dataset['duracao(ms)']/60000, 1)

antigo_dataset = antigo_dataset.rename(columns={'duracao(ms)':'duracao(min)'})

# importando mudanças para .parquet
# new_data.to_parquet('dataset.parquet')
# arquivo em .csv -> 20.1 MB
# arquivo em .parquet -> 8.3 MB


novo_dataset = pd.read_parquet('dataset.parquet')
st.subheader('Dataset após tratamento')
novo_dataset

st.subheader('Quantidade de locais vazios em cada coluna')
soma_de_vazios = novo_dataset.isnull().sum()
soma_de_vazios

st.subheader('Localizando inconsistências')
novo_dataset.loc[pd.isnull(novo_dataset['nome'])]
st.text('''
    Encontramos as 3 inconsistências do nosso dataset, o melhor a se fazer 
    seria preencher as colunas artistas, album e nome a partir da música fornecida
    pelo ID Spotify, porém não existe nenhuma música com esse ID, então tomamos decisão
    de excluir esta linha.
''')

novo_dataset = novo_dataset.drop(65900, axis=0)

st.subheader('Vericando novamente as inconsistências')
soma_de_vazios = novo_dataset.isnull().sum()
soma_de_vazios
# importando novas mudanças para um arquivo .parquet
# novo_dataset.to_parquet('dataset_sem_inconsistencias.parquet')

novo_dataset

df = pd.read_csv('cluster.csv')

df = df.drop(columns = ['Unnamed: 0.1', 
'Unnamed: 0', 
'track_id',
'album_name',
'duration_ms',
'explicit',
'energy',
'key',
'loudness',
'mode',
'speechiness',
'acousticness',
'instrumentalness',
'liveness',
'valence',
'tempo',
'time_signature',
'danceability',
'popularity'])

x = df['cluster'].unique()

x

y = df.loc[df['cluster'] == 0]

y
