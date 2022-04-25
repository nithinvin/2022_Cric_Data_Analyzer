def update_batters_scoreboard(overs_data, batter_scoreboard):
    for overs in overs_data:
        for key, value in overs.items():
            if key == "deliveries":
                for delivery in value:
                    if delivery["batter"] not in batter_scoreboard.keys():
                        batter_scoreboard[delivery["batter"]] = {"runs": 0, "sixes": 0, "fours": 0, "deliveries": 0}

                    batter_scoreboard[delivery["batter"]]["runs"] += delivery["runs"]["batter"]
                    if delivery["runs"]["batter"] == 6:
                        batter_scoreboard[delivery["batter"]]["sixes"] += 1
                    if delivery["runs"]["batter"] == 4:
                        batter_scoreboard[delivery["batter"]]["fours"] += 1
                    batter_scoreboard[delivery["batter"]]["deliveries"] += 1

                        #deliveries_faced += 1

    #print("Runs scored by", batter_to_print, "is", runs_by_batter, "in", deliveries_faced, "balls")  


def main():
    import json
    import os
    batter_scoreboard = {}
    season_2021 = "C:\\Nithin_Data\\Cric_data\\2022"
    matches = 0
    for match in os.listdir(season_2021):
        f = open(season_2021 + "\\" + match, "r")
        matches += 1
        data = json.load(f)

        overs_data = data["innings"][0]["overs"]
        update_batters_scoreboard(overs_data, batter_scoreboard)
        overs_data = data["innings"][1]["overs"]
        update_batters_scoreboard(overs_data, batter_scoreboard)

        f.close()

    sorted_scoreboard = sorted([(runs_data["runs"], batter) for (batter, runs_data) in batter_scoreboard.items()], reverse = True)    
    orange_cap_holder = {}
    playerno = 0
    for batter_data in sorted_scoreboard:
        playerno += 1
        total_runs = batter_scoreboard[batter_data[1]]["runs"]
        total_balls = batter_scoreboard[batter_data[1]]["deliveries"]
        total_sixes = batter_scoreboard[batter_data[1]]["sixes"]
        total_fours = batter_scoreboard[batter_data[1]]["fours"]
        strike_rate = round(total_runs / total_balls * 100, 2)
        print(playerno, "Runs scored by", batter_data[1], "is", total_runs , "(" + str(total_balls) + ")", "at SR " + str(strike_rate) + ", sixes - " + str(total_sixes) + ", fours -", total_fours)
        
    print("\n", sorted_scoreboard[0][1], "is holding the orange cap by scoring", sorted_scoreboard[0][0], "runs, when", len(sorted_scoreboard), "batters played in", matches, "matches in the tournament")    

main()