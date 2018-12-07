indata = open("indata.txt", "r").readlines()


def f(indata):
    for line1 in indata:
        line1 = line1.strip()
        for line2 in indata:
            line2 = line2.strip()
            diff = 0
            diff_index = None
            for c in range(len(line1)):
                #print(c)
                if ord(line1[c])!=ord(line2[c]):
                    diff += 1
                    diff_index = c
            if diff == 1:
                return line1, line2, diff_index

l1, l2, c = f(indata)
print(l1)
print(l2)
#asgwjcmzredihqoutcylvzinx