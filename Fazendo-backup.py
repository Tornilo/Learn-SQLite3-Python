import sqlite3 as sql3
import io

bD = sql3.connect('clientes.db')

with io.open('clientes_dump.sql', 'w') as f:
    for linha in bD.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado com sucesso.')
print('Salvo como clientes_dump.sql')

bD.close()