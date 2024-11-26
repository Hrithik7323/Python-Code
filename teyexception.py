# try:
#     a = 2
#     b = 0
#     result = a / b
#     print(result)


# except Exception as e:
#     print(e) 

# except ZeroDivisionError as e:
#     print(e)

# except ValueError as e:
#     print(e)

try:
     a = 10
     b = 0
     result = a / b
     print(result)

except (ZeroDivisionError, ValueError, NameError) as e:
     print(e)     

