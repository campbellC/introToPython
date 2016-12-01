def printRange(x): # x should be int
    for i in xrange(x):
        print i

printRange(10)
printRange(1000)


#quick aside: range(n) is inefficient as it actually stores all of the numbers!
#use xrange instead!
