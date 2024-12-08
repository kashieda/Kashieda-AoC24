import re
        
with open("day7_test.txt") as f:
    inp = [line.rstrip() for line in f]

correct = 0

for l in range(len(inp)):
    line = inp[l]
    
    p = line.split(": ")
    result = int(p[0])

    print(line)
    print(result)

exit()    
obs = set()
m = len(map)

for l in range(m):
    o = [i for i, ltr in enumerate(map[l]) if ltr == "#"]
    for gnn in o:
        obs.add((l, gnn))
    if "^" in map[l]:
        y = l
        x = map[l].find("^")
        d = 0

[vp, klar] = finishing(obs, x, y, d, m)
print(len(vp))

loops = 0

for i in range(1, len(vp)):
    nobs = obs.copy()
    
    this = vp[i]
    #print("Placing obstacle at: " + str(this))

    nobs.add((vp[0], vp[1]))
    
    klar = p2(nobs, x, y, d, m)

    #print(len(x))
    
    if klar:
        loops += 1
        print("Found a loop!")

    #input("pause")
print(loops)
    
