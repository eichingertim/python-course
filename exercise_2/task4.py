year = ""

while (not year.isdigit()):
    year = input("enter a year: ")
    try:
        year = int(year)
        break
    except ValueError:
        print("This was not a number")

if ((year % 4 == 0 and not year % 100 == 0) or year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")