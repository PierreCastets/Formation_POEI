import csv

cityNameIndex = 8
n = 0
with open("cities.csv", "r") as f:
    rows = csv.reader(f, delimiter = ",")
    for r in rows:
        if r[cityNameIndex].strip().strip("\"").startswith("San"):
            n += 1
    f.close()
f.close()
print(n)

