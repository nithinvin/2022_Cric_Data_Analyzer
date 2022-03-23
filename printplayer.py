def print_batters_scoreboard(overs_data):
    batter_scoreboard = {}    
    for overs in overs_data:
        for key, value in overs.items():
            if key == "deliveries":
                for delivery in value:
                    if delivery["batter"] not in batter_scoreboard.keys():
                        batter_scoreboard[delivery["batter"]] = 0

                    batter_scoreboard[delivery["batter"]] += delivery["runs"]["batter"]
                        #deliveries_faced += 1

    #print("Runs scored by", batter_to_print, "is", runs_by_batter, "in", deliveries_faced, "balls")
    for batter, runs in batter_scoreboard.items():
        print("Runs scored by", batter, "is", runs)


def main():
    import json
    f = open("F:\\Nithin_cricdata\\JSON\\2021\\1254117.json", "r")
    data = json.load(f)

    overs_data = data["innings"][0]["overs"]
    print_batters_scoreboard(overs_data)
    overs_data = data["innings"][1]["overs"]
    print_batters_scoreboard(overs_data)

    f.close()

main()