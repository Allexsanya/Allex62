from operator import index
from pprint import pprint


# creation

user = {
    "id": 22,
    "name": "Alex",
    "hobbies": ["tennis", "socceer"],
    "is_married": True,
    "address": {
        "city": "Odesa",
        "street": "Gogolya",
        "building": 15,
    },
    "siblings": None,
    "money": 100,
}
user2 = dict(id=365, name="John")
user3 = dict(id=3655, name="Marta", hobbies=None)

parcel = {}
parcel2 = dict()


# get data
# user_id = user["id"]
# user2_id = user2["id"]
#
# user_hobbies = user.get("hobbies", [])
# user2_hobbies = user2.get("hobbies", [])
# user3_hobbies = user3.get("hobbies") or []

# for hobby in user_hobbies:
#     print(f"user hobby -{hobby}")

# list type

# user2["hobbies"] = ["diving"]
# user2["hobbies"] = ["scuba"]
# user2["hobbies"].append("diving")
#
# # int type
# user["money"] += 200
#
# # dict type
# user["address"]["city"] = "Lviv"
# user["address"]["stree"] = "Oppa"
#
# pprint(user, indent=4)

#
user_address = {
    "city": "Odesa",
    "street": "Gogolya",
    "building": 15,
}
user_data = {
    "id": 18,
    "city": "Kyiv",
}
# result_dict_optional1 = {**user_address, **user_data}
# result_dict_optional2 = user_address | user_data
#
# print(result_dict_optional2 == result_dict_optional1)


# delete
result_dict_optional1.clear()


# delete value by key
del result_dict_optional2["street"]
city = result_dict_optional2.pop("city2", "")


# iterate
for elem in user:
    print(elem, "->", user[elem])


atlethes = []
for elem in scores.values:
    atleths.extend(elem)
print(atlethes)


pass
