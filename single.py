class car:
    @staticmethod
    def start():
        print("car started..")

    def stop():
        print("car stopte..")

class toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = toyotacar("forturer")
car1 = toyotacar("prius")

print(car1.start())              

