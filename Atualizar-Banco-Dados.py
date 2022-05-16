import sqlite3 as sql3

bD = sql3.connect('clientes.db')
cursor = bD.cursor()

# Lendo os dados

cursor.execute("""
UPDATE clientes
SET name = ?, num_friends =?
WHERE user_id = ?
""", ('Juliana',11, 2))

bD.commit()

print('Dados atualizados com sucesso.')

bD.close()
