#Aim of program: add up the squares of the numbers from -100 to 101
# First attempt:
#First we build the list
listOfNums = []
i = -100
while i < 101:
    listOfNums.append(i)
    i+=1

#Now we add up the numbers
sumOfSquares = 0
for i in range(len(listOfNums)):
    sumOfSquares += listOfNums[i] ** 2

print sumOfSquares


#Better second attempt:
def sumSquares(inputList):
    answer = 0
    for i in range(len(inputList)):
        answer += inputList[i] ** 2
    return answer

print sumSquares(range(-100,101))


#Even better third attempt:
def sumSquares2(inputList):
    answer = 0
    for i in inputList:
        answer += i ** 2
    return answer


print sumSquares2(range(-100,101))



# Magician attempt wait until Session 5 to understand this
print reduce(lambda x,y: x + (y ** 2), xrange(-100,101), 0)
