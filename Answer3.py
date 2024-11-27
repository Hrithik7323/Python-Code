# Using max() and min() function display the maximum and minimum of 5 random numbers.

import random

random_numbers = [random.randint(1, 100) for _ in range(5)]

max_numbers = max(random_numbers)
min_numbers = min(random_numbers)

print("The random num are : {random_num}")
print("The max_num is : {max_num}")
print("The min_num is : {min_num}")


