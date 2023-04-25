from conectar import conexao, cursor


def inserir_filmes(filme,plano, desc, classif):
    inserir_filmes = f"""INSERT INTO filmes(filme, plano, descricao, class)
    values
    ('{filme}', '{plano}', '{desc}', {classif});"""
    cursor.execute(inserir_filmes)
    conexao.commit()


def inserir_usuarios(usuario, email, plano, tipo, idade):
    inserir_usuarios = f"""INSERT INTO usuarios(usuario, email, plano, tipo, idade)
    values
    ('{usuario}', '{email}', '{plano}', '{tipo}', {idade});"""
    cursor.execute(inserir_usuarios)
    conexao.commit()

