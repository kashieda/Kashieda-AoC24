import re, itertools

def foo(l, n): ### Make all combinations of items in l of length n
     yield from itertools.product(*([l] * n))

def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

with open("day8_test.txt") as f:
    inp = [line.rstrip() for line in f]

ants = set()
antinodes = []
m = len(inp)


for l in range(m):
    reg = re.findall(r"[^.]", inp[l])
    if reg:
        for r in reg:
            ants.add(r)

print([4, 9] + [-1, 4])
            
for a in list(ants):
    print(a)

    loc = []
    
    for l in range(m):
        if a in inp[l]:
            x = [i for i, ltr in enumerate(inp[l]) if ltr in a]
            for thisx in x:
                loc.append([[l, thisx]])

            for thisl in range(len(loc)-1):
                for thatl in range(thisl, len(loc)):
                    blubb
                
                


                
    print(loc)  



















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
