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
            
po_sum = 0

for p in range(len(po)):
    print(po[p])
    ok = True
    for n in range(1, len(po[p])):
        for m in range(n):
            for o in range(len(ordering)):
                if po[p][n] == ordering[o][0] and po[p][m] == ordering[o][1]:
                    ok = False
                    print("Ordering: " + str(ordering[o][1]) + " before " +
                          str(ordering[o][0]) + " violated.")

    if ok:
        print(po[p][int((len(po[p])-1)/2)])
        po_sum += po[p][int((len(po[p])-1)/2)]

print(po_sum)
                    













exit()        

this = find_XMAS(indata)
input(this)
total += this
data = rotate45CW(indata)

this = find_XMAS(data)
input(this)
total += this

data = rotate_CW(indata)

this = find_XMAS(data)
input(this)
total += this

data = rotate45CW(data)
this = find_XMAS(data)

input(this)

total += this

print(total)
    
exit()
