# Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b
    
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

result = div(num1, num2)
print("Division:", result)



# def div(a, b):

#     try:
#         result = a / b
#         print("The result division: ")

#     except:
#         print("Error: Division by not Zero: ")  

# div(10, 2)
# div(10, 0)          