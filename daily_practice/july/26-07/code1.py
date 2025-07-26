# 💻 Problem Statement:
# Write a Python program that takes a positive integer as input
# and counts how many digits are even and how many are odd.

# 📥 Input Example:
# Enter a number: 438975

# 📤 Output:
# Even digits: 3
# Odd digits: 3

# ✅ Try solving this using a `while` loop.
# (Don’t use string conversion or list comprehension yet.)

# def count_even_odd(number):

#     even_number_count = 0
#     odd_number_count = 0
#     while number > 0:
#         digit = number % 10
#         if digit % 2 == 0: 
#             even_number_count += 1
#         else:
#             odd_number_count += 1
#         number = number // 10 
#     return f"Even numbers count : {even_number_count}, Odd Numbers count : {odd_number_count}"

# print(count_even_odd(438975))
# print(count_even_odd(2345))
# print(count_even_odd(1234567890))

number = 438975
digits = list(map(int, str(number)))
even_number_count = sum(1 for digit in digits if digit %2 == 0)
print("Even Count", even_number_count)
print("odd Count", len(digits) - even_number_count)