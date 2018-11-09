# -*- coding: utf-8 -*-
from tkinter import *
from Funcoes import Funcoes



def telaClientes():
    def executar():
        n=nome.get()
        c=cpf.get()
        e=email.get()
        t=tel.get()
        f = Funcoes(0,0,n,c,e,t,"","","",0,0)
        lb5 = Label(window, text=f.cadClientes()).place(x=150, y=450)
    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    # janela.destroy()

    Label(window, width=25, text="Cadastro de clientes", font=("Verdana", 30)).place(x=0, y=50)

    Label(window, text="Nome do cliente:").place(x=100, y=150)
    nome = Entry(window, width=30, fg="black")
    nome.place(x=250, y=153)
    Label(window, text="CPF:").place(x=100, y=180)
    cpf = Entry(window, width=30, fg="black")
    cpf.place(x=250, y=183)
    Label(window, text="E-mail:").place(x=100, y=210)
    email = Entry(window, width=30, fg="black")
    email.place(x=250, y=213)
    Label(window, text="Telefone:").place(x=100, y=240)
    tel = Entry(window, width=30, fg="black")
    tel.place(x=250, y=243)
    bt = Button(window, text="Cadastrar", command=executar)
    bt.place(x=250, y=300)

def listarClientes():
    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    lista = Funcoes(0, 0, "", "", "", "", "", "", "", 0, 0)
    for i in range(len(lista.listaClientes())):
        val = lista.listaClientes()[i]
        for n in range(len(val)):  # Column
            b = Entry(window)
            b.insert(0, val[n])
            b.grid(row=i, column=n)
            # b.place(x=100, y=100)
    window.mainloop()

def editarClientes():
    print("ola2")

def telaProdutos():
    def chamaFuncao():
        c = codigo.get()
        d = descricao.get()
        u = unidade.get()
        cP = cPreco.get()
        vP = vPreco.get()
        ret = Label(window, text="")
        cadastro = Funcoes(0, 0, "", "", "", "", c, d, u, float(cP), float(vP))
        ret['text'] = cadastro.cadastraProdutos()
        ret.place(x=100, y=350)

    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")

    Label(window, width=25, text="Cadastro de Produtos", font=("Verdana", 30)).place(x=0, y=50)



    Label(window, text="Código do produto").place(x=100, y=150)
    codigo = Entry(window, width=30, fg="black")
    codigo.place(x=250, y=153)
    Label(window, text="Descrição").place(x=100, y=180)
    descricao = Entry(window, width=30, fg="black")
    descricao.place(x=250, y=183)
    Label(window, text="Unidade").place(x=100, y=210)
    unidade = Entry(window, width=30, fg="black")
    unidade.place(x=250, y=213)
    Label(window, text="Preço de Compra").place(x=100, y=240)
    cPreco = Entry(window, width=30, fg="black")
    cPreco.place(x=250, y=243)
    Label(window, text="Preço de Venda").place(x=100, y=270)
    vPreco = Entry(window, width=30, fg="black")
    vPreco.place(x=250, y=273)
    btn = Button(window, text="Cadastrar", command=chamaFuncao)
    btn.place(x=300, y=350)

def listarProdutos():
    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    lista = Funcoes(0, 0, "", "", "", "", "", "", "", 0, 0)
    for i in range(len(lista.listaProdutos())):
        val = lista.listaProdutos()[i]
        for n in range(len(val)):  # Column
            b = Entry(window)
            b.insert(0, val[n])
            b.grid(row=i, column=n)
    window.mainloop()

def editarProdutos():
    print("ola5")
# def cadClientes():


janela = Tk()
janela.title("Cadastro do barulho")
janela.geometry("600x500")



lb = Label(janela, width=36, text="Selecione o que fazer a seguir", font=("Verdana", 20)).place(x=0, y=90)

bt = Button (janela, text="Cadastro de Clientes", command=telaClientes)
bt.place(x=250, y=150)
bt2 = Button (janela, text="Lista de Clientes", command=listarClientes)
bt2.place(x=250, y=190)
bt3 = Button (janela, text="Editar Informações de Clientes", command=editarClientes)
bt3.place(x=250, y=230)
bt4 = Button (janela, text="Cadastro de Produto", command=telaProdutos)
bt4.place(x=250, y=270)
bt5 = Button (janela, text="Lista de Produto", command=listarProdutos)
bt5.place(x=250, y=310)
bt6 = Button (janela, text="Editar Informações de Produto", command=editarProdutos)
bt6.place(x=250, y=350)




janela.mainloop()
