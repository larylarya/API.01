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

    }
]

def get_all():
    var_json = json.dumps(items, indent=4)
    print(var_json)

def get_one(id):
    var_json = json.dumps(items[id] , indent=4)
    print(var_json)

#get_all()
get_one(1)