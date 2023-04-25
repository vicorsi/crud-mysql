from tkinter import *

janela = Tk()
usuarios = []
idades = []


class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        janela.mainloop()

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.configure(background='#bdbcb3')
        self.janela.geometry('700x1000')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=1000)

    def frames(self):
        self.frame_0 = Frame(self.janela, bg='#b0afa9', highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.05)

        self.frame_1 = Frame(self.janela, bg='#b0afa9', highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_1.place(relx=0.03, rely=0.09, relwidth=0.94, relheight=0.12)

        self.frame_2 = Frame(self.janela, bg='#b0afa9', highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_2.place(relx=0.03, rely=0.23, relwidth=0.94, relheight=0.20)

        self.frame_3 = Label(self.janela, bg='#b0afa9', highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_3.place(relx=0.03, rely=0.44, relwidth=0.94, relheight=0.23)

    def botoes(self):
        self.btBuscar = Button(self.frame_0, text="Buscar", command=self.janela2)
        self.btBuscar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btLimpar = Button(self.frame_0, text="Limpar", bg='#70bfb3', fg='#333')
        self.btLimpar.place(relx=0.27, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btCreate = Button(self.frame_0, text="Create")
        self.btCreate.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btRead = Button(self.frame_0, text="Read")
        self.btRead.place(relx=0.57, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btUpdate = Button(self.frame_0, text="Update")
        self.btUpdate.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.50)

        self.btDelete = Button(self.frame_0, text="Delete")
        self.btDelete.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.50)

    def labels(self):
        self.lbIDUsuario = Label(self.frame_0, text='ID', bg='#b0afa9')
        self.lbIDUsuario.place(relx=0.005, rely=0.01, relwidth=0.1, relheight=0.3)

        self.lbNome = Label(self.frame_1, text='Nome', bg='#b0afa9')
        self.lbNome.place(relx=0.005, rely=0.06, relwidth=0.1, relheight=0.15)

        self.lbEmail = Label(self.frame_1, text='Email', bg='#b0afa9')
        self.lbEmail.place(relx=0.005, rely=0.37, relwidth=0.1, relheight=0.15)

        self.lbPlano = Label(self.frame_1, text='Plano', bg='#b0afa9')
        self.lbPlano.place(relx=0.005, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbTipo = Label(self.frame_1, text='Tipo', bg='#b0afa9')
        self.lbTipo.place(relx=0.32, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbIdade = Label(self.frame_1, text='Idade', bg='#b0afa9')
        self.lbIdade.place(relx=0.62, rely=0.69, relwidth=0.1, relheight=0.15)

        self.lbStatus = Label(self.janela, text='', fg='red', bg='#b0afa9')
        self.lbStatus.place(relx=0.05, rely=0.21, relwidth=0.90, relheight=0.02)

    def inputs(self):
        self.inpIDUsuario = Entry(self.frame_0)
        self.inpIDUsuario.place(relx=0.005, rely=0.37, relwidth=0.1, relheight=0.5)

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

    def janela2(self):
        self.janela2 = Toplevel()
        self.janela2.title("Janela2")
        self.janela2.configure(background="lightblue")
        self.janela2.geometry('200x200')
        self.janela2.resizable(False, False)
        self.janela2.transient(self.janela)
        self.janela2.focus_force()
        self.janela2.grab_set()