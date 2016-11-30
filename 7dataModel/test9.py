class foo():
    def __init__(self, aList):
        self.aList = aList

    def appendTwo(self):
        self.aList.append(2)

    def __repr__(self):
        return self.aList.__repr__()

x = []
y = foo(x)
y.appendTwo()

print x, y
