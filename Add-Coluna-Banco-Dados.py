import sqlite3 as sql3

bD = sql3.connect('clientes.db')
cursor = bD.cursor()

# Adicionando uma nova coluna na tabela;

cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""")

bD.commit()

print('Nova coluna adicionada com sucesso')

bD.close()
