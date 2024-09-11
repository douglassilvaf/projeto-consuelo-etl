import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#Carregar o arquivo CSV
df = pd.read_csv("geracao_usina_agrupado.csv")
df = df.drop(columns=['ESTADO', 'REGIAO'])

resultado = df.groupby(['MES', 'TIPO_DE_USINA']).sum().reset_index()

custo_mwh = 67.70

resultado['VALOR_PARA_GERAR_R$'] = (resultado['VALOR_PARA_GERAR'] * custo_mwh)/1000000.00

resultado = resultado.drop(columns=['VALOR_PARA_GERAR'])

print(resultado)

resultado.to_csv("geracao_usina_grafico.csv", index=False)