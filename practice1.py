# Create student  class that takes name $ marks of 3 suject as arguments in constructor. 
# Than creats a methods to print the average. 

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)    

s1 = student("HRithik Kumar", [65,62,71])
s1.get_avg()
         