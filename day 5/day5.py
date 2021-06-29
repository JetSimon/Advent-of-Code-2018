import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def removeAll(s,i):
    out = ""
    for c in s:
        if c.lower() == i.lower():
            continue
        out += c
    return out

def destroyPolarity(s):
    out = ""
    skip = False
    for i in range(len(s)):
        if i == len(s) - 1:
            if not skip:
                out += s[i]
            break
        c = s[i]
        n = s[i+1]
        if not skip:
            if c.lower() == n.lower() and ( (c.isupper() and n.islower()) or (c.islower() and n.isupper()) ):
                skip = True
            else:
                out += c
        else:
            skip = False
    return out

def reactionLen(s):
    n = destroyPolarity(s)
    while n != s:
        s = n
        n = destroyPolarity(s)
    return len(n)

def solve_1(s):
    n = destroyPolarity(s)
    while n != s:
        s = n
        n = destroyPolarity(s)
    return n

def solve_2(s):
    shortest = len(s)
    removed = None
    for c in set(s.lower()):
        t = removeAll(s,c)
        att = reactionLen(t)
        if att < shortest:
            shortest = att
            removed = c
        print("done")
    return shortest

print(solve_2(data[0]))