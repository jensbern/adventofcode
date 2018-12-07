indata = open("indata.txt")
d = {}
d2 = {}
#1 @ 56,249: 24x16
#2 @ 682,730: 13x20
#3 @ 774,241: 22x23
for line in indata:
    line=line.strip().split(" ")
    claim = line[0][1:]
    
    cords = line[2].split(",")
    cords[1] = cords[1][:-1]
    cords = [int(x) for x in cords]
    size = [int(x) for x in line[3].split("x")]
    d2[claim] = [cords, size]
    #print(cords, size)
    for x in range(size[0]):
        for y in range(size[1]):
            try:
                d[f'{cords[0]+x},{cords[1]+y}'] += 1
            except KeyError:
                d[f'{cords[0]+x},{cords[1]+y}'] = 1
res = 0
for key in d2:
    keysum = 0
    #print(d2[key])
    for x in range(d2[key][1][0]):
        for y in range(d2[key][1][1]):
            keysum += d[f'{d2[key][0][0]+x},{d2[key][0][1]+y}']
    if keysum == d2[key][1][0]*d2[key][1][1]:
        print(key)
