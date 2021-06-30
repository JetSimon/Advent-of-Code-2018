import itertools, re
class Node():
    def __init__(self, metadata, children):
        self.metadata = metadata
        self.children = children

def loadData():
    f = open('input.txt')
    for line in f:
        out = line.split(" ")
    f.close()
    return out

data = loadData()
i = 0
metasum = 0
def solve_1():
    #print("new node")
    global i, metasum
    if i > len(data):
        return
    childAmount = int(data[i])
    metaAmount = int(data[i + 1])
    i += 2
    children = []
    #print("children #:",childAmount, "meta #:",metaAmount)
    for n in range(childAmount):
        children.append(solve_1())
    metadata = data[i:i+metaAmount]
    metasum += sum([int(m) for m in metadata])
    i += metaAmount
    node = Node(metadata, children)
    return node

def solve_2(root):
    if len(root.children) == 0:
        return sum([int(n) for n in root.metadata])
    val = 0

    for n in [int(i) for i in root.metadata]:
        if n > 0 and n <= len(root.children):
            val += solve_2(root.children[n-1])
    
    return val

root = solve_1()

print(solve_2(root))