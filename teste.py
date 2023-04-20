import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='netflix',
    user='root',
    password=''
)

filme = input('Filme: ')
plano = input('Plano: ')
desc = input('Descrição: ')
classif = input('Classificação: ')

frase = """INSERT INTO filmes(filme, plano, descricao, class) values ("""

inserir_filmes = frase + f'"{filme}", "{plano}", "{desc}", {classif}'""");"""
print(inserir_filmes)

cursor = conexao.cursor()
cursor.execute(inserir_filmes)
conexao.commit()

sql = 'SELECT * from filmes'
cursor.execute(sql)
linhas = cursor.fetchall()

for i in linhas:
    print(i[0], end='\t')
    print(i[1], ' ' * (10 - len(i[1])), end='\t')
    print(i[2], ' ' * (20 - len(i[2])), end='\t')
    print(i[3], ' ' * (10 - len(i[3])), end='\t')
    print(i[4])