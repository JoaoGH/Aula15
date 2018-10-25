import pymysql
con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
cursor = con.cursor()
sql = "CREATE TABLE clientes (idclientes int PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(255), cpf VARCHAR(14), email VARCHAR(255), telefone VARCHAR(20))"
cursor.execute(sql)
sql2 = "CREATE TABLE produtos (idprodutos int PRIMARY KEY AUTO_INCREMENT, codigo VARCHAR(255), descricao TEXT, unidade VARCHAR(2), pCompra DOUBLE, pVenda DOUBLE)"
cursor.execute(sql2)
con.close()