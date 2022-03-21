import json
f = open("F:\\Nithin_cricdata\\JSON\\2021\\1254117.json", "r")

data = json.load(f)
for i in data["info"]["outcome"]:
    print(i)

f.close()