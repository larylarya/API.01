# -*- coding: utf-8 -*-

# Importa bibliotecas.
from flask import Flask, jsonify, request, abort, make_response, json, Response
import sqlite3

app = Flask(__name__)

json.provider.DefaultJSONProvider.ensure_ascii = False

database = "./temp_db.db"


def prefix_remove(prefix, data):
    
    new_data = {}
    for key, value in data.items():
        if key.startswith(prefix):
            new_key = key[len(prefix):]
            new_data[new_key] = value
        else:
            new_data[key] = value
    return new_data


@app.route("/owner", methods=["GET"])
def get_all():

    try:

        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM owner WHERE owner_status = 'on' ORDER BY owner_date DESC")

        owner_rows = cursor.fetchall()
        conn.close()

        owner = []
        for owner_row in owner_rows:
            owner.append(dict(owner_row))
            
        if owner:
            new_owner = [prefix_remove('owner_', owner) for owner in owner]
            
            return new_owner, 200
        else:
            return {"error": "Nenhum owner encontrado"}, 404

    except sqlite3.Error as e:  
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error: 
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owner/<int:id>", methods=["GET"])
def get_one(id):

    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM owner WHERE owner_id = ? AND owner_status = 'on'", (id,))
        owner_row = cursor.fetchone()
        conn.close()
        if owner_row:

            owner = dict(owner_row)
            new_owner = prefix_remove('owner_', owner)
            return new_owner, 200
        else:
            return {"error": "Owner não encontrado"}, 404

    except sqlite3.Error as e:  
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:  #
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route('/owner', methods=["POST"])
def create():

    try:
        new_owner = request.get_json()
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        sql = "INSERT INTO owner (owner_name, owner_email, owner_password, owner_birth) VALUES (?, ?, ?, ?)"

        sql_data = (
            new_owner['name'],
            new_owner['email'],
            new_owner['password'],
            new_owner['birth']
        )
        
        cursor.execute(sql, sql_data)
        inserted_id = int(cursor.lastrowid)
        conn.commit()
        conn.close()

        return {"success": "Registro criado com sucesso", "id": inserted_id}, 201

    except json.JSONDecodeError as e:  # Erro ao obter dados do JSON.
        return {"error": f"Erro ao decodificar JSON: {str(e)}"}, 500

    except sqlite3.Error as e:  # Erro ao processar banco de dados.
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:  # Outros erros.
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owner/<int:id>", methods=["DELETE"])
def delete(id):

    
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM owner WHERE owner_id = ? AND owner_status = 'on'", (id,))

        owner_row = cursor.fetchone()
    
        if owner_row:

            sql = "UPDATE owner SET owner_status = 'off' WHERE owner_id = ?"
            cursor.execute(sql, (id,)) 
            conn.commit()
            conn.close()
            return {"success": "Registro apagado com sucesso", "id": id}, 200
        else:      
            conn.close() 
            return {"error": "Owner não encontrado"}, 404
      
    except sqlite3.Error as e:  
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error: 
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owner/<int:id>", methods=["PUT", "PATCH"])
def edit(id):

    try:
        owner_json = request.get_json()
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        set_clause = ', '.join([f"owner_{key} = ?" for key in owner_json.keys()])
        sql = f"UPDATE owner SET {set_clause} WHERE owner_id = ? AND owner_status = 'on'"
        cursor.execute(sql, (*owner_json.values(), id))
        conn.commit()
        conn.close()

        return {"success": "Registro atualizado com sucesso", "id": id}, 201

    except sqlite3.Error as e:  # Erro ao processar banco de dados.
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as e:  # Outros erros.
        return {"error": f"Erro inesperado: {str(e)}"}, 500

@app.route("/item_owner/<int:id>", methods=["GET"])   
def item_owner(id):

    
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM item WHERE item_status != 'off'  AND item_owner = ?", (id,))

        item_row = cursor.fetchone()
    
        if item_row:
            conn.close()    
          
            return dict(item_row), 200
        else:      
            conn.close() 
            return {"error": "Item não encontrado"}, 404
      
    except sqlite3.Error as e:  
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error: 
        return {"error": f"Erro inesperado: {str(error)}"}, 500

@app.route("/owner_item/<int:id>", methods=["GET"])   
def owner_item(id):

    
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM owner INNER JOIN item ON owner_id = item_owner WHERE item_status != 'off' AND item_id = ? ;", (id,))

        item1_row = cursor.fetchone()
    
        if item1_row:
            conn.close()    
          
            return dict(item1_row), 200
        else:      
            conn.close() 
            return {"error": "Item não encontrado"}, 404
      
    except sqlite3.Error as e:  
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error: 
        return {"error": f"Erro inesperado: {str(error)}"}, 500


# Roda aplicativo Flask.
if __name__ == "__main__":
    app.run(debug=True)