# 3.      Write a Python program that determines the largest of three numbers entered by the user.


number1=int(input("enter the number"))
number2=int(input("enter the number"))
number3=int(input("enter the number"))

greater=max(number1,max(number2,number3))
print(greater )