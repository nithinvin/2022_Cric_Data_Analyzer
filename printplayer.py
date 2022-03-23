def update_batters_scoreboard(overs_data, batter_scoreboard):
    for overs in overs_data:
        for key, value in overs.items():
            if key == "deliveries":
                for delivery in value:
                    if delivery["batter"] not in batter_scoreboard.keys():
                        batter_scoreboard[delivery["batter"]] = 0

                    batter_scoreboard[delivery["batter"]] += delivery["runs"]["batter"]
                        #deliveries_faced += 1

    #print("Runs scored by", batter_to_print, "is", runs_by_batter, "in", deliveries_faced, "balls")  


def main():
    import json
    import os
    batter_scoreboard = {}
    season_2021 = "F:\\Nithin_cricdata\\JSON\\2021"
    for match in os.listdir(season_2021):
        f = open(season_2021 + "\\" + match, "r")
        data = json.load(f)

        overs_data = data["innings"][0]["overs"]
        update_batters_scoreboard(overs_data, batter_scoreboard)
        overs_data = data["innings"][1]["overs"]
        update_batters_scoreboard(overs_data, batter_scoreboard)

        f.close()

    sorted_scoreboard = sorted([(runs, batter) for (batter, runs) in batter_scoreboard.items()], reverse = True)
    orange_cap_holder = {}    
    for batter_data in sorted_scoreboard:
        print("Runs scored by", batter_data[1], "is", batter_data[0])
    
    print("\n", sorted_scoreboard[0][1], "is holding the orange cap by scoring", sorted_scoreboard[0][0], "runs, when", len(sorted_scoreboard), "batters played in the tournament")

main()