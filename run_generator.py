import time, sys

def createRange(a,b,fcn):
    for i in range(a,b):
        yield fcn(i)

def transformList(A,fcn):
    for a in A:
        yield fcn(a)

def joinLists(A,B,fcn):
    for a in A:
        for b in B:
            yield fcn(a,b)

def runGenerator(x):
    if (x < 1): x = 1
    A = createRange(0, x, lambda a: a + 1)
    B = transformList(A, lambda a: a**2)
    C = list(joinLists(A, B, lambda a, b: b // a))

x = int(sys.argv[1])
step = 100
for xx in range(0 , x+step, step):
    runGenerator(xx)
    print (xx , ",", time.process_time())
