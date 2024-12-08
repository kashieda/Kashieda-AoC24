import re




def finishing(xmap):
    onmap = True

    #for l in range(len(xmap)):
        #print(xmap[l])
        
    pos = []
    for l in range(len(xmap)):
        if "^" in xmap[l]:
            pos.append([l, xmap[l].index("^"), 0])
            vpos = [[l, xmap[l].index("^")]]
            xmap[l] = xmap[l].replace("^", ".")
            #print(vpos)
            break

    m = len(xmap[0])
    n = len(xmap)

    #for l in range(len(xmap)):
        #print(xmap[l])
    
    #print(pos)
    
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
            
            if xmap[npos[0]][npos[1]] == "#":
                npos = [pos[-1][0], pos[-1][1], (pos[-1][2]+1) % 4]
            elif not [npos[0], npos[1]] in vpos:
                vpos.append([npos[0], npos[1]])

            if npos in pos:
                return [vpos, True]

            pos.append(npos)
        else:
            print("Leaving the area. Bye!")
            return [vpos, False]
            break        
    
with open("day6.txt") as f:
    oldmap = [line.rstrip() for line in f]
    map = oldmap.copy()
    
[visited, finish] = finishing(map)    

loops = 0

for i in range(1, len(visited)):
    nmap = oldmap.copy()

    obs = visited[i]
    print("Placing obstacle at: " + str(obs))

    #print(nmap[obs[0]])
    nmap[obs[0]] = nmap[obs[0]][:obs[1]] + "#" + nmap[obs[0]][(obs[1]+1):]

    #print(nmap[obs[0]])
    [x, klar] = finishing(nmap)

    #print(len(x))
    
    if klar:
        loops += 1
        print("Found a loop!")

    #input("pause")
print(loops)
    
