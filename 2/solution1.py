# https://adventofcode.com/2018/day/2
indata = open("indata.txt", "r")
twos = 0
threes = 0
for line in indata:
    d = {}
    two = False
    three = False
    for c in line:
        try:
            d[c]+= 1
        except KeyError:
            d[c] = 1
    for key in d:
        if d[key] == 2 and not two:
            twos+=1
            two = True
        elif d[key] == 3 and not three:
            three = True
            threes += 1
print(twos*threes)