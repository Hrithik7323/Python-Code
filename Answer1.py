# 1.Write a Python program that determines if a given year is a leap year or not.


year=int(input("enter the year"))
if(year % 4==0 and year % 100!= 0)or (year % 400 == 0):
    print("leap year")
else:
    print("not leap year")