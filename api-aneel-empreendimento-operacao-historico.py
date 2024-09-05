import requests
import pandas as pd

# URL do arquivo CSV
url = 'https://dadosabertos.aneel.gov.br/dataset/306a6fdb-beb9-4296-bf18-77fa0e076ef1/resource/e61fd029-5e78-43be-bed4-873b7b11f04c/download/empreendimento-operacao-historico.csv'

# Fazer o download do arquivo CSV
response = requests.get(url)

csvname = 'empreendimento-operacao-historico.csv'
with open(csvname, 'wb') as file:
    file.write(response.content)

# Carregar o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv(csvname, delimiter=';', encoding='latin1', low_memory=False)

# Visualizar os dados
print(df.head(2))
