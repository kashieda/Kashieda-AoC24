import re, itertools, copy

def foo(l, n): ### Make all combinations of items in l of length n
     yield from itertools.product(*([l] * n))

def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

def add_an(addx, addy):
    in1 = True

    if an1y < m and 0<= an1y:
        #print("ok i y-led")
        if an1x < m and 0<= an1x:
            print((an1y, an1x))
            if (an1y, an1x) not in list(antinodes):
                print("Adding: " + str((an1y, an1x)))
                #print("inte redan med")
                antinodes.add((an1y, an1x))
            #else:
                #print("redan med")
        else:
            print("X1 too big!")
            in1 = False
    else:
        print("Y1 too big!")
        in1 = False

    return in1


with open("day8.txt") as f:
    inp = [line.rstrip() for line in f]

ants = set()
m = len(inp)


for l in range(m):
    reg = re.findall(r"[^.]", inp[l])
    if reg:
        for r in reg:
            ants.add(r)

antinodes = set()
            
for a in list(ants):
    #print(a)

    loc = []
    
    for l in range(m):
        if a in inp[l]:
            x = [i for i, ltr in enumerate(inp[l]) if ltr in a]
            for thisx in x:
                loc.append([l, thisx])
                antinodes.add((l, thisx))

            for thisl in range(len(loc)-1):
                for thatl in range((thisl+1), len(loc)):
                    #print([loc[thatl], loc[thisl]])
                    
                    dy = loc[thatl][0] - loc[thisl][0]
                    dx = loc[thatl][1] - loc[thisl][1]

                    #print("Diff is " + str((dy, dx)))

                    in1 = True

                    n = 1
                    while in1:
                        print(n)

                        an1y = loc[thatl][0] + n*dy
                        an1x = loc[thatl][1] + n*dx

                        #print([an1y, an1x])

                        if an1y < m and 0<= an1y:
                            #print("ok i y-led")
                            if an1x < m and 0<= an1x:
                                #print((an1y, an1x))
                                if (an1y, an1x) not in list(antinodes):
                                    print("Adding: " + str((an1y, an1x)))
                                    #print("inte redan med")
                                    antinodes.add((an1y, an1x))
                                #else:
                                    #print("redan med")
                            else:
                                #print("X1 too big!")
                                in1 = False
                        else:
                            print("Y1 too big!")
                            in1 = False

                        n += 1
                        #input("Pause...")
                        
                    in2 = True
                    n = 1
                    while in2:
                        an2y = loc[thisl][0] - n*dy
                        an2x = loc[thisl][1] - n*dx

                        #print([an2y, an2x])

                        if an2y < m and 0<= an2y:
                            #print("ok i y-led")
                            if an2x < m and 0<= an2x:
                                #print((an2y, an2x))
                                if (an2y, an2x) not in list(antinodes):
                                    #print("Adding: " + str((an2y, an2x)))
                                    #print("inte redan med")
                                    antinodes.add((an2y, an2x))
                                #else:
                                    #print("redan med")
                            else:
                                #print("X1 too big!")
                                in2 = False
                        else:
                            #print("Y1 too big!")
                            in2 = False

                        n += 1
                        #input("Pause...")

                        #if (0 <= an2y and an2y <= m and
                        #0 <= an2x and an2x <= m and
                        #[an2y, an2x] not in antinodes):
                        #antinodes.append([an2y, an2x])

                    #input("Pause...")
print(list(antinodes))
print(len(antinodes))

input("Pause...")

for l in range(m):
    for c in range(m):
        if (l, c) in antinodes:
            print("#", end = "")
        else:
            print(inp[l][c], end = "")
    print("")
    





exit()
    
correct = 0
operators = ["add", "multiply", "cat"]

for l in range(len(inp)):
    line = inp[l]
    
    p = line.split(": ")
    result = int(p[0])

    #print(result)
    reg = re.findall(" ", p[1])

    combos = foo(operators, len(reg))
    #print(list(combos))

    for c in (combos):
        thisline = p[1]
        #print(thisline)


        #print(c)
                
        for op in range(len(c)):
            if c[op] == "add":
                #print("Found add")
                thisline = thisline.replace(" ", "a", 1)
            elif c[op] == "multiply":
                #print("Found mul")
                thisline = thisline.replace(" ", "x", 1)
            else:
                #print("Found nuffin.")
                thisline = thisline.replace(" ", "c", 1)
                
        ops = re.findall(r"[axc]", thisline)
        factors = re.findall(r"\d+", thisline)

        #print(factors)
        #print(ops)
        #input(thisline)

        tr = int(factors[0])
        
        for opno in range(len(ops)):
            if ops[opno] in "a":
                #print(str(tr) + " + " + str(factors[opno+1]) + " = ", end="")
                tr += int(factors[opno+1])
                #print(tr)
            elif ops[opno] in "x":
                #print(str(tr) + " * " + str(factors[opno+1]) + " = ", end="")
                tr *= int(factors[opno+1])
                #print(tr)
            else: # cat!
                #print(str(tr) + str(factors[opno+1]) + " = ", end="")
                tr = int(str(tr) + str(factors[opno+1]))
                #print(tr)
                
        #print(inp[l])
        #print(factors)
        #input(str(result) + " is it " + str(tr))
        if tr == result:
            correct += result
            #print("Got one:" + str(result))
            break

print(correct)
exit()

for fff in 1:
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
