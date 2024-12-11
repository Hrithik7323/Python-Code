# Write a Python program that prompts the user to input an integer and raises a 
# ValueError exception if the input is not a valid integer.


def integer_input():
    user_input = input("Please enter an integer: ")
    
    try:
        number = int(user_input)
        return number
    except ValueError:
        raise ValueError("The input is not a valid integer. Please enter a valid integer.")

try:
    user_integer = integer_input()
    print("You entered the integer: user_integer")
except ValueError as e:
    print(e)
