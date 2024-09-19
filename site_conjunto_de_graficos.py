import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts

# Configurar a página para usar a largura total, título e ícone
st.set_page_config(
    page_title="Dashboard de Geração de Energia",
    page_icon="🔋",  # Você pode usar um emoji ou o caminho para um arquivo .ico
    layout="wide"
)

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

# Função para criar gráficos de linha
def create_line_chart(df, tipo_usina, color):
    data = df[df['TIPO_DE_USINA'] == tipo_usina]
    if data.empty:
        st.write(f"Sem dados para {tipo_usina}")
        return
    options = {
        "xAxis": {"type": "category", "data": data['MES'].tolist()},
        "yAxis": {"type": "value", "name": "Milhões de R$"},
        "series": [{
            "data": data['VALOR_PARA_GERAR_R$'].tolist(),
            "type": "line",
            "color": color
        }]
    }
    st_echarts(options=options, height="400px")

# Função para criar gráfico de linha empilhado
def create_stacked_line_chart(df):
    types = df['TIPO_DE_USINA'].unique()
    series = []
    for tipo in types:
        data = df[df['TIPO_DE_USINA'] == tipo]
        series.append({
            "name": tipo,
            "type": "line",
            "stack": "total",
            "data": data['VALOR_PARA_GERAR_R$'].tolist()
        })
    options = {
        "tooltip": {  # maneira que os dados serão exibidos ao passar o mouse sobre
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },
        "xAxis": {"type": "category", "data": df['MES'].unique().tolist()},
        "yAxis": {"type": "value", "name": "Milhões de R$"},
        "series": series
    }
    st_echarts(options=options, height="400px")

# Função para criar gráficos de barras
def create_bar_chart(df):
    grouped_data = df.groupby('MES')['VALOR_PARA_GERAR_R$'].sum().reset_index()
    options = {
        "xAxis": {"type": "category", "data": grouped_data['MES'].tolist()},
        "yAxis": {"type": "value", "name": "Milhões de R$"},
        "series": [{
            "data": grouped_data['VALOR_PARA_GERAR_R$'].tolist(),
            "type": "bar"
        }]
    }
    st_echarts(options=options, height="400px")

# Função para criar gráfico de barras agrupado
def create_grouped_bar_chart(df):
    types = df['TIPO_DE_USINA'].unique()
    colors = {
        'EOLIELÉTRICA': 'rgb(0, 100, 0)',
        'FOTOVOLTAICA': 'rgb(255, 255, 0)',
        'HIDROELÉTRICA': 'rgb(0, 0, 255)',
        'NUCLEAR': 'rgb(255, 0, 0)',
        'TÉRMICA': 'rgb(255, 165, 0)'
    }
    series = []
    for tipo in types:
        data = df[df['TIPO_DE_USINA'] == tipo]
        series.append({
            "name": tipo,
            "type": "bar",
            "data": data.set_index('MES').reindex(mes_visualizado, fill_value=0)['VALOR_PARA_GERAR_R$'].tolist(),
            "itemStyle": {"color": colors.get(tipo, 'rgb(0, 0, 0)')}
        })
    options = {
        "tooltip": {  # maneira que os dados serão exibidos ao passar o mouse sobre
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },
        "xAxis": {"type": "category", "data": df['MES'].unique().tolist()},
        "yAxis": {"type": "value", "name": "Milhões de R$"},
        "series": series
    }
    st_echarts(options=options, height="400px")

# Função para criar gráfico de área
def create_area_chart(df):
    types = df['TIPO_DE_USINA'].unique()
    series = []
    for tipo in types:
        data = df[df['TIPO_DE_USINA'] == tipo]
        series.append({
            "name": tipo,
            "type": "line",
            "stack": "total",
            "areaStyle": {},
            "data": data['VALOR_PARA_GERAR_R$'].tolist()
        })
    options = {
        "tooltip": {  # maneira que os dados serão exibidos ao passar o mouse sobre
            "trigger": "axis",
            "axisPointer": {
                "type": "cross"
            }
        },
        "xAxis": {"type": "category", "data": df['MES'].unique().tolist()},
        "yAxis": {"type": "value", "name": "Milhões de R$"},
        "series": series
    }
    st_echarts(options=options, height="400px")


# Função para carregar e filtrar a tabela geracao_usina_agrupado.csv
def load_and_filter_table():
    # Carregar o arquivo CSV salvo na máquina
    df_agrupado = pd.read_csv("geracao_usina_agrupado.csv")
    
    # Substituir valores NaN por 0 ou outro valor apropriado
    df_agrupado.fillna(0, inplace=True)
    
    # Exibir a tabela filtrada
    st.write("## Tabela de Geração de Energia")
    st.dataframe(df_agrupado, height=500, width=2000)

# Layout do Streamlit
st.title("Dashboard de Geração de Energia")

st.markdown("<h2 style='color: rgb(0, 100, 0);'>Gráficos de Linha Eolielétrica</h2>", unsafe_allow_html=True)
create_line_chart(df_filtrado, 'EOLIELÉTRICA', 'rgb(0, 100, 0)')

st.markdown("<h2 style='color: rgb(0, 0, 255);'>Gráficos de Linha Hidroelétrica</h2>", unsafe_allow_html=True)
create_line_chart(df_filtrado, 'HIDROELÉTRICA', 'rgb(0, 0, 255)')

st.markdown("<h2 style='color: rgb(255, 0, 0);'>Gráficos de Linha Nuclear</h2>", unsafe_allow_html=True)
create_line_chart(df_filtrado, 'NUCLEAR', 'rgb(255, 0, 0)')

st.markdown("<h2 style='color: rgb(255, 165, 0);'>Gráficos de Linha Térmica</h2>", unsafe_allow_html=True)
create_line_chart(df_filtrado, 'TÉRMICA', 'rgb(255, 165, 0)')

st.markdown("<h2 style='color: rgb(255, 255, 0);'>Gráficos de Linha Fotovoltaica</h2>", unsafe_allow_html=True)
create_line_chart(df_filtrado, 'FOTOVOLTAICA', 'rgb(255, 255, 0)')

st.header("Gráfico de Linha Empilhado")
create_stacked_line_chart(df_filtrado)

st.header("Gráficos de Barras com valor Total")
create_bar_chart(df_filtrado)
st.header("Gráficos de Barras com valor individual")
create_grouped_bar_chart(df_filtrado)

st.header("Gráfico de Área")
create_area_chart(df_filtrado)

load_and_filter_table()
