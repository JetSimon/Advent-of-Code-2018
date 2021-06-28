import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def getDate(s):
    return s[1:s.find("]")]

def getMin(s):
    split = s.find(":")
    return int(s[split+1:split+3])

def getGuard(s):
    return int(s.split("]")[1].replace(" Guard #","").replace(" begins shift",""))

def getMostSleep(guards):
    best = None
    mostTime = 0
    for key in guards:
        g = guards[key]
        if len(g) > mostTime:
            mostTime = len(g)
            best = [key,g]
    return best

def getMostFreq(arr):
    best = None
    bestCount = 0
    for n in set(arr):
        c = arr.count(n)
        if c > bestCount:
            best = n
            bestCount = c
    return best, bestCount

def sortData():
    return sorted(data, key=getDate)

def rangeAsList(start, end):
    out = []
    for n in range(start, end):
        out.append(n)
    return out

def solve_1(data):
    data = sortData()
    guards = {}
    currentGuard = None
    asleep = False
    sleepTime = 0
    for entry in data:
        if "Guard" in entry:
            currentGuard = getGuard(entry)
            if currentGuard not in guards:
                guards[currentGuard] = []
        if "asleep" in entry:
            asleep = True
            sleepTime = getMin(entry)
        if "wakes up" in entry and asleep:
            asleep = False
            guards[currentGuard] += rangeAsList( sleepTime , getMin(entry) )
    
    g = getMostSleep(guards)   
    f = getMostFreq(g[1])
    return g[0] * f 

def solve_2(data):
    data = sortData()
    guards = {}
    currentGuard = None
    asleep = False
    sleepTime = 0
    for entry in data:
        if "Guard" in entry:
            currentGuard = getGuard(entry)
            if currentGuard not in guards:
                guards[currentGuard] = []
        if "asleep" in entry:
            asleep = True
            sleepTime = getMin(entry)
        if "wakes up" in entry and asleep:
            asleep = False
            guards[currentGuard] += rangeAsList( sleepTime , getMin(entry) )
    
    best = None
    min = None
    freq = 0
    for key in guards:
        g = guards[key]  
        f, c = getMostFreq(g)
        if c > freq:
            freq = c
            best = key
            min = f
    return best * min

print(solve_1(data))
print(solve_2(data))