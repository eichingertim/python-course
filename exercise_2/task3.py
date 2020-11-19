x = ""

while (not x.isdigit()):
    x = input("enter a your solution for 'x^2 + 4x + 4 = 0': ")
    try:
        x = int(x)
        break
    except ValueError:
        print("This was not a number")

equation = x**2 + 4*x + 4
solution = 0

if (equation == solution):
    print("your input is a solution for 'x^2 + 4x + 4 = 0'")
else:
    print("your input is not a solution for 'x^2 + 4x + 4 = 0'")