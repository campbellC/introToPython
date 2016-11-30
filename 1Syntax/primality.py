import math
def isPrime(num): # num is an int > 1
    isPrimeFlag = True
    upperBound = int(math.ceil(math.sqrt(num))) + 1
    for i in range(2,upperBound):
        if num % i == 0:
            isPrimeFlag = False
            break

    return isPrimeFlag

x = 10

