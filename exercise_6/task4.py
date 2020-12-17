def recursive_search(searchTerm, data):
    if (len(data) == 1):
        if (data[0] == searchTerm):
            return True
        else:
             return False
    else:
        middleIndex = int(len(data) / 2)
        middle = data[middleIndex]
        if (middle == searchTerm):
            return True
        elif (searchTerm > middle):
            return recursive_search(searchTerm, data[:middleIndex])
        else:
            return recursive_search(searchTerm, data[middleIndex:])

data = [1, 5, 6, 7, 8, 50, 96, 666, 1337, 2112]
searchTerm = 42

print(recursive_search(42, data))
