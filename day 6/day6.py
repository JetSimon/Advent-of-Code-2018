import itertools, re

def loadData():
    f = open('input.txt')
    out = [(int(line.split(",")[0]),int(line.split(",")[1].strip())) for line in f]
    f.close()
    return out

data = loadData()

def getClosest(points, y, x):
    closest = None
    closestDist = None
    seen = {}
    for p in points:
        dist = abs(y - p[1]) + abs(x - p[0])
        if closestDist == None or dist < closestDist:
            closestDist = dist
            closest = p
        seen[dist] = 1 if dist not in seen else seen[dist] + 1
    if seen[closestDist] > 1:
        return None
    return closest 

def getLessThan(points, y, x, limit):
    closest = None
    closestDist = None
    s = 0
    for p in points:
        dist = abs(y - p[1]) + abs(x - p[0])
        if closestDist == None or dist < closestDist:
            closestDist = dist
            closest = p
        s += dist
    if s < limit:
        return p
    else:
        return None
        
def printGrid(grid):
    for row in grid:
        print(row)

def count(grid, c):
    s = 0
    for row in grid:
        for p in row:
            if p == c:
                s += 1
    return s

def solve_1(data):
    grid = []
    #f = open('out.txt','w')
    for y in range(350):
        row = []
        for x in range(350):
            d, p = getClosest(data, y, x)
            
            if d == None:
                row.append('.')
            else:
                c = chr(data.index(p) + ord('A'))
                row.append(c)
        #f.write("".join(row) + "\n")
        grid.append(row)
    lengths = {}
    for i in range(len(data)):
        c = chr(i + ord('A'))
        lengths[c] = count(grid, c)
    #printGrid(grid)
    print(lengths)
    #f.close()

def solve_2(data):
    grid = []
    f = open('out2.txt','w')
    for y in range(350):
        row = []
        for x in range(350):
            p = getLessThan(data, y, x, 10000)
            if p == None:
                row.append('.')
            else:
                c = chr(data.index(p) + ord('A'))
                row.append(c)
        f.write("".join(row) + "\n")
        grid.append(row)
    lengths = {}
    for i in range(len(data)):
        c = chr(i + ord('A'))
        lengths[c] = count(grid, c)
    #printGrid(grid)
    print(lengths)
    f.close()

print( solve_2(data) )