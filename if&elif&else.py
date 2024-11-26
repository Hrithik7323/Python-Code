marks = int(input("enter your marks : "))

#space nhi dena hai niche coding me ....... nhi to nhi hoga

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of student ->", grade)