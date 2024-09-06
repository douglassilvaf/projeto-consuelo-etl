import requests
import pandas as pd

url = "https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/dados_hidrologicos_di/DADOS_HIDROLOGICOS_RES_2024.xlsx"

response = requests.get(url)
response.raise_for_status()


arquivoNome = 'DADOS_HIDROLOGICOS_RES_2024.xlsx'

with open(arquivoNome, 'wb') as file:
    file.write(response.content)

df = pd.read_excel(arquivoNome)

print('-'*20,'As 10 primeiras linhas','-'*20)
print()
print(df.head(10))

df.to_csv('dados-hidrologicos-res-2024', index=False)
print()
print('-'*20,'Dados salvos com sucesso','-'*20)