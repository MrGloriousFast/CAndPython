import time, sys

#the test function
#you can copy this file and implement another way to get the same result
def run(x):
    if (x < 1): x =1
    groupC = []

    for a in range(0,x):
        groupC.append(a+1)
    return groupC[-1]


#dont touch this
#measure code and output that we need to compare implementations
x = 3000 #int(sys.argv[1])
step = 100
for xx in range(0 , x+step, step):
    now = time.process_time()
    result = run(xx)
    print (xx , ",", time.process_time() - now)
    
#compare the result to other implementations to knwo your code runs correct
print (x , ",", time.process_time(), ", total", result)
