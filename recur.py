#5,4,3,2,1 print in reursive function

def show(n):
    if(n == 0):   # Base case
        return
    print(n)
    show(n-1)

show(5)