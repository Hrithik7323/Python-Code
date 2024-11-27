# A toy vendor supplies three of toys:



product_code = int(input("Enter the product code (1 for battery-based, 2 for key-based, 3 for electrical charging):"))
order_amount = float(input("Enter the order amount:"))

discount = 0

if product_code == 1 and order_amount > 1000:
    discount = 0.10
elif product_code == 2 and order_amount > 100:
    discount = 0.05
elif product_code == 3 and order_amount > 500:
    discount = 0.10

net_amount = order_amount - (order_amount * discount)

print("Net amount to be paid", net_amount)