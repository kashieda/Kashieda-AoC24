import re, itertools, copy


with open("day9.txt") as f:
    inp = [line.rstrip() for line in f]

inp = inp[0]

#print(len(inp))

filesystem = []

fn = 0
f = True

for s in range(0,len(inp)):
    #print(s)
    #print(inp[s:s+2])

    if f:
        tw = [fn]
        fn += 1
    else:
        tw = []

    f = not f
        
    for l in range(int(inp[s])):
        filesystem.append(tw)

#print(filesystem)

l = len(filesystem)

no = 0

for pos in range(l):
    if filesystem[pos]:
        no += 1

#print(no)

print("There are " + str(l) + " blocks in the filesystem.")
print(str(no) + " of those are full.")
print("There are " + str(l-no) + " empty blocks.")

nf = 0

#for ff in filesystem:
#    print(ff, end="")
#print("")
    

for bw in range(l-no):
    if filesystem[l-bw-1]:
        while filesystem[nf]:
            nf += 1

        filesystem[nf] = filesystem[l-bw-1]
        filesystem[l-bw-1] = []

    #for ff in filesystem:
    #    print(ff, end="")
    #print("")
    #input("Pause...")

cs = 0
for i in range(no):
    #print(filesystem[i][0])
    cs += i*filesystem[i][0]

print("Checksum: " + str(cs))
