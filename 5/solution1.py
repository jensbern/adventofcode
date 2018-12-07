
def destroy(a, b):
    return (abs(ord(a) - ord(b))) == 32

indata = open("indata_test.txt", "r")
poly = indata.readline().strip()
def cleanup(poly):
    res = ""
    i = 1
    while i < len(poly):
        if destroy(poly[i-1], poly[i]):
            i+=2
        else:
            i+=1
        if i < len(poly):
            res += poly[i]
    return res

for i in range(10):
    print(poly)
    poly = cleanup(poly)


