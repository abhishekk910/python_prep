"""
# ❓ Problem Statement:
# Write a program that takes a string input and counts how many vowels are in it.
# (Vowels = a, e, i, o, u — both uppercase and lowercase)

# 🔹 Example:
# Input: "Python is Awesome"
# Output: 6

"""
input_string =  "Python is Awesome"
# count = 0
# for i in input_string: 
#     if i in "aeiouAEIOU":
#         count += 1
# print(count)


res = sum(1 for i in input_string if i in "aeiouAEIOU")
print(res)
