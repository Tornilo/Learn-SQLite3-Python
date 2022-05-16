import sqlite3 as sql3

bD = sql3.connect('clientes.db')
cursor = bD.cursor()
nomeTabela = 'clientes'

#Obtendo informações da tabela
cursor.execute('PRAGMA table_info({})'.format(nomeTabela))

colunas = [tupla[1] for tupla in cursor.fetchall()]
print('Colunas: ',colunas)

#Listando as tabelas do banco de dados
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
""")

print('Tabelas: ')
for tabela in cursor.fetchall():
    print("%s" %(tabela))

#Obtendo o schema da tabela
cursor.execute("""
SELECT sql FROM sqlite_master WHERE type='table' AND name=?
""",(nomeTabela,))

print("Shema: ")
for schema in cursor.fetchall():
    print("%s" % (schema))

bD.close()