# coding=utf-8
import csv

COUNTRY_NAME = ""  # must be one in global_data.csv

rows = [["id", "cases"]]

with open("global_data.csv", "r") as f:
    data = csv.reader(f)
    for line in data:
        if line[0] == "date":
            for i, j in zip(line, range(len(line))):
                if i == "United States":
                    index = j
            continue
        rows.append([data.line_num-1, int(float(line[index])) if line[index] != "" else 0])

with open("processed_data.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
