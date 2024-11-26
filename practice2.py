# Define a Employee class with attributes role, department & salary. This class also a
# showDetails() method.

# Creat an Engineer class that inherits properties from Employee & has additional
# attribute : name & age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDeatail(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name =name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

eng1 = Engineer("Hrithik Kumar", 24)
eng1.showDeatail()         