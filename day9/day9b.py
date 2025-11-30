import re, itertools, copy

class Files:
    def __init__(self, position, length):
        self.position = position
        self.length = length

with open("day9.txt") as f:
    inp = [line.rstrip() for line in f]

inp = inp[0]

#print(len(inp))

filesystem = []

files = []

fn = 0
f = True

for s in range(0,len(inp)):
    #print(s)
    #print(inp[s:s+2])

    if f:
        files.append(Files(len(filesystem), int(inp[s])))
        tw = [fn]
        fn += 1
        

    else:
        tw = []

    f = not f
        
    for l in range(int(inp[s])):
        filesystem.append(tw)

print(filesystem)
#print(files)

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

for file_bw in range(len(files)-1, -1, -1):
    print(f"Fil {file_bw} startar på {files[file_bw].position}",
          f"och är {files[file_bw].length} block lång.")

    for position in range(files[file_bw].position):
        blank = False
        
        if not filesystem[position]:
            blank = True

            fits = True

            for i in range(1,files[file_bw].length):
                #print(i)
                #print(filesystem[position+i])
                if filesystem[position+i]:
                    fits = False
                    #print("Filen får inte plats.")

            if fits:
                #print(filesystem)

                for i in range(files[file_bw].length):
                    filesystem[position+i] = \
                        filesystem[files[file_bw].position+i]
                    filesystem[files[file_bw].position+i] = []

                #print(filesystem)

print(filesystem)
    
cs = 0
for i in range(len(filesystem)):
    if filesystem[i]:
        print(filesystem[i][0])
        cs += i*filesystem[i][0]

print("Checksum: " + str(cs))
