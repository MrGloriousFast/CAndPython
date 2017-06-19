from fib_lib import ffi, lib

def fib_python(a):
    if (a<=0):
        return 0
    elif (a==1):
        return 1
    else:
        return fib_python(a-2)+fib_python(a-1)

number = 35

for i in range(0,number):
    print(i,lib.fib(i))
    
for i in range(0,number):
    print(i,fib_python(i))



