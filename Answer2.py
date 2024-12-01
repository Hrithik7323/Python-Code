# 2.      Create a Python program that checks if a user-given number is positive, negative, or zero


number=int(input("enter the number"))
if(number>0):
    print("numer is positive")
else:
    if(number==0):
        print("number is zero")
    else:
        print("number is negative")
        