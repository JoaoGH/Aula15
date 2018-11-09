# -*- coding: utf-8 -*-
import pymysql


class Funcoes():
    def __init__(self, idCliente, idProduto, nome, cpf, email, telefone, codigo, descricao, unidade, cPreco, vPreco):
        self.idCliente = idCliente
        self.idProduto = idProduto
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.codigo = codigo
        self.descricao = descricao
        self.unidade = unidade
        self.cPreco = cPreco
        self.vPreco = vPreco

    def cadClientes(self):
        sql = "INSERT INTO clientes (nome,cpf,email,telefone) VALUES (%s,%s,%s,%s)"
        val = (self.nome, self.cpf,self.email,self.telefone)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def busClientes(self):
        sql = "select * from clientes where idClientes = %s"
        val = self.idCliente
        returno = []
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno.append("Falha")
        con.close()
        return returno
    def edtClientes(self):
        sql = "UPDATE clientes SET nome = %s, cpf = %s, email = %s, telefone = %s WHERE idClientes = %s"
        val = (self.nome, self.cpf, self.email, self.telefone, self.idCliente)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno
    def delClientes(self):
        sql = "DELETE FROM clientes WHERE idClientes=%s"
        val = self.idCliente
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def listaClientes(self):
        sql = "select * from clientes"
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql)
            returno = []
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def cadProdutos(self):
        sql = "INSERT INTO produtos (codigo,descricao,unidade,pCompra,pVenda) VALUES (%s,%s,%s,%s,%s)"
        val = (self.codigo, self.descricao, self.unidade, self.cPreco, self.vPreco)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def busProdutos(self):
        sql = "select * from produtos where idprodutos = %s"
        val = self.idProduto
        returno = []
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno.append("Falha")
        con.close()
        return returno

    def edtProdutos(self):
        sql = "UPDATE produtos SET codigo ='"+str(self.codigo)+"', descricao = '"+str(self.descricao)+"', unidade = '"+str(self.unidade)+"', pCompra = '"+str(self.cPreco)+"', pVenda = '"+str(self.vPreco)+"' WHERE idprodutos = '"+str(self.idProduto)+"'"
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def delProdutos(self):
        sql = "DELETE FROM produtos WHERE idprodutos=%s"
        val = self.idProduto
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def listaProdutos(self):
        sql = "select * from produtos"
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql)
            returno = []
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

