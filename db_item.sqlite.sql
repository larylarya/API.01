-- Apaga as tabelas caso exista.
-- CUIDADO! Isso destroi todos os dados do banco. 

DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS owner;

-- Cria a tabela 'owner'.
CREATE TABLE owner (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    owner_name TEXT,
    owner_email TEXT,
    owner_password TEXT,
    owner_birth DATE,
    owner_status TEXT COMMENTS "Valores: on, off"
    owner_field1 TEXT,
    owner_field2 TEXT
);

-- Popular a tabela 'owner' com dados 'fake'. 
INSERT INTO owner (owner_id, owner_date, owner_name, owner_email, owner_password, 
owner_birth, owner_status)
VALUES
('1', '2023-09-28 10:11:12', 'Joca da Silva', 'joca@silva.com',
'123', '1915-11-13', 'on'),('2', '2023-10-28 10:11:18', 'Lary da Silva', 'lary@silva.com',
'126', '1922-13-11', 'on'),('3', '2023-11-27 16:11:17', 'Isa da Silva', 'isa@silva.com',
'258', '1998-11-17', 'on'),('4', '2023-02-26 12:11:16', 'Lucas da Silva', 'lucas@silva.com',
'963', '1978-05-18', 'on'),('5', '2023-01-25 15:11:13', 'Lilia da Silva', 'lilia@silva.com',
'122', '1968-07-19', 'on'),('6', '2023-07-24 05:11:14', 'Fernanda da Silva', 'fernanda@silva.com',
'121', '1998-08-15', 'on'),('7', '2023-08-24 09:11:12', 'Lucia da Silva', 'lucia@silva.com',
'456', '1988-09-14', 'on'),('8', '2023-09-21 22:11:18', 'Jony da Silva', 'jony@silva.com',
'789', '1988-12-14', 'on'),('9', '2023-03-22 24:11:13', 'Leila da Silva', 'leila@silva.com',
'698', '1988-10-14', 'on');

-- Cria a tabela 'item'.
CREATE TABLE item (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    item_name TEXT,
    item_description TEXT,
    item_location TEXT,
    item_owner INTEGER,
	item_status TEXT DEFAULT 'on',
    item_field1 TEXT,
    item_field2 TEXT,
	FOREIGN KEY (item_owner) REFERENCES owner (owner_id)
);

INSERT INTO item (item_id, item_date, item_name, item_description,
 item_location,  item_owner, item_status)
VALUES
     ('10', '2022-03-21 10:11:13', 'Biscoito', 'Biscoito de limao', 'Madureira', '1', 'on'),
     ('12', '2021-04-22 10:10:19', 'Biscoito', 'Biscoito de laranja', 'Vaz Lobo', '2', 'on'),
     ('13', '2020-05-24 10:16:17', 'Biscoito', 'Biscoito de morango', 'Irajá', '3', 'on'),
     ('14', '2023-06-29 10:18:14', 'Biscoito', 'Biscoito de chocolate', 'Campo Grande', '4', 'on'),
     ('15', '2024-07-26 10:19:13', 'Biscoito', 'Biscoito de abacaxi', 'Gramacho', '5', 'on'), 
     ('16', '2025-08-24 10:14:12', 'Biscoito', 'Biscoito de framboesa', 'Cosmos', '6', 'on');
