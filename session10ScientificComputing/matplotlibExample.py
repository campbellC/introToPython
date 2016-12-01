import numpy as np
import matplotlib.pyplot as plt

gradient =4
intercept = 3
N = 100
xx = np.arange(N)
yy = xx * gradient + intercept
yy = yy + np.random.normal(scale=10,size=N)


#plt.scatter(xx,yy)

X = np.vstack([xx, np.ones(len(xx))]).T

lstSq = np.linalg.lstsq(X,yy)
m,c = lstSq[0]
mse=lstSq[1]

#plt.plot(xx, m * xx + c, color='r')
#plt.show()
print m,c
print mse
