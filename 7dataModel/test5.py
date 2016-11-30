def fun(aList):
    aList.append(2)
    return

x = [2]
y = x
fun(x)
print x,y
