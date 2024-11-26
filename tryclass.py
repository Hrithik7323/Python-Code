#__class

# try:
#     a = 20
#     b = 0
#     div = a / b
#     print(div)

# except Exception as e:
#     print(e.__class__)   


import sys

num1 = input("enter the first number")
num2 = input("enter the second number")

try:
    res = num1 / num2
    print(res)

except Exception as e:
    print(sys.exc_info())    
