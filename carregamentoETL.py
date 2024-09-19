import boto3

# Defina suas credenciais diretamente ou configure no AWS CLI/configuração de ambiente
aws_access_key_id = 'sua_chave_de_acesso_aws'
aws_secret_access_key = 'sua_chave_secreta_aws'

# Crie um cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Faça o upload do arquivo
s3.upload_file(
    Filename='geracao_usina_por_tipo.csv',
    Bucket='projeto-etl-consuelo',
    Key='geracao_usina_por_tipo.csv'
)

print("Upload realizado com sucesso!")
