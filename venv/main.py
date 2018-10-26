# -*- coding: utf-8 -*-
from tkinter import *
# from calc import Calculos

def calcular():
    conta1=Calculos(1)

    tipo=option.get()
    tTaxa=option2.get()
    capital=ed1.get()
    taxa=ed2.get()
    if(tTaxa=="1" and taxa!=""):
        taxa=float(taxa)
    elif(tTaxa=="2" and taxa!=""):
        taxa=float(taxa)/12
    elif(taxa==""):
        taxa=taxa
    else:
        result="Selecione um tipo de taxa"
    periodo=ed3.get()
    montante=ed4.get()
    if(tipo=="1"):
        ##composto
        result = conta1.composto(capital, taxa, periodo, montante)
    elif(tipo=="2"):
        ##simples
        result=conta1.simples(capital, taxa, periodo, montante)
    else:
        result="Selecione um tipo de juros"

    lb5['text']=result

def trocar():
    print("hello!")
def trocar2():
    print("ola!")



janela = Tk()
janela.title("Calculadora Super Bolada 3000")
janela.geometry("600x500")

lb = Label(janela, width=25, text="Selecione o que\nfazer a seguir", font=("Verdana", 30))
lb.place(x=0, y=0)


menubar = Menu(janela)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Cadastro de clientes", command=trocar)
filemenu.add_command(label="Cadastro de produtos", command=trocar2)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=janela.quit)
menubar.add_cascade(label="Cadastro", menu=filemenu)
janela.config(menu=menubar)

option = StringVar()
rd1 = Radiobutton(janela, text="Juros Composto", fg="black", font=("Verdana", 12), variable=option, value=1, tristatevalue=0)
rd1.place(x=250, y=140)
rd2 = Radiobutton(janela, text="Juros Simples", fg="black", font=("Verdana", 12), variable=option, value=2, tristatevalue=0)
rd2.place(x=250, y=170)

lb = Label(janela, text="Capital inicial:", font=("Verdana", 12))
lb.place(x=100, y=200)
ed1 = Entry(janela, width=20, fg="black")
ed1.place(x=250, y=203)

lb2 = Label(janela, text="Taxa de juros:", font=("Verdana", 12))
lb2.place(x=100, y=230)
ed2 = Entry(janela, width=20, fg="black")
ed2.place(x=250, y=233)

option2 = StringVar()
rd3 = Radiobutton(janela, text="% a.m.", fg="black", font=("Verdana", 12), variable=option2, value=1, tristatevalue=0)
rd3.place(x=250, y=252)
rd4 = Radiobutton(janela, text="% a.a.", fg="black", font=("Verdana", 12), variable=option2, value=2, tristatevalue=0)
rd4.place(x=250, y=275)


lb3 = Label(janela, text="Período (meses):", font=("Verdana", 12))
lb3.place(x=100, y=320)
ed3 = Entry(janela, width=20, fg="black")
ed3.place(x=250, y=323)

lb4 = Label(janela, text="Montante final:", font=("Verdana", 12))
lb4.place(x=100, y=350)
ed4 = Entry(janela, width=20, fg="black")
ed4.place(x=250, y=353)

bt = Button (janela, text="Calcular", command=calcular)
bt.place(x=250, y=400)

lb5 = Label(janela, text="", font=("Verdana", 12))
lb5.place(x=150, y=450)


janela.mainloop()
