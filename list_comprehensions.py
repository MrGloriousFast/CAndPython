import time, sys

run_comprehension = lambda x: (a//b for a, b in ((c,d**2) for d in (c + 1 for c in range(0, x))))

x = int(sys.argv[1])
step = 100
for xx in range(0 , x+step, step):
    run_comprehension(xx)
    print (xx , ",", time.process_time())
