def myXrange(bottom, top=None, stepsize=1):
    if top is None:
        top = bottom
        bottom = 0
    i =bottom
    while(i<top):
        yield i
        i+=stepsize

def foo():
    return ""

print myXrange(10)
print foo
# for i in myXrange(10):
    # print i

# for i in myXrange(1, 100, 2):
    # print i
