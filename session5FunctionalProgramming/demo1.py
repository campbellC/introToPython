x = [1,2,3,4,5,6]

def transformList(func, xs):
    for index,i in enumerate(xs):
        xs[index] = func(i)

def square(i):
    return i*i
transformList(square, x)
print x

def plusOne(i):
    return i+1
transformList(plusOne,x)
print x
