# Write a python program to handle a ZeroDevisionError exception when dividing a number by Zero.

def divide_num(a, b):
    
    try:
        a = 10
        b = 0
        result = a / b
        print("result")

    except ZeroDivisionError:
        print("Not divide by Zero.")