#WAF to print the elements of a list a single line. (list is the parameter)

cities = ["patna", "modinagar", "digha", "danapur"]
heroes = ["krish", "krishna", "jiwan", "saktiman", "hanuman"]

def print_len(list):
    for item in list:
        print(item, end=" ")

print_len(heroes)        

