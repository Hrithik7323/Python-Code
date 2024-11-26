#WAP  to enter marks of 3 subjects from the user store them in a dictionary. Start with an
# empty dictionary & add one by one. Use subject name as key & marks as value.


marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)

