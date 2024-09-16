import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo CSV salvo na máquina
df = pd.read_csv("geracao_usina_por_tipo.csv")

# Criar um gráfico de barras para visualizar o custo por tipo de energia a cada mês
plt.figure(figsize=(12, 6))
sns.barplot(x='MES', y='VALOR_PARA_GERAR', hue='TIPO_DE_USINA', data=df)
plt.title('Custo por Tipo de Energia a Cada Mês')
plt.xlabel('Mês')
plt.ylabel('Custo (VALOR_PARA_GERAR)')
plt.legend(title='Tipo de Usina')

# Exibir o gráfico usando Streamlit
st.write("## Custo por Tipo de Energia a Cada Mês")
st.pyplot(plt.gcf())  # Use plt.gcf() para obter a figura atual
