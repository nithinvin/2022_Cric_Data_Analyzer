import csv
file = open("F:\\Nithin_cricdata\csv2\ipl_male_csv2\\1254117.csv", "r")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
lines = file.readlines()
print(lines[14])
#rows = []
#for row in csvreader:
 #   rows.append(row)
#print(rows)
file.close()