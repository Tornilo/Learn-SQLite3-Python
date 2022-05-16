import sqlite3 as sql3
import io

bD = sql3.connect('clientes_recuperado.db')
cursor = bD.cursor()

f = io.open('clientes_dump.sql', 'r')
sql = f.read()
cursor.executescript(sql)

print('Banco de dados recuperado com sucesso.')
print('Salvo como clientes_recuperado.db')

bD.close()