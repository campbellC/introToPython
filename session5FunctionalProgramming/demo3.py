import operator
x = [1,2,3,4,5]
z = ["1","2"]

print map(lambda y: y*y, x)
print map(int,z)


print filter(lambda x: x % 2 == 0, x)

print reduce(lambda z,y: z * y,x,1)
print reduce(lambda z,y : z+y, x, 0)


def myReduce(f, lst, accumulator):
    if len(lst) ==0 :
        return accumulator
    else:
        newaccumulator = f(accumulator,lst[0])
        return myReduce(f,lst[1:],newaccumulator)
