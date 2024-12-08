import re
        
with open("day7.txt") as f:
    inp = [line.rstrip() for line in f]

correct = 0

for l in range(len(inp)):
    line = inp[l]
    
    p = line.split(": ")
    result = int(p[0])

    factors = p[1].split(" ")
    
    f = list(map(int, factors))

    op = 0

    undone = True

    while (undone and op < 2**((len(f)-1))):

        res = f[0]
        #print(res)
        
        for thisop in range(len(f)-1):
            #print((op & 2**thisop))
            if ((op & 2**thisop) != 0): # multiplying!
                #print(str(res) + "*" + str(f[thisop+1]))
                res *= f[thisop+1]

            else: # adding
                #print(str(res) + "+" + str(f[thisop+1]))
                res += f[thisop+1]

        if res == result:
            #print("This one is ok")
            correct += result
            undone = False
        #else:
            #print("Nope: " + str(res) + " /= " + str(result))
                        
        op += 1
        #input("Pause...")
    
print(correct)
exit()    
