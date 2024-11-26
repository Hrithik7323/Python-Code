#Create a new file "practice.txt" using python. Acc the following dat in it:
# Hi everyone
# we are learning File I/O
# using Java.
# i like programmering in Java.

 #with open("practice.txt", "w") as f:
 #   f.write("Hi everyone\nwe are learning File I/O\nusing Java.\n")
 #   f.write("I like programming in Java.")


# Q2 WAF that replace all occurrence of " java" with "python" in file.

#with open("practice.txt", "r") as f:
#    data = f.read()

#new_data = data.replace("Java", "Python")
#print(new_data)

#with open("practice.txt", "w") as f:
#    data = f.write(new_data)


# Q3 Search if the word "learing" exist in the file or not.

#def check_for_word():
#    word = "learning"
#    with open("practice.txt", "r") as f:
#        data = f.read()
#        if(word in data):
#            print("fond")
#        else:
#            print("not found")
#check_for_word()


# Q4 WAF to find in which line of the file does the word "learning" occur first.
# Print-1 if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())   




