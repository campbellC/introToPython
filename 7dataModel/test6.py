def fun(aList):
    return aList.append(2)

x = [2]
y = x
fun(x)
print x,y
