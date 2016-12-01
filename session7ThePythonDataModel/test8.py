# make sure you realise the difference between this and test6, test7
def fun(aList):
    aList.append(2)

x = [2]
y = x
x = fun(x)
print x,y
