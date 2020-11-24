import math

myList = ["Dusky", "Joe", "Hartington"]

print("### ELEMENTE IN MODUL MATH:")
# print(dir(math))

# print(help(math.factorial))
print("Should print '6': " + str(math.factorial(3)))
# print(help(math.radians))
print("Should print '3,14...': " + str(math.radians(180)))

print()

print("### ELEMENTE IN KLASSE LIST:")
# print(dir(myList))

# print(help(myList.index))
print("Should print '1': " + str(myList.index("Joe")))

# print(help(myList.clear))
myList.clear()
print("Should print empty list: " + str(myList))
