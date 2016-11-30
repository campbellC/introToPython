x = range(10000)
for i in (j for j in x if j % 2 == 0):
    print i

def product(iterable1, iterable2):
    for x in iterable1:
        for y in iterable2:
            yield (x,y)

list1 = [1,2,3]
for index, i in enumerate(list1):
    newList = list1[:index] + list1[index+1:]
X = "ABCDEFG"
# Y = "zyxwvut"
# for i in product(X,Y):
    # print i

# from itertools import product

# for i in product(X,Y):
    # print i
