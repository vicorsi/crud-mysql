from conectar import conexao, cursor


def inserir_filmes(filme, plano, desc, classif):
    sql = f"""INSERT INTO filmes(filme, plano, descricao, class)
    values
    ('{filme}', '{plano}', '{desc}', {classif});"""
    cursor.execute(sql)
    conexao.commit()


def inserir_usuarios(usuario, email, plano, tipo, idade):
    sql = f"""INSERT INTO usuarios(usuario, email, plano, tipo, idade)
    values
    ('{usuario}', '{email}', '{plano}', '{tipo}', {idade});"""
    cursor.execute(sql)
    conexao.commit()
