import requests
import pandas as pd

# URL do arquivo CSV
url = 'https://dadosabertos.aneel.gov.br/dataset/6d90b77c-c5f5-4d81-bdec-7bc619494bb9/resource/11ec447d-698d-4ab8-977f-b424d5deee6a/download/siga-empreendimentos-geracao.csv'

# Fazer o download do arquivo CSV
response = requests.get(url)

csvname = 'siga-empreendimento-geracao.csv'
with open(csvname, 'wb') as file:
    file.write(response.content)

# Carregar o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv(csvname, delimiter=';', encoding='latin1', low_memory=False)

# Visualizar os dados
print(df.head(2))
