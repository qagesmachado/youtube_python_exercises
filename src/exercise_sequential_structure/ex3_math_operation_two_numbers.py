# https: // wiki.python.org.br / EstruturaSequencial
# This code will execute some math operation between two numbers

# Input validations
while True:
    number_1 = input("Write number 1: ")
    try:
        number_1 = float(number_1)
        break
    except:
        print("Invalid input")
while True:
    number_2 = input("Write number 2: ")
    try:
        number_2 = float(number_2)
        break
    except:
        print("Invalid input")
while True:
    operation = input("Choose operation (+,-,/,*) or '-1' to quit: ")

    if (operation == "+") or (operation == "-") or (operation == "/") or (operation == "*"):
        break
    if operation == "-1":
        quit()

# Operations
if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "/":
    try:
        result = number_1 / number_2
    except ZeroDivisionError:
        print("!! Error !! Cannot divide by zero !! Error !! ")
        quit()
elif operation == "*":
    result = number_1 * number_2


print(f'The result of {number_1} {operation} {number_2} = {result}')

