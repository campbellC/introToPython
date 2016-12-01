import time

def fib(n): #n >=0
    if (n==0) or (n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

starttime = time.time()
fib(25)
print time.time() - starttime

fibonacciNumers = {0: 1, 1:1}
def memoisedFib(n):
    if n in fibonacciNumers:
        return fibonacciNumers[n]
    else:
        result = memoisedFib(n-1) + memoisedFib(n-2)
        fibonacciNumers[n] = result
        return result

starttime = time.time()
memoisedFib(25)
print time.time() - starttime
