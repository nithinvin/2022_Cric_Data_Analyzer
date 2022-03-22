import json
f = open("F:\\Nithin_cricdata\\JSON\\2021\\1254117.json", "r")

data = json.load(f)

batter_to_print = "F du Plessis"
runs_by_batter = 0
deliveries_faced = 0

overs_data = data["innings"][0]["overs"]
for overs in overs_data:
    for key, value in overs.items():
        if key == "deliveries":
            for delivery in value:
                #print(delivery)
                #print(delivery["batter"])
                #print(delivery["runs"]["batter"])
                if delivery["batter"] == batter_to_print:
                    runs_by_batter += delivery["runs"]["batter"]
                    deliveries_faced += 1

print("Runs scored by", batter_to_print, "is", runs_by_batter, "in", deliveries_faced, "balls")
    #print(type(overs["deliveries"]))

    #print(overs)
        

f.close()