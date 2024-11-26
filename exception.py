# Customize User Exception

#=================================== RAISE ====================================================== #


# class UnderAgeException(Exception):
#     pass

# class Hrithik:
#     age = 10

#     try:
#         if(age < 18):
#             raise UnderAgeException("you are Under Age")
#         else:
#             print("You are Eligible")
#     except UnderAgeException as uae:
#         print(uae)    


#=================================== 7 DIVISION ERROR ============================================== #

class SevenDivisionErrror(Exception):
    def __init__(self):
        print("You Can not Division by Seven")
    pass

class Main:
    num1 = int(input("Enter the First Number "))
    num2 = int(input("Enter the Second Number "))

    try:
        if(num2 == 7):
            raise SevenDivisionErrror
        else:
            result = num1 // num2
            print(result)
    except  SevenDivisionErrror as hrithik:
        print(hrithik)

      



        