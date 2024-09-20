---

# Análise de Dados de Energia Renovável - Projeto ETL com Visualização

## Descrição do Projeto

Este projeto foi desenvolvido com o objetivo principal de realizar o processo de **Extração, Transformação e Carregamento (ETL)** de dados relacionados à geração e consumo de energia renovável. Posteriormente, foi estendida a funcionalidade de visualização dos dados através de um site criado com **Streamlit**. Os dados foram obtidos a partir de fontes abertas fornecidas pelo ONS (Operador Nacional do Sistema Elétrico) e processados para permitir análises mais eficientes e uma visualização clara dos resultados.

## Funcionalidades Principais

- **ETL Completo**: Extração de dados brutos, tratamento e carregamento em banco de dados AWS.
- **Conversão de MWH para R$**: Implementada para facilitar a compreensão dos custos energéticos.
- **Criação de Coluna 'Mês'**: Adicionada manualmente para facilitar a análise temporal dos dados.
- **Visualização Gráfica**: Implementada via Streamlit com gráficos interativos utilizando a biblioteca `streamlit_echarts`.
- **Redução Significativa de Dados**: A partir de 4.046.233 linhas e 13 colunas para 41 linhas e 4 colunas após limpeza e tratamento.

## Resultados

- Após a extração inicial, os dados consistiam de **4.046.233 linhas** e **13 colunas**.
- Após o processo de tratamento, os dados foram reduzidos para **742 linhas** e **5 colunas**.
- Para a visualização, as colunas "estado" e "região" foram descartadas, resultando em uma tabela final de **41 linhas** e **4 colunas** com a adição de uma nova coluna calculada em partes por milhão (ppm).

## Tecnologias Utilizadas

- **Python** para processamento de dados.
- **Streamlit** para criação de interface web interativa.
- **Bibliotecas Usadas**:
  - `requests`: Para download de dados via HTTP.
  - `urllib3`: Desabilitação de avisos de certificados SSL.
  - `pandas`: Manipulação e transformação de dados.
  - `io`: Conversão de texto para arquivos manipuláveis com `pandas`.
  - `boto3`: Usada para se conectar ao Amazon S3 e realizar o upload do arquivo especificado para o bucket escolhido..
  - `streamlit`: Interface de visualização dos dados.
  - `streamlit_echarts`: Criação de gráficos dinâmicos e interativos.

## Instalação

### Pré-requisitos

Certifique-se de ter o **Python 3.8** ou superior instalado. Instale as dependências necessárias executando o seguinte comando:

```bash
pip install requests urllib3 pandas streamlit streamlit_echarts
```

### Como Executar o Projeto

1. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/seu_usuario/projeto-energia-renovavel.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd projeto-energia-renovavel
   ```
3. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```

4. Acesse o site local gerado pelo Streamlit através do endereço `http://localhost:8501` no seu navegador.

Se o seu projeto está dividido em vários códigos separados para cada etapa, isso deve ser refletido no **README** para que os usuários entendam como cada parte funciona individualmente e como elas se conectam. Aqui está como você pode ajustar a seção "Estrutura do Projeto" para destacar isso:

---

## Estrutura do Projeto

O projeto está organizado em **múltiplos scripts**, onde cada etapa do processo de ETL e visualização dos dados é separada em um arquivo Python distinto:

- [EXTRAÇÃO](https://github.com/douglassilvaf/projeto-consuelo-etl/blob/main/projetoETL.py) Responsável pela **extração** dos dados brutos a partir das fontes fornecidas.
- [TRATAMENTO](https://github.com/douglassilvaf/projeto-consuelo-etl/blob/main/ProjetoETL-agrupamento.py): Realiza o **tratamento** dos dados, incluindo limpeza, padronização de colunas.
- [TRATAMENTO FINAL](https://github.com/douglassilvaf/projeto-consuelo-etl/blob/main/PETLA-GRAFICO.py): Realiza o **tratamento** dos dados, criando colunas calculadas, como a conversão de MWH para R$.
- [CARREGAMENTO](https://github.com/douglassilvaf/projeto-consuelo-etl/blob/main/carregamentoETL.py): Implementa a fase de **carregamento** dos dados tratados para o banco de dados AWS.
- [VISUALIZAÇÃO](https://github.com/douglassilvaf/projeto-consuelo-etl/blob/main/site_conjunto_de_graficos.py): Script que gera a interface visual e **exibe gráficos interativos** utilizando `streamlit` e `streamlit_echarts`.

Os scripts podem ser executados individualmente conforme a necessidade, seguindo a ordem de **extração**, **tratamento**, **tratamento final**, **carregamento** e, por fim, **visualização**.

### Como Executar Cada Etapa

1. **Extração de Dados**:
   ```bash
   python projetoETL.py
   ```
2. **Tratamento dos Dados**:
   ```bash
   python ProjetoETL-agrupamento.py
   ```
2. **Tratamento Final**:
   ```bash
   python PETLA-grafico.py
   ```
3. **Carregamento dos Dados para AWS**:
   ```bash
   python carregamentoETL.py
   ```
4. **Visualização dos Dados**:
   ```bash
   streamlit run site_conjunto_de_grafico.py
   ```

---

## Uso das Bibliotecas

1. **`requests`**: Realiza download de arquivos CSV diretamente das fontes de dados com o método `requests.get()`.
2. **`urllib3`**: Desativa os avisos de verificação SSL usando `urllib3.disable_warnings()`.
3. **`pandas`**: Manipula e transforma os dados, realizando operações de leitura, limpeza e agregação.
4. **`io`**: Converte o texto baixado em um formato de arquivo manipulável por `pandas`.
5. **`streamlit`**: Cria a interface web para a visualização interativa dos dados.
6. **`streamlit_echarts`**: Gera gráficos dinâmicos e interativos para visualização dos dados.

## Considerações Finais

Este projeto demonstra como trabalhar com grandes volumes de dados de energia renovável, realizando a conversão de valores, tratamento de dados brutos e visualização dos resultados em uma interface web simples e intuitiva.

## Links Úteis

- [Repositório no GitHub](https://github.com/seu_usuario/projeto-energia-renovavel) - Acesse o código-fonte completo deste projeto.

---
