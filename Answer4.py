# 4 A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
# Here we have the three Category for the Toys.
# 1. Battery Based
# 2. Key Based
# 3. Electrical Based

amount = 10000
code = int(input("Enter the code from 1 to 3"))

if(code == 1):
    if(amount <= 1000):
        print("The total Amount are:- ",amount)
    else:
         discount = amount * 10  / 100
         print("The Discounted Amount are:- ", int(discount))   
         print("The Amount after Discounted:- ", int(amount - discount))  
elif(code == 2):
    if(amount <= 100):
        print("The total Amount are:- ",amount)
    else:
         discount = amount * 5  / 100
         print("The Discounted Amount are:- ", int(discount))   
         print("The Amount after Discounted:- ", int(amount - discount))          
elif(code == 3):
    if(amount <= 500):
        print("The total Amount are:- ",amount)
    else:
         discount = amount * 10  / 100
         print("The Discounted Amount are:- ", int(discount))   
         print("The Amount after Discounted:- ", int(amount - discount))
    