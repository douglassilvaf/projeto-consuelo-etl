import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Carregar o arquivo CSV
df = pd.read_csv("geracao_usina_agrupado.csv")
df = df.drop(columns=['ESTADO', 'REGIAO'])

df['MES'] = df['MES'].astype(str)

# Agrupar os dados por 'MES' e 'TIPO_DE_USINA' e somar os valores
resultado = df.groupby(['MES', 'TIPO_DE_USINA']).sum().reset_index()

# Definir o custo por MWh
custo_mwh = 67.70

# Calcular o valor para gerar em milhões de reais
resultado['VALOR_PARA_GERAR_R$'] = (resultado['VALOR_PARA_GERAR'] * custo_mwh) / 1000000.00

# Arredondar os valores na coluna 'VALOR_PARA_GERAR_R$' para 2 casas decimais
resultado['VALOR_PARA_GERAR_R$'] = resultado['VALOR_PARA_GERAR_R$'].round(2)

# Remover a coluna 'VALOR_PARA_GERAR'
resultado = resultado.drop(columns=['VALOR_PARA_GERAR'])

# Remover linhas onde a coluna 'MES' tem o valor '9'
resultado = resultado[resultado['MES'] != '9']

# Exibir o DataFrame resultado
print(resultado)

# Salvar o DataFrame resultado em um novo arquivo CSV
resultado.to_csv("geracao_usina_grafico.csv", index=False)
