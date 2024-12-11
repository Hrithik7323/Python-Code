# Write a Python program that opens a file and handles a FileNotFoundError exception if the 
# file does not exit.

def read_file():

    try:

        file_name = input("Enter the file_name to open: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("The file does not exist.")