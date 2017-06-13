import time, sys

def createRange(a,b,fcn):
    for i in range(a,b):
        yield fcn(i)

def transformList(A,fcn):
    for a in A:
        yield fcn(a)

def joinLists(A,B,fcn):
    for a, b in zip(A,B):
        yield fcn(a,b)

def runGenerator(x):
    if (x < 1): x = 1
    A = createRange(0, x, lambda a: a + 1)
    B = lambda it: transformList(it, lambda a: a**2)
    return list(joinLists(A, B(A), lambda a, b: b // a))

#  x = int(sys.argv[1])
x = 3000
step = 100
for xx in range(0 , x+step, step):
    now = time.process_time()
    result = runGenerator(xx)
    print (xx , ",", time.process_time() - now)
print (x , ",", time.process_time(), ", total", result[-1])
