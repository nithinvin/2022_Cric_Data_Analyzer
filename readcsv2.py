file_handle = open("F:\\Nithin_cricdata\csv2\ipl_male_csv2\\1254117.csv", "r")
ball_no = 15
Lines = file_handle.readlines()
count = 0
striker_name = ""
for line in Lines:
    count += 1
    if count == ball_no + 1:
        field_count = 0
        for char in line:
            if (char == ','):
                field_count += 1
                if field_count == 9:
                    break
            else:
                if field_count == 8:
                    striker_name += char
        #print("Line{}: {}".format(count, line.strip()))
        print ("Striker is", striker_name)