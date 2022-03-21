import json
f = open("F:\\Nithin_cricdata\\JSON\\2021\\1254117.json", "r")

data = json.load(f)
outcome_data = data["info"]["outcome"]
for key, value in outcome_data.items():
    print(key, ":", value)

f.close()