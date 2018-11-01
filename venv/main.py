# -*- coding: utf-8 -*-
from tkinter import *
# from calc import Calculos

def telaClientes():
    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    # janela.destroy()

    menuBar()

    lb = Label(window, width=25, text="Cadastro de clientes", font=("Verdana", 30))
    lb.place(x=0, y=50)

    lb = Label(window, text="Nome do cliente:", font=("Verdana", 12))
    lb.place(x=100, y=150)
    ed1 = Entry(window, width=30, fg="black")
    ed1.place(x=250, y=153)

    lb2 = Label(window, text="CPF:", font=("Verdana", 12))
    lb2.place(x=100, y=180)
    ed2 = Entry(window, width=30, fg="black")
    ed2.place(x=250, y=183)

    lb3 = Label(window, text="E-mail:", font=("Verdana", 12))
    lb3.place(x=100, y=210)
    ed3 = Entry(window, width=30, fg="black")
    ed3.place(x=250, y=213)

    lb4 = Label(window, text="Telefone:", font=("Verdana", 12))
    lb4.place(x=100, y=240)
    ed4 = Entry(window, width=30, fg="black")
    ed4.place(x=250, y=243)

    bt = Button(window, text="Cadastrar")
    bt.place(x=250, y=300)

    lb5 = Label(window, text="", font=("Verdana", 12))
    lb5.place(x=150, y=450)


def telaProdutos():
    print("ola!")

# def cadClientes():

def menuBar():
    menubar = Menu(janela)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Cadastro de clientes", command=telaClientes)
    filemenu.add_command(label="Cadastro de produtos", command=telaProdutos)
    filemenu.add_separator()
    filemenu.add_command(label="Sair", command=janela.quit)
    menubar.add_cascade(label="Cadastro", menu=filemenu)
    janela.config(menu=menubar)

janela = Tk()
janela.title("Cadastro do barulho")
janela.geometry("600x500")


menuBar()

lb = Label(janela, width=25, text="Selecione o que\nfazer a seguir", font=("Verdana", 30))
lb.place(x=0, y=100)

bt = Button (janela, text="Cadastro de Clientes", command=telaClientes)
bt.place(x=250, y=250)
bt2 = Button (janela, text="Cadastro de Produto", command=telaProdutos)
bt2.place(x=250, y=300)




janela.mainloop()
