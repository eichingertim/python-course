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
            return recursive_search(searchTerm, data[middleIndex:])
        else:
            return recursive_search(searchTerm, data[:middleIndex])

data = [1, 5, 6, 7, 8, 42, 96, 666, 1337, 2112]

print(recursive_search(2112, data))
