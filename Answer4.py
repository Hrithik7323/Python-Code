# 4. Write a Python program that takes an integer input from the user and calculates its factorial using a while loop. Display the result as the factorial of the entered number.

num = int(input("Enter a  integer:"))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(factorial)    
