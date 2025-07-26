"""
# ❓ Problem Statement:
# Given a list of integers, print all the even numbers in that list.

# 🔹 Example:
# Input: [10, 15, 22, 33, 40]
# Output: [10, 22, 40]

"""
nums = [10, 15, 22, 33, 40] 


res = []
temp = [res.append(num) for num in nums if num%2==0]
print(res)
print(temp)