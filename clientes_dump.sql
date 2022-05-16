BEGIN TRANSACTION;
CREATE TABLE clientes (
        user_id INT NOT NULL,
        name VARCHAR(200),
        num_friends INT, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(0,'Hero',2,NULL);
INSERT INTO "clientes" VALUES(2,'Juliana',11,NULL);
COMMIT;
