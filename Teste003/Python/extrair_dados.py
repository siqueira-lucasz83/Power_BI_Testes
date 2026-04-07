import mysql.connector
import pandas as pd

# conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*pessoal*",
    database="*pessoal*"
)

# query
query = "SELECT * FROM vendas_carros"

df = pd.read_sql(query, conexao)

# fechar conexão
conexao.close()

# ----------------------------
# LIMPEZA E TRANSFORMAÇÃO
# ----------------------------

# 1. Converter data
df['data_venda'] = pd.to_datetime(df['data_venda'])

# 2. Criar coluna de mês
df['mes'] = df['data_venda'].dt.month

# 3. Criar coluna de ano da venda
df['ano_venda'] = df['data_venda'].dt.year

# 4. Padronizar texto (exemplo)
df['marca'] = df['marca'].str.upper()

# 5. Verificar dados nulos
print(df.isnull().sum())

# 6. Visual final
print(df.head())

# após testar, adicionei a parte exportação para .csv

# ----------------------------
# EXPORTAR PARA CSV
# ----------------------------

df.to_csv('vendas_tratadas.csv', index=False, encoding='utf-8-sig')

print("Arquivo csv ok")