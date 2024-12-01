import re
from collections import Counter

with open("day1.txt") as f:
    indata = [line.rstrip() for line in f]

for l in range(len(indata)):
    print(indata[l])

list1 = []
list2 = []

for n in range(len(indata)):
    r = re.findall(r"\d+", indata[n])
    list1.append(int(r[0]))
    list2.append(int(r[1]))

count = Counter()

for n in list2:
    count[n] += 1

sim = 0
    
for n in list1:
    print("Nummer: " + str(n) + " finns " + str(count[n]) + " gånger")

    sim += n*count[n]
    
    #print("List1: " + str(list1[n]) + " List2: " +
          #str(list2[n]) + " Diff: " + str(d[n]))

print("Summa likhet: " + str(sim))
