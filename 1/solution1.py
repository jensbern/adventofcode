indata = open("input.txt", "r")
res = 0
for line in indata:
    if line[0] == "+":
        res += int(line[1:])
    else:
        res -= int(line[1:])
print(res)