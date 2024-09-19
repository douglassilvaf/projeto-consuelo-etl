import pandas as pd
import csv

# Carregar o arquivo CSV
df = pd.read_csv("geracao_usina_agrupado.csv")
df = df.drop(columns=['ESTADO', 'REGIAO'])

df['MES'] = df['MES'].astype(str)

# Agrupar os dados por 'MES' e 'TIPO_DE_USINA' e somar os valores
resultado = df.groupby(['MES', 'TIPO_DE_USINA']).sum().reset_index()

# Definir o custo por MWh
custo_mwh = 67.70

resultado['VALOR_PARA_GERAR_R$'] = (resultado['VALOR_PARA_GERAR'] * custo_mwh)/1000000.00
# Remover linhas onde a coluna 'MES' tem o valor '9'
resultado = resultado[resultado['MES'] != '9']

# Exibir o DataFrame resultado
print(resultado)

# Salvar o DataFrame resultado em um novo arquivo CSV
resultado.to_csv("geracao_usina_grafico.csv", index=False)