import json
items = [
    {
        "id": 1,
        "name": "Bagulho",
        "desciption": "Apenas um bagulho"
    }, {
        "id": 2,
        "name": "Tranqueira",
        "desciption": "Apenas um tranqueira qualquer",
        "location": "Em um gaveteiro"
    }, {
        "id": 3,
        "name": "Bagulete",
        "desciption": "Apenas um bagulete",
        "location": "Na esquina"

    }, {
        "id": 4,
        "name": "Lua",
        "desciption": "Apenas uma Lua",
        "location": "No ceu"

    }, {
        "id": 5,
        "name": "Flora",
        "desciption": "Apenas uma flora",
        "location": "No campo"

    }, {
        "id": 6,
        "name": "Solar",
        "desciption": "Apenas uma solar",
        "location": "No espaço"

    }
]


def get_all():   
    return json.dumps(items, indent=2)

def get_one(id):  

    try:
        id = int(id)  
        for item in items:  
            if item.get("id") == id:
                return json.dumps(item, indent=2)        
    except: 
        return False  

def new(json_data):
    #print('new →', json_data)

    max_id = max(item["id"] for item in items) + 1
    print('max →', max_id)
    return 

def get_data():
    
    input_id = input("Digite o ID do item: ")
    view = get_one(input_id)

    if view: 
        print(view)
    else:
        print("Algo errado não deu certo!")

# Chama (call) a função get_all().
# print(get_all())
#get_data()

my_json = ''' 
{
    "name": "Barata",
    "desciption": "Inseto",
    "location": "No lixo"
}
'''
new(my_json)


