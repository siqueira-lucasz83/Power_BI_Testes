import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="*pessoal*",
    database="*pessoal*"
)

print("conectado")

conexao.close()