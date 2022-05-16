import sqlite3 as sql3

bD = sql3.connect('clientes.db')
cursor = bD.cursor()

# excluindo um registro da tabela
# Use o WHERE para escolher a linha que será excluida, caso contrário,
#a tabela será excluida.
cursor.execute("""
DELETE FROM clientes
WHERE user_id = 1
""")

bD.commit()

print('Registro excluido com sucesso.')

bD.close()
