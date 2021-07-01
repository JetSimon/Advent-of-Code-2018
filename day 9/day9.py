import itertools, re
from math import floor

def loadData():
    f = open('input.txt')
    out = [line.strip() for line in f]
    f.close()
    return out


data = loadData()
lastPer = 0
def solve_1(playerAmount, final):
    global lastPer
    pos = 0
    board = [0]
    players = [0] * playerAmount
    playerIndex = 0
    for i in range(1,final+1):
        per = floor((i / final) * 100)
        if per != lastPer:
            lastPer = per
            print(per,"% done")
        if i % 23 != 0:
            pos = ((pos + 1) % len(board)) + 1
            board.insert(pos, i)
        else:
            players[playerIndex % len(players)] += i + board[pos-7]
            del board[pos - 7]
            pos = pos - 7
            if pos < 0:
                pos += len(board)+1
        playerIndex += 1
        #print("[" + str(i) + "]", board, "current: ", board[pos])
    print(max(players))

def solve_2():
    pass

print( solve_1(424, 71482* 100) )