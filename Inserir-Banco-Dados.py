import sqlite3 as sql3

bD = sql3.connect('clientes.db')
cursor = bD.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes(user_id, name, num_friends)
VALUES(0, 'Hero', 2)
""")

cursor.execute("""
INSERT INTO clientes(user_id, name, num_friends)
VALUES(1, 'John', 5)
""")

cursor.execute("""
INSERT INTO clientes(user_id, name, num_friends)
VALUES(2, 'Carl', 9)
""")

#---------Inserindo n registros -----------------
"""
lista = [(3, 'Danilo',6), (4,'Pedro', 8), (5, 'Victor', 10)]
"""
#cursor.executemany("""INSERT INTO clientes(user_id, name, num_friends)VALUES(?,?,?)""",lista)

#------------------------------------------------

# commit(): grava de fato as alterações na tabela;
bD.commit()

print('Dados inseridos com sucesso.')

bD.close()
