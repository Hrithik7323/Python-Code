# Q5 From a file containing numbers separation by comma, print the count of even numbers.


count = 0
with open("practice5.txt", "r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1

print(count)            
    