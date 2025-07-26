# 📝 Problem Statement:
# Write a Python function that takes a positive integer as input
# and returns the product of all its digits.

# Example:
# Input: 231
# Output: 6   (2 * 3 * 1)

# Input: 450
# Output: 0   (4 * 5 * 0 = 0)

import math 
def return_product(number):
    # if "0" in str(number):
    #     return 0 
 
    # product = 1 
    # while number > 0:
    #     digit = number % 10 
    #     product = product * digit
    #     number = number // 10 
    # return product
    return 0 if "0" in str(number) else math.prod(map(int, str(number)))

print(return_product(231))
print(return_product(450))