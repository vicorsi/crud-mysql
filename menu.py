#
# from create import inserir_filmes, inserir_usuarios
# from read import listar_filmes, listar_usuarios, procurar_usuario
# from update import up_usuario, up_filme
# from delete import dt_usuario, dt_filme
#
# def menu(user):
#     while True:
#         print(f'\n\nUsuário: {user}\n'
#               '[0] - Sair\n'
#               '[1] - Login\n'
#               '[2] - Cadastrar\n'
#               '[3] - Listar\n'
#               '[4] - Atualizar\n'
#               '[5] - Apagar\n'
#               )
#         op = int(input('Escolha a opção: '))
#         if op == 0:
#             break
#         elif op == 1:
#             login()
#         elif op == 2:
#             if user != '':
#                 menu_cadastrar()
#             else:
#                 print('É necessário Logar como admin para fazer cadastros...')
#         elif op == 3:
#             menu_listar()
#         elif op == 4:
#             menu_atualizar()
#         elif op == 5:
#             menu_apagar()
#
#
# def menu_cadastrar():
#     print('\n'
#           '[0] - Sair\n'
#           '[1] - Usuário\n'
#           '[2] - Filme\n'
#           )
#     op = int(input('Escolha a opção: '))
#     if op == 0:
#         pass
#     elif op == 1:
#         inserir_usuarios()
#     elif op == 2:
#         inserir_filmes()
#
#
# def menu_listar():
#     print('\n'
#           '[0] - Sair\n'
#           '[1] - Usuário\n'
#           '[2] - Filme\n'
#           )
#     op = int(input('Escolha a opção: '))
#     if op == 0:
#         pass
#     elif op == 1:
#         listar_usuarios()
#     elif op == 2:
#         listar_filmes()
#
#
# def login():
#     usuario = input('Usuário: ')
#     email = input('Email: ')
#     procurar_usuario(usuario, email)
#     if procurar_usuario(usuario, email) == 'admin':
#         menu(usuario)
#
#
# def menu_atualizar():
#     print('\n'
#           '[0] - Sair\n'
#           '[1] - Usuário\n'
#           '[2] - Filme\n'
#           )
#     op = int(input('Escolha a opção: '))
#     if op == 0:
#         pass
#     elif op == 1:
#         up_usuario()
#     elif op == 2:
#         up_filme()
#
# def menu_apagar():
#     print('\n'
#           '[0] - Sair\n'
#           '[1] - Usuário\n'
#           '[2] - Filme\n'
#           )
#     op = int(input('Escolha a opção: '))
#     if op == 0:
#         pass
#     elif op == 1:
#         dt_usuario()
#     elif op == 2:
#         dt_filme()