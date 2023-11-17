# -*- coding: utf-8 -*-

# Importa as bilbiotecas de dependências.
import json
import sqlite3
import os


database = 'temp_db.db'

def get_all_owner():
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql = "SELECT * FROM owner WHERE owner_status != 'off'"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    res = []
    for res_temp in data:
        res.append(dict(res_temp))
    return res


def get_one_owner(id):
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql = "SELECT * FROM owner WHERE owner_status != 'off' AND owner_id = ?"
    cursor.execute(sql, (id,))
    data = cursor.fetchone()
    conn.close()

    if data:  
        return dict(data)
    else:  
        return {"error": "Registro não encontrado."}

# Limpa o console.
os.system('cls')

# Exemplo para obter todos os 'item' válidos.
#print(  # Exibe no console.
#  json.dumps(  # No formato JSON.
#      get_all_items(),  # Os items obtidos desta função.
#      ensure_ascii=False,  # Usando a tabela UTF-8 (acentuação).
#      indent=2  # Formatando o JSON.
#  )
#)

print(
    json.dumps(
        get_one_owner(3),
        ensure_ascii=False,
        indent=2
    )
)
