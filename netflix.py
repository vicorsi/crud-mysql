
from create import inserir_filmes, inserir_usuarios
from read import listar_filmes, listar_usuarios, procurar_usuario
from update import up_usuario, up_filme
from delete import dt_usuario, dt_filme

class Cliente:
    def __init__(self, nome='', email='', plano='basic', tipo='user'):
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']
        if plano in self.planos:
            self.plano = plano
        else:
            print('Plano inválido.')
            self.plano = ''
        self.tipos = ['user', 'admin']
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            print('Tipo de usuário inválido.')
            self.tipo = ''
        self.user = ''

    def menu(self, user=''):
        while True:
            try:
                print(f'\n\nUsuário: {self.user}\n'
                      '[0] - Quit\n'
                      '[1] - Login\n'
                      '[2] - Create\n'
                      '[3] - Read\n'
                      '[4] - Update\n'
                      '[5] - Delete\n'
                      )
                op = int(input('Escolha a opção: '))
                if op == 0:
                    break
                elif op == 1:
                    self.login()
                elif op == 2:
                    if self.user != '':
                        self.menu_cadastrar()
                    else:
                        print('É necessário Logar como admin para fazer CREATE...')
                elif op == 3:
                    if self.user != '':
                        self.menu_listar()
                    else:
                        print('É necessário Logar como admin para fazer READ...')
                elif op == 4:
                    if self.user != '':
                        self.menu_atualizar()
                    else:
                        print('É necessário Logar como admin para fazer UPDATE...')
                elif op == 5:
                    if self.user != '':
                        self.menu_apagar()
                    else:
                        print('É necessário Logar como admin para fazer DELETE...')
                else:
                    print('Escolha um número válido...')

            except ValueError as e:
                print(f'Erro: {e}, o valor deve ser um número...')

    def menu_cadastrar(self):
        print('\n'
              '[0] - Sair\n'
              '[1] - Usuário\n'
              '[2] - Filme\n'
              )
        op = int(input('Escolha a opção: '))
        if op == 0:
            pass
        elif op == 1:
            inserir_usuarios()
        elif op == 2:
            inserir_filmes()

    def menu_listar(self):
        print('\n'
              '[0] - Sair\n'
              '[1] - Usuário\n'
              '[2] - Filme\n'
              )
        op = int(input('Escolha a opção: '))
        if op == 0:
            pass
        elif op == 1:
            listar_usuarios()
        elif op == 2:
            listar_filmes()

    def login(self):
        usuario = input('Usuário: ')
        email = input('Email: ')
        procurar_usuario(usuario, email)
        x = procurar_usuario(usuario, email)
        self.user = usuario
        print(x)
        if x == 'admin':
            return self.user

    def menu_atualizar(self):
        print('\n'
              '[0] - Sair\n'
              '[1] - Usuário\n'
              '[2] - Filme\n'
              )
        op = int(input('Escolha a opção: '))
        if op == 0:
            pass
        elif op == 1:
            up_usuario()
        elif op == 2:
            up_filme()

    def menu_apagar(self):
        print('\n'
              '[0] - Sair\n'
              '[1] - Usuário\n'
              '[2] - Filme\n'
              )
        op = int(input('Escolha a opção: '))
        if op == 0:
            pass
        elif op == 1:
            dt_usuario()
        elif op == 2:
            dt_filme()



