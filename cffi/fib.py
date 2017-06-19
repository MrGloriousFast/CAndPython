from cffi import FFI

ffibuilder = FFI()

# For every function that you want to have a python binding,
# specify its declaration here
ffibuilder.cdef("""
    int fib(int a);
                """)

# Here go the sources, most likely only includes and additional functions if necessary
ffibuilder.set_source("fib_lib",
    """
    #include "fib.h"
    """, sources=["fib.c"])

if __name__ == "__main__":
    ffibuilder.compile()
