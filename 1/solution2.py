indata = open("input.txt", "r")
indata = indata.readlines()
res = 0
d = {}

def fun(indata, res, d):
    print(indata)
    while True:
        for line in indata:
            try:
                res2 = d[res]
                return res2
            except KeyError:
                d[res] = res
                if line[0] == "+":
                    res += int(line[1:])
                else:
                    res -= int(line[1:])
print(fun(indata, res, d))