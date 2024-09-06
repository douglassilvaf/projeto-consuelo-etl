import requests
import pandas as pd

# URL do arquivo Excel
url = "https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/carga_energia_di/CARGA_ENERGIA_2024.xlsx"

# Fazendo a requisição para baixar o arquivo
response = requests.get(url)
response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

# Salvando o conteúdo do arquivo em um arquivo local
with open('CARGA_ENERGIA_2024.xlsx', 'wb') as file:
    file.write(response.content)

# Carregando o arquivo Excel em um DataFrame
df = pd.read_excel('CARGA_ENERGIA_2024.xlsx')

# Imprimindo as 10 primeiras linhas para verificação
print("Primeiras 10 linhas do DataFrame:")
print(df.head(10))

# Salvando os dados em um arquivo CSV (opcional)
df.to_csv('carga-energia.csv', index=False)

print("Dados extraídos e salvos em 'carga-energia.csv'")
