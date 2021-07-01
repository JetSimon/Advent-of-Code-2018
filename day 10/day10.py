import itertools, re
from copy import deepcopy
class Node():
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    def atTime(self,t):
        return self.x + (self.dx*t), self.y + (self.dy*t)

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def process(data):
    lowX = None
    lowY = None
    highX = None
    highY = None
    nodes = []
    grid = []

    for point in data:
        x = int( point.split("position=<")[1].split(",")[0] )
        y = int( point.split("position=<")[1].split(",")[1].split(">")[0] )
        dx = int( point.split("velocity=<")[1].split(",")[0] )
        dy = int( point.split("velocity=<")[1].split(",")[1].split(">")[0] )
        lowX = x if lowX == None or x < lowX else lowX
        lowY = y if lowY == None or y < lowY else lowY
        highX = x if highX == None or x > highX else highX
        highY = y if highY == None or y > highY else highY
        nodes.append( Node(x,y,dx,dy) )
    w = abs(lowX) + abs(highX)
    h = abs(lowY) + abs(highY)
    dw = w
    dh = h
    t = 0
    last = w*h
    print("finding close config...")
    while True:
        lowX = None
        lowY = None
        highX = None
        highY = None
        for node in nodes:
            x,y = node.atTime(t)
            lowX = x if lowX == None or x < lowX else lowX
            lowY = y if lowY == None or y < lowY else lowY
            highX = x if highX == None or x > highX else highX
            highY = y if highY == None or y > highY else highY
        t+=1
        #print(w*h)
        w = abs(lowX) + abs(highX)
        h = abs(lowY) + abs(highY)
        if w * h > last:
            h = dh
            w = dw
            print("optimal:", w * h)
            break
        last = w * h
        dw = w
        dh = h

    print("done finding points. making grid", w,"x",h)
    
    grid = [["." for x in range(w)] for y in range(h)] 
    return grid,nodes,t

def inGrid(grid, x, y):
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def solve_1(data):
    out = open("out.txt", "w")
    grid, nodes, startTime = process(data)
    print("done making grid")
    for t in range(startTime-27, startTime-10):
        print("t=",t)
        g = deepcopy(grid)
        for node in nodes:
            nx, ny = node.atTime(t)
            if inGrid(g,nx,ny):
                g[ny][nx] = "#"
        for row in g:
            out.write("".join(row) + "\n")
        out.write("\n")
def solve_2():
    pass

solve_1(data)