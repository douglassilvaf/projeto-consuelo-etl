import requests
import urllib3
import pandas as pd
import io

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URLs dos arquivos CSV
base_url = "https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/geracao_usina_2_ho/GERACAO_USINA-2_2024_0"
file_urls = [f"{base_url}{i}.csv" for i in range(1, 9)]

def download_and_load_csv(url):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    data = response.content.decode('utf-8')
    df = pd.read_csv(io.StringIO(data), sep=';')
    mes = url.split('/')[-1].split('.')[0][-1]
    df['MES'] = mes
    print(df.head(2))
    print()
    return df

dataframes = []
for url in file_urls:
    df = download_and_load_csv(url)
    dataframes.append(df)

for arquivo in dataframes:
    arquivo.columns = arquivo.columns.str.upper()

all_data = pd.concat(dataframes, ignore_index=True)

# Modificar o DataFrame conforme necessário
all_data = all_data.drop(columns=['DIN_INSTANTE', 'ID_SUBSISTEMA', 'ID_ESTADO', 'COD_MODALIDADEOPERACAO', 'NOM_TIPOCOMBUSTIVEL', 'ID_ONS', 'CEG'])
all_data = all_data.rename(columns={
    'NOM_SUBSISTEMA': 'REGIAO',
    'NOM_ESTADO': 'ESTADO',
    'NOM_TIPOUSINA': 'TIPO_DE_USINA',
    'VAL_GERACAO': 'VALOR_PARA_GERAR'
})
all_data = all_data[['MES', 'ESTADO', 'REGIAO', 'TIPO_DE_USINA', 'VALOR_PARA_GERAR']]

# Salvar o DataFrame modificado em um novo arquivo CSV
all_data.to_csv('geracao_usina_por_tipo.csv', index=False)

# Imprimir as primeiras 10 linhas do DataFrame modificado
print(all_data.head(10))
