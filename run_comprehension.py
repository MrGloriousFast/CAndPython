import time, sys

run_comprehension = lambda x: (b//a for a, b in ((d,d**2) for d in (c + 1 for c in range(0, x))))

#  x = int(sys.argv[1])
step = 100
x = 3000
for xx in range(0 , x+step, step):
    now = time.process_time()
    result = list(run_comprehension(xx))
    print (xx , ",", time.process_time() - now)

print (x , ",", time.process_time(), ", total", result[-1])
