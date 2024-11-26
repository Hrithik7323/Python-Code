#Q1. define a cirle class to create with radius r using the constuctor.
# Define an Aera() method of the class which calculates the area of the circle.
# Define a perameter() method of class which allows you to claculate the paremeter of the circle.

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def parameter(self):
        return 2 * (22/7) * self.radius

c1 = circle(21)
print(c1.area())
print(c1.parameter())
