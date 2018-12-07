class Guard():
    def __init__(self, id, sleepTime = 0):
        self.id = id
        self.sleepIntervals = []

    def __str__(self):
        return str(self.sleepIntervals)

g = {}
indata = open("sorted_indata.txt", "r")
for line in indata:
    logList = line.strip().split(" ")
    if logList[2] == "Guard":
        guardID = logList[3][1:]
        
        if guardID not in g.keys():
            g[guardID] = Guard(guardID)
    elif logList[2] == "falls":
        sleepStart = int(logList[1][ 3:5 ])        
    elif logList[2] == "wakes": 
        g[guardID].sleepIntervals.append({x for x in range(sleepStart, int(logList[1][ 3:5 ]))})
indata.close()        
guardMaxMin = []
for key in g:
    minCount = [0]*60
    for mInterval in g[key].sleepIntervals:
        for m in mInterval:
            minCount[m]+= 1
        maxMin = max(minCount)
        maxMinIndex = [index for index, minuite in enumerate(minCount) if minuite == maxMin ][0]
        guardMaxMin.append((key, maxMinIndex, maxMin ))
        #guardMaxMin.append((key, maxVal, ))
guardMaxMin.sort(key = lambda m: m[2], reverse = True)
print(int(guardMaxMin[0][0]) * guardMaxMin[0][1] )