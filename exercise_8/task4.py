with open('gameScores.txt', 'r') as gs:
    header = gs.readline().replace('\"', '').replace('\n', '').split(',')

    counterDict = dict()

    for name in header:
        counterDict[name] = 0

    for line in gs:
        ar = line.replace('\n', '').split(',')
        for i, v in enumerate(counterDict):
            counterDict[v] += int(ar[i])

    print(counterDict)