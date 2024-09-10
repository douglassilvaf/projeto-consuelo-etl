# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Carregar o arquivo CSV salvo na máquina
# df = pd.read_csv("geracao_usina_por_tipo.csv")

# # Criar um gráfico de barras para visualizar o custo por tipo de energia a cada mês
# plt.figure(figsize=(12, 6))
# sns.barplot(x='MES', y='VALOR_PARA_GERAR', hue='TIPO_DE_USINA', data=df)
# plt.title('Custo por Tipo de Energia a Cada Mês')
# plt.xlabel('Mês')
# plt.ylabel('Custo (VALOR_PARA_GERAR)')
# plt.legend(title='Tipo de Usina')

# # Exibir o gráfico usando Streamlit
# st.write("## Custo por Tipo de Energia a Cada Mês")
# st.pyplot(plt)

# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Carregar o arquivo CSV salvo na máquina
# df = pd.read_csv("geracao_usina_por_tipo.csv")

# # Criar uma lista de tipos de usina únicos
# tipos_de_usina = df['TIPO_DE_USINA'].unique()

# mes_visualizado = df['MES'].unique()

# # Adicionar um filtro de seleção de tipo de usina
# tipo_selecionado = st.multiselect('Selecione o Tipo de Usina', tipos_de_usina, default=tipos_de_usina)

# mes_selecionado = st.multiselect('Selecione o Mês a ser visualizado', mes_visualizado, default=mes_visualizado)

# # Filtrar o DataFrame com base na seleção
# df_filtrado = df[df['TIPO_DE_USINA'].isin(tipo_selecionado) & df['MES'].isin(mes_selecionado)]


# # Criar um gráfico de barras para visualizar o custo por tipo de energia a cada mês
# plt.figure(figsize=(12, 6))
# sns.barplot(x='MES', y='VALOR_PARA_GERAR', hue='TIPO_DE_USINA', data=df_filtrado)
# plt.title('Custo por Tipo de Energia a Cada Mês')
# plt.xlabel('Mês')
# plt.ylabel('Custo (VALOR_PARA_GERAR)')
# plt.legend(title='Tipo de Usina')

# # Exibir o gráfico usando Streamlit
# st.write("## Custo por Tipo de Energia a Cada Mês")
# st.pyplot(plt)

import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

# Carregar o arquivo CSV salvo na máquina
df = pd.read_csv("geracao_usina_por_tipo.csv")

# Criar uma lista de tipos de usina únicos
tipos_de_usina = df['TIPO_DE_USINA'].unique()

# Criar uma lista de meses únicos
mes_visualizado = df['MES'].unique()

# Adicionar um filtro de seleção de tipo de usina
tipo_selecionado = st.multiselect('Selecione o Tipo de Usina', tipos_de_usina, default=tipos_de_usina)

# Adicionar um filtro de seleção de mês
mes_selecionado = st.multiselect('Selecione o Mês a ser visualizado', mes_visualizado, default=mes_visualizado)

# Filtrar o DataFrame com base na seleção
df_filtrado = df[(df['TIPO_DE_USINA'].isin(tipo_selecionado)) & (df['MES'].isin(mes_selecionado))]

# Preparar os dados para o gráfico
data = []
for tipo in tipo_selecionado:
    data.append({
        "name": tipo,
        "type": "bar",
        "data": df_filtrado[df_filtrado['TIPO_DE_USINA'] == tipo]['VALOR_PARA_GERAR'].tolist()
    })

options = {
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {
            "type": "shadow"
        }
    },
    "legend": {
        "data": tipo_selecionado
    },
    "xAxis": {
        "type": "category",
        "data": df_filtrado['MES'].unique().tolist()
    },
    "yAxis": {
        "type": "value"
    },
    "series": data
}

# Exibir o gráfico usando Streamlit e ECharts
st.write("## Custo por Tipo de Energia a Cada Mês")
st_echarts(options=options)
