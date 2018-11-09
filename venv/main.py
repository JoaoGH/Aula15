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
        Label(window, text=f.cadClientes()).place(x=150, y=450)
        nome.delete(0,END)
        cpf.delete(0,END)
        email.delete(0,END)
        tel.delete(0,END)
    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    # janela.destroy()

    Label(window, width=25, text="Cadastro de clientes", font=("Verdana", 20)).place(x=0, y=50)

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
    window.geometry("700x600")
    lista = Funcoes(0, 0, "", "", "", "", "", "", "", 0, 0)
    for i in range(len(lista.listaClientes())):
        val = lista.listaClientes()[i]
        for j in range(len(val)):
            b = Entry(window)
            b.insert(0, val[j])
            b.grid(row=i, column=j)
    window.mainloop()

def editarClientes():

    def busca():
        def editar():
            f = Funcoes(id.get(), 0, nome.get(), cpf.get(), email.get(), tel.get(),"", "", "", 0, 0)
            Label(window, text=f.edtClientes()).place(x=75, y=450)
            zerar()
        def deletar():
            f = Funcoes(id.get(), 0, "","", "", "","", "", "", 0, 0)
            Label(window, text=f.delClientes()).place(x=75, y=450)
            zerar()
        def zerar():
            id.delete(0, END)
            nome.delete(0, END)
            cpf.delete(0, END)
            email.delete(0, END)
            tel.delete(0, END)


        f = Funcoes(id.get(),0,"","","","","","","",0,0)
        f.busClientes()
        val = f.busClientes()[0]
        Label(window, text="Nome").place(x=50,y=150)
        nome = Entry(window)
        nome.insert(0,val[1])
        nome.place(x=125, y=150)
        Label(window, text="CPF").place(x=50, y=200)
        cpf = Entry(window)
        cpf.insert(0,val[2])
        cpf.place(x=125,y=200)
        Label(window, text="Email").place(x=50, y=250)
        email = Entry(window)
        email.insert(0, val[3])
        email.place(x=125, y=250)
        Label(window, text="Telefone").place(x=50, y=300)
        tel = Entry(window)
        tel.insert(0, val[4])
        tel.place(x=125, y=300)
        edt = Button(window,text="Editar", command=editar)
        edt.place(x=50, y=350)
        dlt = Button(window, text="Deletar", command=deletar)
        dlt.place(x=150, y=350)

    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    id = Entry(window)
    Label(window, width=25, text="Editar clientes", font=("Verdana", 20)).place(x=100, y=50)
    Label(window, text="Informe a ID").place(x=50, y=100)
    id.place(x=125, y=100)
    busca = Button(window, command=busca, text="Buscar")
    busca.place(x=275, y=100)
    window.mainloop()

def telaProdutos():
    def chamaFuncao():
        c = codigo.get()
        d = descricao.get()
        u = unidade.get()
        cP = float(cPreco.get())
        vP = float(vPreco.get())
        f = Funcoes(0, 0, "", "", "", "", c, d, u, cP, vP)
        Label(window, text=f.cadProdutos()).place(x=150, y=450)
        codigo.delete(0,END)
        descricao.delete(0,END)
        unidade.delete(0,END)
        cPreco.delete(0,END)
        vPreco.delete(0,END)


    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")

    Label(window, width=25, text="Cadastro de Produtos", font=("Verdana", 20)).place(x=100, y=50)



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
    window.geometry("700x600")
    lista = Funcoes(0, 0, "", "", "", "", "", "", "", 0, 0)
    for i in range(len(lista.listaProdutos())):
        val = lista.listaProdutos()[i]
        for j in range(len(val)):  # Column
            b = Entry(window)
            b.insert(0, val[j])
            b.grid(row=i, column=j)
    window.mainloop()


def editarProdutos():
    def busca():
        def editar():
            f = Funcoes(0, id.get(), "", "", "", "", codigo.get(), des.get(), un.get(), float(cPreco.get()),float(vPreco.get()))
            Label(window, text=f.edtProdutos()).place(x=75, y=450)
            zerar()
        def deletar():
            f = Funcoes(0, id.get(), "", "", "", "", "", "", "", 0, 0)
            Label(window, text=f.delProdutos()).place(x=75, y=450)
            zerar()
        def zerar():
            id.delete(0, END)
            codigo.delete(0, END)
            des.delete(0, END)
            un.delete(0, END)
            cPreco.delete(0, END)
            vPreco.delete(0, END)

        f = Funcoes(0, id.get(), "", "", "", "", "", "", "", 0, 0)
        val = f.busProdutos()[0]
        Label(window, text="Código").place(x=50, y=150)
        codigo = Entry(window)
        codigo.insert(0, val[1])
        codigo.place(x=200, y=150)
        Label(window, text="Descrição").place(x=50, y=200)
        des = Entry(window)
        des.insert(0, val[2])
        des.place(x=200, y=200)
        Label(window, text="Unidade").place(x=50, y=250)
        un = Entry(window)
        un.insert(0, val[3])
        un.place(x=200, y=250)
        Label(window, text="Preço de Compra").place(x=50, y=300)
        cPreco = Entry(window)
        cPreco.insert(0, val[4])
        cPreco.place(x=200, y=300)
        Label(window, text="Preço de Venda").place(x=50, y=350)
        vPreco = Entry(window)
        vPreco.insert(0, val[5])
        vPreco.place(x=200, y=350)
        edt = Button(window, text="Editar", command=editar)
        edt.place(x=50, y=400)
        dlt = Button(window, text="Deletar", command=deletar)
        dlt.place(x=200, y=400)

    window = Tk()
    window.title("Cadastro do barulho")
    window.geometry("600x500")
    Label(window, width=25, text="Editar produtos", font=("Verdana", 20)).place(x=100, y=50)
    id = Entry(window)
    Label(window, text="Informe a ID").place(x=50, y=100)
    id.place(x=125, y=100)
    busca = Button(window, command=busca, text="Buscar")
    busca.place(x=275, y=100)
    window.mainloop()

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
bt4 = Button (janela, text="Cadastro de Produtos", command=telaProdutos)
bt4.place(x=250, y=270)
bt5 = Button (janela, text="Lista de Produtos", command=listarProdutos)
bt5.place(x=250, y=310)
bt6 = Button (janela, text="Editar Informações de Produtos", command=editarProdutos)
bt6.place(x=250, y=350)

lb5 = Label(janela, text="").place(x=150, y=450)


janela.mainloop()


