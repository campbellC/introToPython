def powerFactory(n):
    def g(x):
        return x ** n
    return g

square = powerFactory(2)
cube = powerFactory(3)
print square(20)
print cube(20)

def multiply(f,g):
    def fg(x):
        return f(x) * g(x)
    return fg

