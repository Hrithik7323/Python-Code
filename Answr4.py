# Write a Python program that prompts the user to input two numbers and raises a
# TypeError exception if the inputs are not numerical.


def numerical_input():
    try:
        
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        return num1, num2
    except ValueError:
        raise TypeError("Both inputs must be numerical values.")

try:
    number1, number2 = numerical_input()
    print("You entered the numbers: {number1} and {number2}")
except TypeError as e:
    print(e)
