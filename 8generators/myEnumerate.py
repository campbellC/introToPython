def myEnumerate(iterable):
    index = 0
    for i in iterable:
        yield (index,i)
        index += 1

for i in myEnumerate("hello"):
    print i
