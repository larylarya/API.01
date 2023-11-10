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
    return json.dumps(items, indent=2)

def get_one(id):
    var_json = json.dumps(items[id] , indent=1)
    return var_json

#print(get_all())
print(get_one(1))