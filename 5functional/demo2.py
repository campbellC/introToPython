
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        answer =  fib(n-1) + fib(n-2)
        return answer

def memoise(f):
    memo = {}
    def g(n):
        if n in memo:
            return memo[n]
        else:
            answer = f(n)
            memo[n] = answer
            return answer
    return g
fib = memoise(fib)

