from tkinter import *
from conectar import conexao
from tkinter import ttk
from create import inserir_filmes, inserir_usuarios
from read import listar_filmes, listar_usuarios
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

janela = Tk()


class Limpar():
    def limpa_tela(self):
        self.inpIdUsuario.delete(0, END)
        self.inpNome.delete(0, END)
        self.inpEmail.delete(0, END)
        self.inpPlano.delete(0, END)
        self.inpTipo.delete(0, END)
        self.inpClass.delete(0, END)


class Aplicacao(Limpar):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.select_list()
        self.lista_frame2()
        self.grafic()
        janela.mainloop()

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.configure(background='#70b0b3')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#70b0b3', highlightthickness=0.5, highlightbackground='#f00')
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)
        self.frame_1 = Frame(self.janela, bg='#84dbdb', highlightthickness=2, highlightbackground='#2962f2')
        self.frame_1.place(relx=0.03, rely=0.15, relwidth=0.94, relheight=0.35)
        self.frame_2 = Frame(self.janela, bg='#84dbdb', highlightthickness=2, highlightbackground='#2962f2')
        self.frame_2.place(relx=0.03, rely=0.51, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btLimpar = Button(self.frame_0, text="Buscar", bd=4)
        self.btLimpar.place(relx=0.15, rely=0.45, relwidth=0.1, relheight=0.50)

        self.btLimpar = Button(self.frame_0, text="Limpar", bg='#70bfb3', fg='#333', command=self.limpa_tela)
        self.btLimpar.place(relx=0.25, rely=0.45, relwidth=0.1, relheight=0.50)

        self.btCreate = Button(self.frame_0, text="Create", fg='#f00',
                               command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.45, relwidth=0.1, relheight=0.50)

        self.btRead = Button(self.frame_0, text="Read")
        self.btRead.place(relx=0.55, rely=0.45, relwidth=0.1, relheight=0.50)

        self.btUpdate = Button(self.frame_0, text="Update")
        self.btUpdate.place(relx=0.65, rely=0.45, relwidth=0.1, relheight=0.50)

        self.btDelete = Button(self.frame_0, text="Delete")
        self.btDelete.place(relx=0.75, rely=0.45, relwidth=0.1, relheight=0.50)

    def labels(self):
        self.lbIdUsuario = Label(self.frame_0, text='UsuárioID', background='#70b0b3')
        self.lbIdUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.50)

        self.lbNome = Label(self.frame_1, text='Nome', bg='#84dbdb')
        self.lbNome.place(relx=0.005, rely=0.05, relwidth=0.1, relheight=0.15)

        self.lbEmail = Label(self.frame_1, text='Email', bg='#84dbdb')
        self.lbEmail.place(relx=0.005, rely=0.25, relwidth=0.1, relheight=0.15)

        self.lbPlano = Label(self.frame_1, text='Plano', bg='#84dbdb')
        self.lbPlano.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lbTipo = Label(self.frame_1, text='Tipo', bg='#84dbdb')
        self.lbTipo.place(relx=0.32, rely=0.45, relwidth=0.1, relheight=0.15)

        self.lbClass = Label(self.frame_1, text='Class', bg='#84dbdb')
        self.lbClass.place(relx=0.62, rely=0.45, relwidth=0.1, relheight=0.15)

    def inputs(self):
        self.inpIdUsuario = Entry(self.frame_0)
        self.inpIdUsuario.place(relx=0.005, rely=0.45, relwidth=0.1, relheight=0.50)

        self.inpNome = Entry(self.frame_1)
        self.inpNome.place(relx=0.12, rely=0.05, relwidth=0.8, relheight=0.15)

        self.inpEmail = Entry(self.frame_1)
        self.inpEmail.place(relx=0.12, rely=0.25, relwidth=0.8, relheight=0.15)

        self.inpPlano = Entry(self.frame_1)
        self.inpPlano.place(relx=0.12, rely=0.45, relwidth=0.2, relheight=0.15)

        self.inpTipo = Entry(self.frame_1)
        self.inpTipo.place(relx=0.425, rely=0.45, relwidth=0.2, relheight=0.15)

        self.inpClass = Entry(self.frame_1)
        self.inpClass.place(relx=0.72, rely=0.45, relwidth=0.2, relheight=0.15)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Email')
        self.listaCli.heading('#4', text='Plano')
        self.listaCli.heading('#5', text='Tipo')
        self.listaCli.heading('#6', text='Class')

        self.listaCli.column('#0', width=3)
        self.listaCli.column('#1', width=10)
        self.listaCli.column('#2', width=150)
        self.listaCli.column('#3', width=150)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)
        self.listaCli.column('#6', width=10)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        #Barra de Rolagem
        self.scroolLista=Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def select_list(self):
        #self.listaCli.delete(*self.listaCli.get_children())
        for i in self.list_user():
            print(i)
            #self.listaCli.insert('', END, values=i)


    def insert_user(self):
        '''
        FUNÇÃO QUE INSERE USUÁRIOS
        :return: None
        '''
        inserir_usuarios(self.inpNome.get(), self.inpEmail.get(), self.inpPlano.get(), self.inpTipo.get(), self.inpClass.get())
        self.select_list()

    def insert_movies(self):
        inserir_filmes()
        #{filme}', '{plano}', '{desc}', {classif}

    def list_user(self):
        cursor = conexao.cursor()
        cursor.execute('select database();')
        linha = cursor.fetchone()
        print(f'Banco => {linha[0]}')

        sql = 'SELECT * from usuarios'
        cursor.execute(sql)
        linhas = cursor.fetchall()
        return linhas

    def grafic(self):

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        recipe = ["375",
                  "75",
                  "250",
                  "300"]

        data = [float(x.split()[0]) for x in recipe]
        ingredients = [x.split()[-1] for x in recipe]

        def func(pct, allvals):
            absolute = int(np.round(pct / 100. * np.sum(allvals)))
            return f"{pct:.1f}%\n({absolute:d} g)"

        wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

        ax.legend(wedges, ingredients,
                  title="Ingredients",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))

        plt.setp(autotexts, size=8, weight="bold")

        ax.set_title("Matplotlib bakery: A pie")

        plt.show()