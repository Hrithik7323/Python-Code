#3. Write a Python program using a while loop to iterate through each character of the string "Python" and print each character on a new line. 
#   Additionally, calculate and print the length of the string.

string = "Python"
index = 0
length = len(string)

#print(length)

while index < length:
    print(string[index])
    index += 1

print("Length of the string:", length)    