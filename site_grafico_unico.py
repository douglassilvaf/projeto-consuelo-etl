import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

# Configurar a página para usar a largura total
st.set_page_config(layout="wide")

# Carregar o arquivo CSV salvo na máquina
df = pd.read_csv("geracao_usina_grafico.csv")

# Substituir valores NaN por 0 ou outro valor apropriado
df.fillna(0, inplace=True)

# Criar uma lista de tipos de usina únicos
tipos_de_usina = df['TIPO_DE_USINA'].unique()

# Criar uma lista de meses únicos
mes_visualizado = df['MES'].unique()

# Adicionar um filtro de seleção de tipo de usina
st.sidebar.write("### Selecione o Tipo de Usina")
tipo_selecionado = st.sidebar.multiselect('Tipos de Usina', tipos_de_usina, default=tipos_de_usina)

# Adicionar um filtro de seleção de mês
st.sidebar.write("### Selecione o Mês a ser visualizado")
mes_selecionado = st.sidebar.multiselect('Meses', mes_visualizado, default=mes_visualizado)

# Filtrar o DataFrame com base na seleção
df_filtrado = df[(df['TIPO_DE_USINA'].isin(tipo_selecionado)) & (df['MES'].isin(mes_selecionado))]

# Preparar os dados para o gráfico
data = []
for tipo in tipo_selecionado:
    tipo_data = df_filtrado[df_filtrado['TIPO_DE_USINA'] == tipo].groupby('MES').sum().reset_index()
    #Garantir que todos os meses estejam presentes, mesmo que com valor 0
    tipo_data = tipo_data.set_index('MES').reindex(mes_visualizado, fill_value=0).reset_index()
    data.append({
        "name": tipo,
        "type": "line", # Alterar o tipo de gráfico para linha
        "data": tipo_data['VALOR_PARA_GERAR_R$'].tolist()
    })

options = {
    "tooltip": {#maneira que os dados serão exibidos ao passar o mouse sobre
        "trigger": "axis",
        "axisPointer": {
            "type": "cross"
        }
    },
    "legend": {
        "data": tipo_selecionado
    },
    "xAxis": {
        "type": "category",
        "data": sorted(mes_visualizado.tolist())
    },
    "yAxis": {
        "type": "value"
    },
    "series": data
}

# Exibir o gráfico usando Streamlit e ECharts
st.write("## Custo por Tipo de Energia a Cada Mês")
st_echarts(options=options, height="600px")  # Aumentar a altura do gráfico
