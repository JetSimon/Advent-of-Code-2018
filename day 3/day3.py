import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def printGrid(grid):
    for row in grid:
        print(row)

def makeGrid(n, initial=0):
    grid = []
    for i in range(n):
        grid.append([initial]*n)
    return grid



def validPos(grid, x, y):
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0])

def fillRect(grid, x_start,y_start,width,height):
    for y in range(y_start,y_start+height):
        for x in range(x_start, x_start+width):
            if validPos(grid,x,y):
                grid[y][x] += 1

def fillRect2(grid, id, x_start,y_start,width,height,overlaps):
    for y in range(y_start,y_start+height):
        for x in range(x_start, x_start+width):
            if validPos(grid,x,y):
                if len(grid[y][x]) == 0:
                    grid[y][x] = [id]
                else:
                    overlaps[grid[y][x][0]] = True
                    overlaps[id] = True

def getGreaterThan(grid, n):
    count = 0
    for row in grid:
        for p in row:
            if p >= n:
                count +=1 
    return count

def getLoneID(grid, overlaps):
    for step in data:
        id = int(step.split("@")[0].replace("#","").strip())
        if id not in overlaps:
            return id

def solve_1():
    grid = makeGrid(1000)
    for step in data:
        x = int(step.split("@")[1].split(",")[0].strip())
        y = int(step.split("@")[1].split(",")[1].split(":")[0].strip())
        width = int(step.split("@")[1].split(",")[1].split(":")[1].split("x")[0].strip())
        height = int(step.split("@")[1].split(",")[1].split(":")[1].split("x")[1].strip())
        fillRect(grid,x,y,width,height)
    return getGreaterThan(grid,2)

def solve_2():
    grid = makeGrid(1000,[])
    overlaps={}
    for step in data:
        x = int(step.split("@")[1].split(",")[0].strip())
        y = int(step.split("@")[1].split(",")[1].split(":")[0].strip())
        width = int(step.split("@")[1].split(",")[1].split(":")[1].split("x")[0].strip())
        height = int(step.split("@")[1].split(",")[1].split(":")[1].split("x")[1].strip())
        id = int(step.split("@")[0].replace("#","").strip())
        fillRect2(grid,id,x,y,width,height,overlaps)
    #printGrid(grid)
    return getLoneID(grid, overlaps)

print(solve_2())