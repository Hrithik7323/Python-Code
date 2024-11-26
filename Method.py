class student:
    collage_name = "ABC infocollage"  # Attributes

    def __init__(self, name, marks):
        self.name = name              # Object > attributes
        self.marks = marks            # object

    def welcome(self):
        print("Welcome student", self.name)   

    def get_marks(self):
        return self.marks


s1 = student('Hrithik', '72')
s1.welcome()
print(s1.get_marks())


