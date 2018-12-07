from datetime import datetime, timedelta

class Guardlog():
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message
    
    def __str__(self):
        return str(self.timestamp)+ " " + self.message

class Guard():
    def __init__(self, id, sleepTime = timedelta(0), timesAsleep = 0):
        self.id = id
        self.sleepTime = sleepTime
        self.timesAsleep = timesAsleep

    def __str__(self):
        return self.id + ": " + str(self.sleepTime)


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
for log in logs:
    logList = log.message.split(" ")
    if logList[0] == "Guard":
        if guard != None:
            guards.append(guard)
        guardID = logList[1][1:]
        guard = Guard(guardID)
    elif logList[0] == "falls":
        guard.timesAsleep+= 1
        sleepStart = log.timestamp
    elif logList[0] == "wakes": 
        guard.sleepTime += log.timestamp - sleepStart  

guards.sort(key=lambda g: g.sleepTime, reverse = True)
sleepyGuard = guards[0]

print( int(guards[0].id) * (((sleepyGuard.sleepTime.seconds%3600)//60) -sleepyGuard.timesAsleep ))