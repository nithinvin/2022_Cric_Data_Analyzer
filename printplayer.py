import json
f = open("F:\\Nithin_cricdata\\JSON\\2021\\1254117.json", "r")

data = json.load(f)
overs_data = data["innings"][0]["overs"]
for overs in overs_data:
    for key, value in overs.items():
        print(key, ":", value)
    #print(type(overs["deliveries"]))
    #print(overs)
        

f.close()