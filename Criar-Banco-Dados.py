import sqlite3 as sql

# Criar banco de dados;
#conectando...
bD = sql.connect('clientes.db')

# Cursor: é um interador que permite navegar e manipular os registros do bD.
cursor = bD.cursor()

# Execute: lê e executa comandos SQL puro diretamente no bD.
cursor.execute("""
CREATE TABLE clientes (
        user_id INT NOT NULL,
        name VARCHAR(200),
        num_friends INT);
""")

print('Tabela criada com sucesso.')

#desconectando...
bD.close()
