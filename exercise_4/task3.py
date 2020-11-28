height = ""

while (not height.isdigit()):
    height = input("enter tree height: ")
    try:
        height = int(height)
        break
    except ValueError:
        print("This was not a number")

startStars = 1
startSpaces = height - 1

for i in range(height):
    print(" " * startSpaces + "*" * startStars)
    startStars += 2
    startSpaces -= 1