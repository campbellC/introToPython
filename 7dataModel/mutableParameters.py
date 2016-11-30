#This file has horrible behaviour.
def add(x,y=0):
    return x + y

# print add(1,1)
# print add(1)
def append(x,y=[]):
    y.append(1)
    return x + y
def betterAppend(x,y=None):
    if y is None:
        y = []
    y.append(1)
    return x + y

print append([])
print append([])

#Make a grid
x = [[0] * 8] * 8
for i in x:
    print i

x[0][0] = 1
for i in x:
    print i

# make a grid properly
x = [[0] * 8 for _ in range(8)]
for i in x:
    print i

x[0][0] = 1
for i in x:
    print i
