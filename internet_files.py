import requests

#
# url = "https://www.ukr.net/"
#
# response = requests.get(url)
# # print(response.content)
# print(response.text)
# with open("ukr.html", mode="w", encoding="utf-8") as file:
#     file.write(response.text)
# pass


url = (
    "https://static-cse.canva.com/blob/1218652/feature_StockImages_hero2x.b2c8064f.jpg"
)
response = requests.get(url)
content = response.content
with open("ed.jpg", mode="bw") as file:
    file.write(content)
