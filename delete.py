from conectar import conexao, cursor


def dt_usuario(idUser):
    sql = f"""DELETE FROM usuarios WHERE idUsuario = '{idUser}';"""
    cursor.execute(sql)
    conexao.commit()


def dt_filme(idFilme):
    sql = f"""DELETE FROM filmes WHERE idFilme = '{idFilme}';"""
    cursor.execute(sql)
    conexao.commit()
