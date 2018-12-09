indata = open("indata_test.txt", "r")
for line in indata:
    coords = [int(x) for x in (line.strip().split(", "))]
    print(coords)