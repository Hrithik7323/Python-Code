#search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
idx = 0
x = 49

for el in num:
    if(el == x):
        print("number found at idx", idx)
        break
    idx += 1
