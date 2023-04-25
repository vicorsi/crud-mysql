from conectar import conexao, cursor


def del_usuario(idUser):
    sql = f"""DELETE FROM usuarios WHERE idUsuario = '{idUser}';"""
    cursor.execute(sql)
    conexao.commit()


def del_filme(idFilme):
    sql = f"""DELETE FROM filmes WHERE idFilme = '{idFilme}';"""
    cursor.execute(sql)
    conexao.commit()
