from conectar import conexao, cursor


def listar_usuarios():
    sql = 'SELECT * from usuarios'
    cursor.execute(sql)
    return cursor.fetchall()


def listar_filmes():
    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    return cursor.fetchall()


def procurar_usuario(idUser):
    sql = f"SELECT * from usuarios WHERE idUsuario = '{idUser}'"
    cursor.execute(sql)
    return cursor.fetchall()

