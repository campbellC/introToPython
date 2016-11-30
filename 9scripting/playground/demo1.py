with open('demoFile.dat', 'r') as f:
    for line in f:
        if line[0] == '1':
            print line

#with open('demoFile.dat','w') as f: #OH DEAR...
