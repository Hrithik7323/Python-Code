# create Account class with 2 attributs- balance $ account no.UserWarning
# Ceate methods for debit, credit $ printing the balance.

class Account:

    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    def  debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance           

s1 = Account(10000, 1234567)
s1.debit(10000)
s1.credit(500)
s1.credit(50000)
s1.debit(1000)