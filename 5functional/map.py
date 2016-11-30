print map(lambda z : z ** 2, [1,2,3])

def myMap(func, inputList):
    x= []
    for element in inputList:
        x.append(func(element))
    return x
print myMap(lambda z : z ** 2, [])

x= [1,2,3]

y= filter(lambda z: z % 2 == 1,x)
y.append(3)
print y
print x
