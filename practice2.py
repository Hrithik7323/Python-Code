#WAP to check if a list contains a palindrome of elements. (Hind use copy()method)

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1  = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")