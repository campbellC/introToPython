#Remove the 60th element from a list
#Attempt One

testList = range(1,100)
outputList1 = []
for i in range(len(testList)):
    if i != 59:
        outputList1.append(testList[i])

# Second attempt
outputList2 = testList[:59] + testList[60:]

print outputList1 == outputList2


#Remove the penultimate item from a list
def penultimateRemover(inputList):
    return inputList[:-2] + inputList[-1:]

#print penultimateRemover(range(10))

#print penultimateRemover([])
#print penultimateRemover(range(1))
