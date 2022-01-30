# https: // wiki.python.org.br / EstruturaSequencial
# These are command to receive a number or string, shows the type and convert if necessary and print
x = input("Write something: ")

try:
    y = float(x)
    print(y)
    y_type = str(type(y))
    print("You choose a number: " + y_type)
except:
    print(x)
    x_type = str(type(x))
    print("You choose a string: " + x_type)

