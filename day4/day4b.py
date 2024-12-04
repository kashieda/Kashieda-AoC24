with open("day4.txt") as f:
    indata = [line.rstrip() for line in f]
total = 0
for l in range(1,len(indata)-1):
    for c in range(1, len(indata[0])-1):
        if indata[l][c] == 'A':
            if ((indata[l-1][c-1] == "M" and
                 indata[l+1][c+1] == "S") or
                (indata[l-1][c-1] == "S" and
                 indata[l+1][c+1] == "M")):
                if ((indata[l+1][c-1] == "M" and
                     indata[l-1][c+1] == "S") or
                    (indata[l+1][c-1] == "S" and
                     indata[l-1][c+1] == "M")):
                    total += 1
print(total)
