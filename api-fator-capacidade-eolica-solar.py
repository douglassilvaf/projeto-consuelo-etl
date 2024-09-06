import requests
import pandas as pd
import numpy as np
import io

# URLs dos arquivos CSV
base_url = "https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/fator_capacidade_2_di/FATOR_CAPACIDADE-2_2024_0"
file_urls = [f"{base_url}{i}.csv" for i in range(1, 10)]

# Função para baixar e carregar os dados em um DataFrame
def download_and_load_csv(url):
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
    data = response.content.decode('utf-8')
    df = pd.read_csv(io.StringIO(data))
    return df

# Lista para armazenar os DataFrames
dataframes = []

# Baixando e carregando os dados
for url in file_urls:
    df = download_and_load_csv(url)
    dataframes.append(df)
    print(f"Primeiras 10 linhas do arquivo {url.split('/')[-1]}:")
    print(df.head(10))
    print("\n")

# Concatenando todos os DataFrames em um único DataFrame
all_data = pd.concat(dataframes, ignore_index=True)

# Tratamento de dados (exemplo: conversão de tipos, tratamento de valores ausentes)
all_data.replace('', np.nan, inplace=True)
all_data.dropna(how='all', inplace=True)

# Salvando os dados combinados em um arquivo CSV
all_data.to_csv('dados_fator_capacidade_combinados.csv', index=False)

print("Dados combinados extraídos e salvos em 'dados_fator_capacidade_combinados.csv'")
