
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
     
    @staticmethod 
    def her0_name():
          print("Krish", "robot")  

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)    

s1 = student("HRithik Kumar", [65,62,71])
s1.get_avg()
s1.her0_name()