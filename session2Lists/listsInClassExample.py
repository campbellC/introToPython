# Add up the squares of the numbers from -100 to 100

# Attempt 1:
# build the list

listOfNums = []
i = -100
while i < 101:
    listOfNums.append(i)
    i += 1

#add up the squares
sumOfSquares = 0

for num in listOfNums:
    sumOfSquares += num ** 2


#attempt 2:
def sumSquares(inputList):
    sumOfSquares = 0
    for num in inputList:
        sumOfSquares += num ** 2
    return sumOfSquares

print sumSquares(range(-100, 101))

print reduce(lambda x,y: x + (y ** 2), xrange(-100,101), 0)
