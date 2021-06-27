import itertools, re

def loadData():
    f = open('input.txt')
    out = [int(line.strip()) for line in f]
    f.close()
    return out

data = loadData()

def solve_1(data):
    return sum(data)

def solve_2(data):
    seen = {0:True}
    f = 0
    i = 0
    while True:
        n = data[i]
        f += n
        if f in seen:
            return f
        seen[f] = True
        i += 1
        if i >= len(data):
            i = 0

print(solve_1(data))
print(solve_2(data))