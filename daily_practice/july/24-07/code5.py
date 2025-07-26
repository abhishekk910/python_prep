# 🧩 Problem 5: Sum of Digits of a Number

# ❓ Problem Statement:
# Write a program that takes a positive integer and calculates 
# the sum of its digits.

# 🔹 Example:
# Input: 1234
# Output: 10  (because 1 + 2 + 3 + 4 = 10)

# input_number = int(input("Please enter a positive integer number : "))
# sum = 0 
# while input_number > 0:
#     remainder = input_number % 10 
#     input_number //= 10
#     sum += remainder
# print(sum)


input_number = input("Please enter a positive integer number: ")
print(sum(map(int, input_number)))