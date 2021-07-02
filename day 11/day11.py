import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def power(serial,x,y):
    id = x + 10
    power = id * y
    power += serial
    power *= id
    if len(str(power)) < 3:
        power = 0
    else:
        power = int(str(power)[-3])
    return power - 5

def gridPower(serial,x,y, sq=3):
    fuelPower = 0
    for i in range(y,y+sq):
        for j in range(x, x+sq):
            fuelPower += power(serial,j,i)
    return fuelPower

def solve_1(serial, w,h):
    largest = 0
    largestCoord = (0,0)
    for y in range(1,h-3):
        for x in range(1,w-3):
            fuelPower = gridPower(serial,x,y)
            if fuelPower > largest:
                largest = fuelPower
                largestCoord = (x,y)
    return largestCoord
            
            

def solve_2(serial, w, h):
    largest = 0
    largestCoord = (0,0,0)
    for sq in range(1,301):
        print(largest, largestCoord)
        print(sq,"/300")
        for y in range(1,h+1):
            if y + sq > 300:
                continue
            for x in range(1,w+1):
                if x + sq > 300:
                    continue
                #print(y,x)
                fuelPower = gridPower(serial,x,y,sq)
                if fuelPower > largest:
                    largest = fuelPower
                    largestCoord = (x,y,sq)
    return largestCoord

print(solve_2(1309,300,300))