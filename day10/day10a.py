import re, itertools, copy

class Pos:
    def __init__(self, x, y):
        self.x = y
        self.y = y

def dprint(*s):
    if DEBUG:
        print(*s)

def check(x, y, d, lvl):
    dprint(x,y,d,lvl)    
    
    if d == 'W':
        newx = x-1
    elif d == 'E':
        newx = x+1
    else:
        newx = x
        
    if d == 'N':
        newy = y-1
    elif d == 'S':
        newy = y+1
    else:
        newy = y

    if newx < 0:
        dprint("x too low")
        return False

    if newx > (B-1):
        dprint("x too large")
        return False

    if newy < 0:
        dprint("y too low")
        return False

    if newy > (H-1):
        dprint("y too large")
        return False

    dprint(f"{newx=}, {newy=}, height = {height[newx][newy]}")
    
    if lvl == height[newx][newy]:
        dprint("One closer!")
        return newx, newy

    dprint("Not the next level!")
    return False
    
DEBUG = False
        
with open("day10.txt") as f:
    inp = [line.rstrip() for line in f]

height = []



for l in range(len(inp)):
    thisline = inp[l]
    height.append([])
    for p in range(len(thisline)):
        #dprint(f"line {l} och position {p}")
        height[l].append(int(thisline[p]))

    print(height[l])

#print(height)

H = len(height)
B = len(height[0])

trails = 0

for y in range(H):
    print(f"Checking input line: {y}")
    for x in range(B):

        if height[x][y]==0:
            print(f"Possible start at {x}, {y}.")

            heads = []

            for d1 in ('W', 'N', 'E', 'S'):
                if np1 :=check(x, y, d1, 1):
                    x1 = np1[0]
                    y1 = np1[1]
                    dprint("Reached lvl 1!")
                    for d2 in ('W', 'N', 'E', 'S'):
                        if np2 := check(x1, y1, d2, 2):
                            x2 = np2[0]
                            y2 = np2[1]
                            dprint("Reached lvl 2!")
                            for d3 in ('W', 'N', 'E', 'S'):
                                if np3 := check(x2, y2, d3, 3):
                                    x3 = np3[0]
                                    y3 = np3[1]
                                    dprint("Reached lvl 3!")                    
                                    for d4 in ('W', 'N', 'E', 'S'):
                                        if np4 := check(x3, y3, d4, 4):
                                            x4 = np4[0]
                                            y4 = np4[1]
                                            for d5 in ('W', 'N', 'E', 'S'):
                                                if np5 := check(x4, y4, d5, 5):
                                                    x5 = np5[0]
                                                    y5 = np5[1]
                                                    for d6 in ('W', 'N', 'E', 'S'):
                                                        if np6 := check(x5, y5, d6, 6):
                                                            x6 = np6[0]
                                                            y6 = np6[1]
                                                            for d7 in ('W', 'N', 'E', 'S'):
                                                                if np7 := check(x6, y6, d7, 7):
                                                                    x7 = np7[0]
                                                                    y7 = np7[1]
                                                                    for d8 in ('W', 'N', 'E', 'S'):
                                                                        if np8 := check(x7, y7, d8, 8):
                                                                            x8 = np8[0]
                                                                            y8 = np8[1]
                                                                            for d9 in ('W', 'N', 'E', 'S'):
                                                                                if head := check(x8, y8, d9, 9):
                                                                                    if head not in heads:
                                                                                        heads.append(head)
                                                                                    #print(f"{np1}, {np2}, {np3}, {np4}, {np5}, {np6}, {np7}, {np8}, {head}") 

            print(heads)                                        
            trails += (len(heads))

print(trails)
            # kolla riktningar i ordning:
            # om kollade positionen har rätt nummer,
            #    kollar riktningar i ordning, ...
            #       om höjden är 9, spara positionen

            # gå igenom trails och sök efter duplikat
            #    hittat duplikat, ta bort. 
            # räkna antalet som är kvar
            

            
