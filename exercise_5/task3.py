import random

def selectionSort(unsortierteListe):

    for i in range(len(unsortierteListe)):
        minIndex = i

        for j in range(i + 1, len(unsortierteListe)):
            if (unsortierteListe[j] < unsortierteListe[minIndex]):
                minIndex = j
        
        unsortierteListe[minIndex], unsortierteListe[i] = unsortierteListe[i], unsortierteListe[minIndex]

testList = random.sample(range(50), 6)

print(testList)
selectionSort(testList)
print(testList)
