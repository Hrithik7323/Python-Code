#WAP to find the gratest  of 3 numbers entered by the user.

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print("First number is greater", a)
elif(b >= c):
    print("second number is greater", b)
else:
    print("Third number is greater", c)
    