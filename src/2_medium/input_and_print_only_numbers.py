# Inspiration was this exercise -> src\wiki_python_exercises\exercise_sequential_structure\ex2_input_and_print.py

# Ask for a number and validate if was printed
# Validation of number x string x special character 

x = input("Write any number ")

try:
    y = float(x)
    print(y)
except:
    print("it is not a number")