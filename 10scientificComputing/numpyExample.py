import numpy as np
x = np.random.rand(3)
y = np.eye(3)
z = np.zeros((4,4,4))

x = np.arange(10)
y = np.arange(10) * 2

z = np.asarray([1,2])
z = z ** 2
print z
print z + 2

x = np.arange(4).reshape(2,2)
print x.T
print np.dot(x,z)
