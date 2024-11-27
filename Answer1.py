# Python program to check leap year.

def checkleap(year):
    
    if((year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)):
        print("The year is a leap year")
    else:
        print("The year is not a leap year")

year = int(input("Enter the number : "))

checkleap(year)

