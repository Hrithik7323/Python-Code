class student:
    collage_name = "ABC infocollage"  # Attributes

    def __init__(self, name, marks):
        self.name = name              # Object > attributes
        self.marks = marks            # object
        print("Adding new information in Database...")

s1 = student("Hrithik Kumar", 72)
print(s1.name, s1.marks)        
        