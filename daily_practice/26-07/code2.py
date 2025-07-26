# 🧠 Problem 2: Count Digits Greater Than 5
# -----------------------------------------
# ❓ Problem Statement:
# Write a Python function that takes a positive integer as input and returns
# the count of digits that are greater than 5 in that number.

# 🧪 Example:
# Input: 493867
# Output: 3   (digits > 5 are: 9, 8, 6)

# 🔁 Try solving using:
# - While loop
# - Or Pythonic way using list/map/generator expression

# 📌 Your Turn:
def count_digits_gt_five(number):
    # count = 0
    # while number > 0:
    #     digit = number % 10
    #     if digit > 5:
    #         count += 1
    #     number = number // 10 
    # return count 
    return sum(1 for digit in str(number) if int(digit) > 5)

# 🔍 Test Cases
print(count_digits_gt_five(493867))  
print(count_digits_gt_five(4984))   
print(count_digits_gt_five(9876543210))  


