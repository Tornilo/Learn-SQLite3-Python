import sqlite3 as sql3

bD = sql3.connect('clientes.db')
cursor = bD.cursor()

# Lendo os dados

cursor.execute("""
SELECT * FROM clientes;
""")

# O método fetchall() retorna o resultado do SELECT;
for linha in cursor.fetchall():
    print(linha)

bD.close()
