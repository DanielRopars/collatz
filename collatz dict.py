import math
coldict = {}
colpare = []
def twopower(n):
    return (n & (n-1) == 0) and n != 0


def collatz(n):
    for i in range(2, n):
        g = i
        a = []
        while not g == 1:
            if g < i < 1:
                a.append(coldict[g])
            if g % 2 == 0:
                g=g/2
            else: g = g*3+1
            a.append(g)
        coldict[i] = a

def colbig():
    for i in range (2, len(coldict)):
        colpare.append(len(coldict[i]))
    colpare.sort()
    print(colpare[-1])
    for key, value in coldict.items():
        if len(value) == colpare[-1]:
            print("The biggest chain is " + str(key) + ", with a length of " + str(colpare[-1]) + ".")
            print("Its chain is " + str(coldict[key]) + ".")
def collittle():
    colpare.sort()
    for key, value in coldict.items():
        if len(value) == colpare[key] and not twopower(key):
            print("The smallest chain is " + str(key))
            print("Its chain is " + str(coldict[key]))
            break
def colaverage():
    return sum(colpare)/len(colpare)
print(twopower(16))
collatz(10000)
colbig()
collittle()
print(colaverage())
