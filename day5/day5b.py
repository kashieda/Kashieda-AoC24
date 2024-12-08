import re

with open("day5.txt") as f:
    indata = [line.rstrip() for line in f]
    
total = 0

ordering = []
po = []
for l in indata:
    if "|" in l:
        reg = re.findall(r"\d+", l)
        #print(reg)
        line = [int(reg[0]), int(reg[1])]
        ordering.append(line)
            
        
    if "," in l:
        reg = re.findall(r"\d+", l)
        #print(reg)

        line = []
        for n in reg:
            line.append(int(n))
        po.append(line)
            
not_ok = []

for p in range(len(po)):
    ok = True
    
    for n in range(1, len(po[p])):
        for m in range(n):
            for o in range(len(ordering)):
                if po[p][n] == ordering[o][0] and po[p][m] == ordering[o][1]:
                    ok = False
                    if not p in not_ok:
                        not_ok.append(p)
                    
for p in not_ok:
    print(po[p])
    ok = False

    while not ok:
        ok = True
        for n in range(1, len(po[p])):
            for m in range(n):
                for o in range(len(ordering)):
                    if po[p][n] == ordering[o][0] and po[p][m] == ordering[o][1]:
                        ok = False
                        print("Ordering: " + str(ordering[o][1]) + " before " +
                              str(ordering[o][0]) + " violated. Reordering.")
                        po[p][m], po[p][n] = po[p][n], po[p][m]
                        

    print("New order!")
    print(po[p])

    total += po[p][int((len(po[p])-1)/2)]

print(total)

exit()        
