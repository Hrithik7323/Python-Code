class person:
    name = "anonymous"

    #def changename(self, name):
    #    self.__class__.name = "HRITHIK"
        #person.name = name

    @classmethod
    def changename(cls, name):
        cls.name = name    

p1 = person()
p1.changename("Hrithik kumar")
print(p1.name)
print(person.name)      