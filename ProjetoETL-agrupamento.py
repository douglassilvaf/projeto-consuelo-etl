import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("geracao_usina_por_tipo.csv")

# Substituir valores NaN por 0 ou outro valor apropriado
df.fillna(0, inplace=True)

# Agrupar os dados por 'MES', 'ESTADO', 'REGIAO', e 'TIPO_DE_USINA' e somar os valores de 'VALOR_PARA_GERAR'
df_agrupado = df.groupby(['MES', 'ESTADO', 'REGIAO', 'TIPO_DE_USINA'])['VALOR_PARA_GERAR'].sum().reset_index()

# Salvar o novo DataFrame em um novo arquivo CSV
df_agrupado.to_csv("geracao_usina_agrupado.csv", index=False)

print("Novo arquivo CSV criado com sucesso: geracao_usina_agrupado.csv")