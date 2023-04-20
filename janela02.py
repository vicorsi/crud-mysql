from tkinter import *
from tkinter import ttk
from create import inserir_filmes, inserir_usuarios
from read import listar_usuarios, procurar_usuario
from update import up_usuario, up_filme
from delete import dt_usuario, dt_filme

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        self.select_list()
        janela.mainloop()

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.geometry('700x500')
        self.janela.configure(background='#bdbcb3')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#b0afa9',
                             highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.janela, bg='#b0afa9',
                             highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.25)

        self.frame_2 = Frame(self.janela, bg='#b0afa9',
                             highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_2.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text='Buscar', bg='#70bfb3', command=self.select_user)
        self.btBuscar.place(relx=0.15, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btLimpar = Button(self.frame_0, text='Limpar', bg='#70bfb3', command=self.limpa_tela)
        self.btLimpar.place(relx=0.27, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btCreate = Button(self.frame_0, text='Create', bg='#70bfb3', command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btRead = Button(self.frame_0, text='Read', bg='#70bfb3', command=self.select_list)
        self.btRead.place(relx=0.55, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btUpdate = Button(self.frame_0, text='Update', bg='#70bfb3', command=self.update_user)
        self.btUpdate.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.5)

        self.btDelete = Button(self.frame_0, text='Delete', bg='#70bfb3', command=self.delete_user)
        self.btDelete.place(relx=0.75, rely=0.25, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lbIDUsuario = Label(self.frame_0, text='ID', bg='#b0afa9')
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.3)

        self.lbNome = Label(self.frame_1, text='Nome', bg='#b0afa9')
        self.lbNome.place(relx=0.005, rely=0.05, relwidth=0.1, relheight=0.15)

        self.lbEmail = Label(self.frame_1, text='Email', bg='#b0afa9')
        self.lbEmail.place(relx=0.005, rely=0.35, relwidth=0.1, relheight=0.15)

        self.lbPlano = Label(self.frame_1, text='Plano', bg='#b0afa9')
        self.lbPlano.place(relx=0.005, rely=0.65, relwidth=0.1, relheight=0.15)

        self.lbTipo = Label(self.frame_1, text='Tipo', bg='#b0afa9')
        self.lbTipo.place(relx=0.32, rely=0.65, relwidth=0.1, relheight=0.15)

        self.lbIdade = Label(self.frame_1, text='Idade', bg='#b0afa9')
        self.lbIdade.place(relx=0.62, rely=0.65, relwidth=0.1, relheight=0.15)

    def inputs(self):
        self.inpIDUsuario = Entry(self.frame_0)
        self.inpIDUsuario.place(relx=0.005, rely=0.25, relwidth=0.1, relheight=0.5)

        self.inpNome = Entry(self.frame_1)
        self.inpNome.place(relx=0.12, rely=0.05, relwidth=0.8, relheight=0.25)

        self.inpEmail = Entry(self.frame_1)
        self.inpEmail.place(relx=0.12, rely=0.35, relwidth=0.8, relheight=0.25)

        self.inpPlano = Entry(self.frame_1)
        self.inpPlano.place(relx=0.12, rely=0.65, relwidth=0.2, relheight=0.25)

        self.inpTipo = Entry(self.frame_1)
        self.inpTipo.place(relx=0.425, rely=0.65, relwidth=0.2, relheight=0.25)

        self.inpIdade = Entry(self.frame_1)
        self.inpIdade.place(relx=0.72, rely=0.65, relwidth=0.2, relheight=0.25)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     columns=('col1',
                                              'col2',
                                              'col3',
                                              'col4',
                                              'col5',
                                              'col6'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Email')
        self.listaCli.heading('#4', text='Plano')
        self.listaCli.heading('#5', text='Tipo')
        self.listaCli.heading('#6', text='Idade')

        self.listaCli.column('#0', width=5)
        self.listaCli.column('#1', width=35)
        self.listaCli.column('#2', width=220)
        self.listaCli.column('#3', width=220)
        self.listaCli.column('#4', width=70)
        self.listaCli.column('#5', width=70)
        self.listaCli.column('#6', width=70)

        self.listaCli.place(relx=0.01, rely=0.1,
                            relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def select_list(self):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in listar_usuarios():
            self.listaCli.insert(parent='', index=0, values=i)

    def insert_user(self):
        inserir_usuarios(self.inpNome.get(),
                         self.inpEmail.get(),
                         self.inpPlano.get(),
                         self.inpTipo.get(),
                         self.inpIdade.get())
        self.limpa_tela()
        self.select_list()

    def delete_user(self):
        dt_usuario(self.inpIDUsuario.get())
        print(self.inpIDUsuario.get())
        self.limpa_tela()
        self.select_list()

    def limpa_tela(self):
        self.inpIDUsuario.delete(0, END)
        self.inpTipo.delete(0, END)
        self.inpNome.delete(0, END)
        self.inpIdade.delete(0, END)
        self.inpPlano.delete(0, END)
        self.inpEmail.delete(0, END)
        self.listaCli.delete(*self.listaCli.get_children())

    def update_user(self):
        if self.inpNome.get():
            self.inpIDUsuario.update()
            self.inpNome.update()
            self.inpTipo.update()
            self.inpEmail.update()
            self.inpIdade.update()
            self.inpPlano.update()
            up_usuario(self.inpIDUsuario.get(), self.inpNome.get(),
                       self.inpEmail.get(), self.inpIdade.get(),
                       self.inpTipo.get(), self.inpPlano.get())
            self.limpa_tela()
            self.select_list()

    def select_user(self):
        self.listaCli.delete(*self.listaCli.get_children())
        usuario = procurar_usuario(self.inpIDUsuario.get())
        self.listaCli.insert(parent='', index=0, values=usuario[0])
        self.inpNome.insert(0, usuario[0][1])
        self.inpEmail.insert(0, usuario[0][2])
        self.inpPlano.insert(0, usuario[0][3])
        self.inpTipo.insert(0, usuario[0][4])
        self.inpIdade.insert(0, usuario[0][5])
