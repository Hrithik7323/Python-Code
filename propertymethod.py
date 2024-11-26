class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math


    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

hri = student(62, 61, 71)
print(hri.percentage)

hri.phy = 67
print(hri.percentage)        