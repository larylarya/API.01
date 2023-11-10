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

     for item in items:
        if item.get("id") == id:
            return json.dumps(item, indent=2)

# print(get_all())
print(get_one(4))
