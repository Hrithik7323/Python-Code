class bar:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class toyotacar(bar):
    def __init__(self, name):
        self.name = name

car1 = toyotacar("forturer")
car1 = toyotacar("prius")

print(car1.start())