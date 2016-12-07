import numpy as np

N = 10 ** 6
x = np.random.normal(size=N)
# print np.mean(x)
# print np.std(x)

gradient =4
intercept = 3
xx = np.arange(10)
yy = xx * gradient + intercept
yy = yy + np.random.normal(scale=.1,size=10)
print xx,yy
X = np.vstack([xx, np.ones(len(xx))]).T

lstSq = np.linalg.lstsq(X,yy)
m,c = lstSq[0]
mse=lstSq[1]
print m,c
print mse
