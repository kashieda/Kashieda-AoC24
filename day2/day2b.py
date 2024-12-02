import re

with open("day2.txt") as f:
    indata = [line.rstrip() for line in f]

unsafe = []
safe = 0

for l in range(len(indata)):
    unsafe.append(l)
    #print(indata[l])
    reg = re.findall(r"\d+", indata[l])

    line = []
    for i in reg:
        line.append(int(i))

    #print(line)
    faults = 0
    
    diff = []
    
    for n in range(1,len(line)):
        diff.append(line[n-1]-line[n])

    #print(diff)

    if 0 in diff:
        print("There is a 0 in here!")
        faults = 1
        continue
        
    samesign = True
    
    if diff[0] < 0:
        for n in range(1, len(diff)):
            if diff[n]>0:
                samesign = False
    else:
        for n in range(1, len(diff)):
            if diff[n]<0:
                samesign = False

    if not samesign:
        print("Mixes signs. Bad!")
        continue

    ok = True
    for n in range(len(diff)):
        if abs(diff[n])>3:
            ok = False

    if ok:
        print("This one is ok!")
        safe += 1
        unsafe.pop()
    else:
        print("Nope, too big a difference.")
        
print("There are " + str(safe) + " safe reports.")
print("There are " + str(len(unsafe)) + " unsafe reports in the first run.")

print(unsafe)

for l in unsafe:
    reg = re.findall(r"\d+", indata[l])

    thisone = False
    for r in range(len(reg)):
        if thisone:
            continue
        
        line = []
        for i in reg:
            line.append(int(i))

        line.pop(r)

        #print(line)
    
        diff = []
    
        for n in range(1,len(line)):
            diff.append(line[n-1]-line[n])

        #print(diff)

        if 0 in diff:
            print("There is a 0 in here!")
            faults = 1
            continue
        
        samesign = True
    
        if diff[0] < 0:
            for n in range(1, len(diff)):
                if diff[n]>0:
                    samesign = False
        else:
            for n in range(1, len(diff)):
                if diff[n]<0:
                    samesign = False

        if not samesign:
            print("Mixes signs. Bad!")
            continue

        ok = True
        for n in range(len(diff)):
            if abs(diff[n])>3:
                ok = False

        if ok:
            print("This one is ok!")
            safe += 1
            thisone = True
            continue
        else:
            print("Nope, too big a difference.")

print("There are " + str(safe) + " safe reports.")
