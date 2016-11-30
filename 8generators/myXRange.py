def myXRange(n):
    i = 0
    while( i < n ):
        yield i
        i += 1

for i in myXRange(10):
    print i


