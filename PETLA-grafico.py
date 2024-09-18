import pandas as pd
import csv

# Carregar o arquivo CSV
df = pd.read_csv("geracao_usina_agrupado.csv")
df = df.drop(columns=['ESTADO', 'REGIAO'])

df['MES'] = df['MES'].astype(str)

# Agrupar os dados por 'MES' e 'TIPO_DE_USINA' e somar os valores
resultado = df.groupby(['MES', 'TIPO_DE_USINA']).sum().reset_index()

# Definir o custo por MWh
custo_mwh = 67.70

resultado['VALOR_PARA_GERAR_R$'] = (resultado['VALOR_PARA_GERAR'] * custo_mwh)/1000000.00
# Remover linhas onde a coluna 'MES' tem o valor '9'
resultado = resultado[resultado['MES'] != '9']

# Exibir o DataFrame resultado
print(resultado)

# Salvar o DataFrame resultado em um novo arquivo CSV
resultado.to_csv("geracao_usina_grafico.csv", index=False)

# Função para contar o número de linhas e colunas em um arquivo CSV
def contar_linhas_colunas(nome_arquivo):
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        linhas = list(leitor_csv)
        num_linhas = len(linhas)
        num_colunas = len(linhas[0]) if num_linhas > 0 else 0
        return num_linhas, num_colunas

# Nome do arquivo CSV
nome_arquivo = 'geracao_usina_grafico.csv'

# Contar linhas e colunas
linhas, colunas = contar_linhas_colunas(nome_arquivo)

# Imprimir o resultado
print(f'O arquivo {nome_arquivo} tem {linhas} linhas e {colunas} colunas.')