import re




def finishing(xmap):
    onmap = True
    
    pos = []
    for l in range(len(xmap)):
        if "^" in map[l]:
            pos.append([l, map[l].index("^"), 0])
            vpos = [[l, map[l].index("^")]]
            map[l] = map[l].replace("^", ".")

    m = len(map[0])
    n = len(map)
    
    while onmap:
        #onmap = False
        if pos[-1][2] == 0: # Facing North
            if pos[-1][0] == 0:
                onmap = False
            else:
                npos = [pos[-1][0]-1, pos[-1][1], 0]
        elif pos[-1][2] == 1: # Facing East
            if pos[-1][1] == m-1:
                onmap = False
            else:
                npos = [pos[-1][0], pos[-1][1]+1, 1]
        elif pos[-1][2] == 2: # Facing South
            if pos[-1][0] == n-1:
                onmap = False
            else:
                npos = [pos[-1][0]+1, pos[-1][1], 2]
        else: # Facing West
            if pos[-1][1] == 0:
                onmap = False
            else:
                npos = [pos[-1][0], pos[-1][1]-1, 3]
                
                #print("Now at:  " + str(pos[-1]))
                #print("Going 2: " + str(npos))
    
        if onmap:
            #print(map[npos[0]][npos[1]])
            
            if map[npos[0]][npos[1]] == "#":
                npos = [pos[-1][0], pos[-1][1], (pos[-1][2]+1) % 4]
            elif not [npos[0], npos[1]] in vpos:
                vpos.append([npos[0], npos[1]])

            if npos in pos:
                return [pos, True]

            pos.append(npos)
        else:
            print("Leaving the area. Bye!")
            return [pos, False]
            break

        #input("Pause")
    
with open("day6.txt") as f:
    map = [line.rstrip() for line in f]

[skibidi, finish] = finishing(map)    

