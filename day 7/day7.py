from copy import deepcopy
import itertools, re

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out

data = loadData()

def getSteps():
    out = {}
    reqs = set()
    for line in data:
        req = line.split(" must be")[0].replace("Step ", "")
        step = line.split("before step ")[1].replace(" can begin.", "")
        reqs.add(req)
        if step not in out:
            out[step] = [req]
        else:
            out[step].append(req)
    return out, reqs

def solve_1():
    inst, reqs = getSteps()
    doneAlready = sorted(list(reqs - set(inst.keys())))
    todo = list(inst.keys()) + doneAlready
    steps = sorted(  list(inst.keys()) + doneAlready)

    answer = ""
    while(len(todo) > 0):
        #print(todo)
        for step in steps:
            if step in todo:
                add = True
                if step in inst:
                    for req in inst[step]:
                        if req in todo:
                            add = False
                            break
                
                if add:
                    todo.remove(step)
                    answer += step
                    break
    return answer
def solve_2():
    time = -1
    workers = 5
    delay = 60
    q = {}
    inst, reqs = getSteps()
    doneAlready = sorted(list(reqs - set(inst.keys())))
    todo = list(inst.keys()) + doneAlready
    steps = sorted(  list(inst.keys()) + doneAlready)
    answer = ""
    while(len(todo) > 0 or len(q) > 0):
        time += 1
        print(q)
        cp = deepcopy(q)
        for key in q:
            if q[key] <= 1:
                workers += 1
                answer += key
                del cp[key]
                continue
            cp[key] -= 1
        q = cp
        for step in steps:
            if step in todo:
                add = workers > 0
                if step in inst:
                    for req in inst[step]:
                        if req in todo or req in q:
                            add = False
                            break
                
                if add:
                    workers -= 1
                    todo.remove(step)
                    q[step] = 1 + delay + ord(step) - ord('A')
    return answer, time

print(solve_2())

