import requests

url = "https://dummyjson.com/products?limit=194&skip=4"
TARGET_BRAND = "Apple"

response = requests.get(url)
response_lson = response.json()
products = response_lson["products"]

count = 0
total_cost = 0
for product in products:
    if product.get("brand", "").lower() == TARGET_BRAND.lower():
        count += 1
        cost = product["price"] * product["stock"]
        total_cost += cost
print(f"{total_cost}, {count=}")

pass
