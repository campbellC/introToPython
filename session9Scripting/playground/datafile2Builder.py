import random
random.seed()
with open('datafile2.dat','w') as f:
    for i in range(10000):
        for j in range(50):
            f.write(str(random.randint(0,1000)) + ' ')
        f.write('\n')


