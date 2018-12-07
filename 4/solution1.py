from datetime import datetime, timedelta

class Guardlog():
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message
    
    def __str__(self):
        return str(self.timestamp)+ " " + self.message

class Guard():
    def __init__(self, id, sleepTime = 0):
        self.id = id
        self.sleepTime = sleepTime
        self.sleepIntervals = []

    def __str__(self):
        return str(self.sleepTime) + ": " + str(self.sleepIntervals)


indata = open("indata.txt", "r")
logs = []
for line in indata:
    line = line.strip().split("] ")
    time = line[0][1:]
    dt = datetime(int(time[:4]), int(time[5:7]), int(time[8:10]),int(time[11:13]), int(time[14:16]) )        
    logs.append(Guardlog(dt, line[1]))

guards = []
guard = None
logs.sort(key = lambda x: x.timestamp)
"""
sortedFile = open("sorted_indata.txt", "w")
for l in logs:
    sortedFile.write(str(l)+"\n")
sortedFile.close()
"""
g = {}

for log in logs:
    logList = log.message.split(" ")
    if logList[0] == "Guard":
        guardID = logList[1][1:]
        if guardID not in g.keys():
            g[guardID] = Guard(guardID)
    elif logList[0] == "falls":
        sleepStart = log.timestamp.minute
    elif logList[0] == "wakes": 
        g[guardID].sleepIntervals.append({x for x in range(sleepStart, log.timestamp.minute)})
        g[guardID].sleepTime += log.timestamp.minute  - sleepStart  

#for key in g:
#    print(key, str(g[key]))

guardList = [guard for guard in g.values()]
guardList.sort(key= lambda g:g.sleepTime, reverse = True)
minuite_list = [0]*60
for intervals in guardList[0].sleepIntervals:
    for m in intervals:
        minuite_list[m]+=1

maxMin = max(minuite_list)
maxMinIndex = [index for index, minuite in enumerate(minuite_list) if minuite == maxMin ]

print(maxMinIndex[0]*int(guardList[0].id))
"""
guards.sort(key=lambda g: g.sleepTime, reverse = True)
for interval in guards[0].sleepIntervals:
    print(interval)
print( int(guards[0].id))
"""