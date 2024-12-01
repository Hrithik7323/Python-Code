# 5. A transport company charges the fare according to the following table:
# Distance	Charges
# 1-50	8 Rs./Km
# 51-100	10 Rs./Km
# >100	12 Rs./Km


distance=int(input("enter the distance"))
if(distance>=1 and distance<=50):
    print("the total charges are ",10*distance)
elif(distance>=51 and distance<=100):
    print("the total charges are",10*distance)
else:
    print("the total charges are",12*distance)