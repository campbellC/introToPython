x = 10
def fun1():
    def fun2():
        x = 10
        y = fun3() + x
        return y
    x = 20
    y = fun2() + x
    return y


def fun3():
    z = 10
    return z


import pdb; pdb.set_trace()
print fun1()
