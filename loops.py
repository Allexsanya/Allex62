# some_list = [55, 666] * 6
# some_string = "ghvgc323kfjvgfeg"
#
# products = ["banana", "mlk", "bread", "vodka"]
#
# for product in products:
#
#     if product == "milk":
#         break
#
#     if product == "vodka":
#         continue
#
#     print(product)
#     if product == "vodka":
#         print("no booze today")
from pprint import pprint

print(8888888)
people = [
    ["Alex", "Bert", "Odesa", 35, True, 3584153],
    ["Petr", "Somov", "Kyiv", 40, False, 79879789],
    ["Alex", "Scheka", "Lwiw", 65, True, 65456465],
    ["Ostap", "Vishnya", "Ternopil", 15, False, 1321321],
    ["Alex", "Berkut", "Kyiv, Loban", 44, True, 7411441],
    ["Olga", "Frolova", "Vinnytsia", 28, False, 3132132132132],
    ["Alex", "Gopstop", "Kiyv", 56, True, 963366963],
]

# all married people
# not married from Kyiv
# average age of married people
all_married_people = []
not_married_from_city = []
city = "Kiyv"

total_age = 0


############################
for person in people:
    name, surname, address, age, is_married, inn = person

    # is_married = person[4]
    # address = person[2].lower()
    # address = address.lower()
    if is_married:
        print(person)
        all_married_people.append(person)
    if not is_married and city.lower() in address.lower():
        not_married_from_city.append(person)

if all_married_people:
    ages = []
    for married_person in all_married_people:
        age = married_person[3]
        total_age += age

        #   option 2
        ages.append(age)

    print(f"Average age of marriedf = {total_age/len(all_married_people)}")
    print(f"Average age of marriedf = {sum(ages)/len(all_married_people)}")
print("all married")
pprint(all_married_people)
print(f"not married from{city}")
pprint(not_married_from_city)
##########################
# for person in people:
#     # ["Alex", "Bert", "Odesa", 35, True, 3584153]
#     is_married = person[4]
#     if is_married:
#         print(person)
#         all_married_people.append(person)
# pprint(all_married_people)

# not_married_from_city = []
# city = "Kyiv"
# for person in people:
#     # ["Alex", "Bert", "Odesa", 35, True, 3584153]
#     is_married = person[4]
#     address = person[2].lower()
#     if not is_married and city.lower() in address:
#         not_married_from_city.append(person)
# pprint(not_married_from_city)


# WARNINGS

list_data = [55, 46]
for number in list_data:
    print(number)
    new_number = number * 2
    list_data.append(new_number)
