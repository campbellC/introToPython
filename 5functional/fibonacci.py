memo = {1:1, 0:1}

def fib(n):
    if n is memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

def memoise(func):
    memo = {}

    def newFunc(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = func(n)
            return memo[n]
    return newFunc
def newFib(n):
    if n ==0 or n==1:
        return 1
    else:
        return newFib(n-1) + newFib(n-2)

betterFib = memoise(newFib)
