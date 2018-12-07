import re
indata = open("indata.txt")
d = {}
#1 @ 56,249: 24x16
#2 @ 682,730: 13x20
#3 @ 774,241: 22x23
for line in indata:
    line=line.strip().split(" ")
    cords = line[2].split(",")
    cords[1] = cords[1][:-1]
    cords = [int(x) for x in cords]
    size = [int(x) for x in line[3].split("x")]
    #print(cords, size)
    for x in range(size[0]):
        for y in range(size[1]):
            try:
                d[f'{cords[0]+x},{cords[1]+y}'] += 1
            except KeyError:
                d[f'{cords[0]+x},{cords[1]+y}'] = 1
res = 0
for key in d:
    if(d[key] > 1):
        res += 1
print(res)