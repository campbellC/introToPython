# make sure you realise the difference between this and test6
def fun(aList):
    return aList.append(2)

x = [2]
y = x
x= fun(x)
print x,y
