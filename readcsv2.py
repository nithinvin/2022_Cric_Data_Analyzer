ball_no = 15
striker_fieldno = 9
bowler_fieldno = 11
runs_of_bat_fieldno = 12
extras_fieldno = 13

file_handle = open("F:\\Nithin_cricdata\csv2\ipl_male_csv2\\1254117.csv", "r")
Lines = file_handle.readlines()

count = 0
striker_name = ""
bowler_name = ""
runs_of_bat = ""
extras = ""

for line in Lines:
    count += 1
    if count == ball_no + 1:
        field_count = 0
        for char in line:
            if (char == ','):
                field_count += 1                
            else:
                if field_count == striker_fieldno - 1:
                    striker_name += char
                if field_count == bowler_fieldno - 1:
                    bowler_name += char
                if field_count == runs_of_bat_fieldno - 1:
                    runs_of_bat += char
                if field_count == extras_fieldno - 1:
                    extras += char
        #print("Line{}: {}".format(count, line.strip()))
        if runs_of_bat:
            print("Striker", striker_name, "scored", runs_of_bat, "when", bowler_name, "bowled")
        else:
            print("Striker", striker_name, "faced", bowler_name, "while extras", extras, "were scored")
        