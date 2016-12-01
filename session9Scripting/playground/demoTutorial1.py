def endsIn7(n):
    return n % 10 == 7
with open('demoFile.dat', 'r') as f:
    for line in f:
        listOfInts = line.split(' ')
        listOfInts = map(int, listOfInts)
        if endsIn7(listOfInts[1]):
            print listOfInts
