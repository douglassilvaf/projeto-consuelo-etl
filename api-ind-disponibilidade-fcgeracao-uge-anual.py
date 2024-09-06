import requests
import pandas as pd

# URL do arquivo Excel
url = "https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/ind_disponibilidade_fgeracao_uge_an/IND_DISPONIBILIDADE_FCGERACAO_UGE_ANUAL.xlsx"

# Fazendo a requisição para baixar o arquivo
response = requests.get(url)
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

# Salvando o conteúdo do arquivo em um arquivo local
with open('IND_DISPONIBILIDADE_FCGERACAO_UGE_ANUAL.xlsx', 'wb') as file:
    file.write(response.content)

# Carregando o arquivo Excel em um DataFrame
df = pd.read_excel('IND_DISPONIBILIDADE_FCGERACAO_UGE_ANUAL.xlsx')

# Imprimindo as 10 primeiras linhas para verificação
print("Primeiras 10 linhas do DataFrame:")
print(df.head(10))

# Salvando os dados em um arquivo CSV (opcional)
df.to_csv('dados_disponibilidade_geracao.csv', index=False)

print("Dados extraídos e salvos em 'dados_disponibilidade_geracao.csv'")
