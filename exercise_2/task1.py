input_num = ""

while (not input_num.isdigit()):
    input_num = input("enter a number: ")
    try:
        input_num = int(input_num)
        break
    except ValueError:
        print("This was not a number")


print(2 * input_num)