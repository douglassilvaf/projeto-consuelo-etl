import requests
import pandas as pd

# URL do arquivo CSV
url = 'https://dadosabertos.aneel.gov.br/dataset/283a0172-3966-49e7-ae45-d2885ad17b03/resource/20ef769f-a072-489d-9df4-c834529f8a78/download/agentes-geracao-energia-eletrica.csv'

# Fazer o download do arquivo CSV
response = requests.get(url)

csvname = 'agentes-geracao-energia-eletrica.csv'
with open(csvname, 'wb') as file:
    file.write(response.content)

# Carregar o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv(csvname, delimiter=';', encoding='latin1', low_memory=False)

# Visualizar os dados
print(df.head(2))
