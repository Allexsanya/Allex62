import json

user = {
    "id": 22,
    "name": "Олекс",
    "hobbies": ["tennis", "socceer"],
    "is_married": True,
    "address": {
        "city": "Odesa",
        "street": "Gogolya",
        "building": 15,
    },
    "siblings": None,
    "money": 100,
    0: 555,
}

# dict to string
result_string = json.dumps(user, ensure_ascii=False)


# string to dict
recover_dict = json.loads(result_string)

# dict to file
with open("user.json", mode="w") as file:
    json.dump(user, file, indent=4)

# file into dict
with open("user.json", mode="r", encoding="utf-8") as file:
    decover_from_file = json.load(file)
pass
