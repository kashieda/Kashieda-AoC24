import re

with open("day3.txt") as f:
    indata = [line.rstrip() for line in f]

total = 0
enabled = True

for l in range(len(indata)):
    print(indata[l])
    reg = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", indata[l])

    for s in reg:
        print(s)
        if s == "do()":
            print("It's a do!")
            enabled = True
        elif s == "don't()":
            print("It's a don't!")
            enabled = False
        else:
            if enabled:
                r = re.findall(r"\d+",s)
                print(str(r) + " multiplying: " + r[0] + " and " + r[1])
                total += int(r[0])*int(r[1])
            else:
                print("Ignoring a mul!")

print(total)
exit()

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
                                    
