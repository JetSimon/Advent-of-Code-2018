import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def times(s, counts):
    s = list(s)
    for c in set(s):
        count = s.count(c)
        if count in counts:
            counts[count] = True

def difference(a,b):
    same = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            same += a[i]
    return len(a) - len(same), same

def solve_1(data):
    three = 0
    two = 0
    for code in data:
        counts = {2:False, 3:False}
        times(code, counts)
        two += 1 if counts[2] else 0
        three += 1 if counts[3] else 0
    return two * three

def solve_2(data):
    for code in data:
        for other in data:
            n, same = difference(code, other)
            if n == 1:
                return same
    return None

print(solve_1(data))
print(solve_2(data))