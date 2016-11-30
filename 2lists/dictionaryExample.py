from math import sqrt
import time

primality = {1:False}
def primeTest(n):
    if n in primality:
        return primality[n]
    else:
        answer = True
        for i in range(2,int( sqrt(n) ) ):

            if n % i == 0:
                answer = False
                break
        primality[n]= answer
        return answer


timeNow = time.time()
print primeTest(1010101019)
print time.time() - timeNow

timeNow = time.time()
primeTest(1010101019)
print time.time() - timeNow

