#   __init__

# we called as CONSTRUCTOR....

class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new name and marks in Database.....")

s1 = student("Hrithik", 71)
print(s1.name, s1.marks)

s2 = student("Ankit", 85)
print(s2.name, s2.marks)
