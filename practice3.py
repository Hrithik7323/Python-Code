# Create a class called order which store item & its price.
# use Dunder function __gt__() to convey that:

#    order1 > order2  if price of order1 > price of order2


class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = order("samosa", 12)
odr2 = order("tea", 10)

print(odr1 > odr2)