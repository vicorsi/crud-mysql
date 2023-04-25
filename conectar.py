import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='netflix',
    user='root',
    password=''
)

cursor = conexao.cursor()
cursor.execute('select database();')
cursor.fetchone()
