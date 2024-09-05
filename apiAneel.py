import requests
import pandas as pd

# URL do arquivo CSV
url = 'https://dadosabertos.aneel.gov.br/dataset/57e4b8b5-a5db-40e6-9901-27ca629d0477/resource/4a615df8-4c25-48fa-bbea-873a36a79518/download/ralie-usina.csv'

# Fazer o download do arquivo CSV
response = requests.get(url)

# Salvar o conteúdo em um arquivo local
with open('ralie-usina.csv', 'wb') as file:
    file.write(response.content)

# Carregar o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv('ralie-usina.csv', delimiter=';', encoding='latin1', low_memory=False)

# Visualizar os dados
print(df.head(2))
