def chainGenerator(*numbers, sep='-'):
    result = ''
    for i, num in enumerate(numbers):
        if (i == len(numbers) - 1):
            result += str(num)
        else:
            result += str(num) + sep
    return result

print( chainGenerator(1, 2, 3) )
print( chainGenerator(1, 2, 3, 4, sep="~~~") )
