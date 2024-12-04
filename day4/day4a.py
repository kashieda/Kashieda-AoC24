import re

def rotate_CW(strmatrix):
    rotmatrix = []
    rows = list(zip(*reversed(strmatrix)))

    for row in list(rows):
        rotmatrix.append(''.join(row))
    
    return rotmatrix

def rotate45CW(inm):
    for l in inm:
        print(l)
    
    mout = []
    m = len(inm[0]) # Going to assume square matrix to start, at least
    print(str(m) + " lines")
    
    for d in range(2*m-1):

        n = m-abs(m-d-1)

        ri = max(0, m-d-1) # row index

        ci = min(m-1, 2*m-2-d) # column index

        line= []
        for iter in range(n):
            line += inm[ri+iter][ci-iter]
        #print(line)
        mout.append(''.join(line))

    return mout

def find_XMAS(m_in):

    XMAS = 0
    for l in range(len(m_in)):
        print(m_in[l])
        reg = re.findall(r"XMAS", m_in[l])

        if reg:
            print("!!XMAS")
        
        XMAS += len(reg)

        reg = re.findall(r"XMAS", m_in[l][::-1])

        if reg:
            print("!!SAMX")

        XMAS += len(reg)

        
    return XMAS
    
with open("day4.txt") as f:
    indata = [line.rstrip() for line in f]
    
total = 0

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
