# Write a recursive function to print all element in a list.
# Hint: use list & index as parameters.

def fun_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    fun_list(list, idx+1)

fruits = ["mango", "bananan", "orange", "apple", "graps"]

fun_list(fruits)