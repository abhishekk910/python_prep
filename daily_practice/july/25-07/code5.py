# 🚀 Problem 5: Check for Palindrome Number

"""
🧩 Problem Statement:
Write a program that checks if a given **positive integer** is a **palindrome**.

A palindrome number is the same when reversed.
(e.g., 121, 1331, 12321)

📥 Input:
- A positive integer (e.g., 121)

📤 Output:
- True if it's a palindrome, else False

🔁 Examples:
Input: 121     → Output: True
Input: 123     → Output: False
Input: 9999    → Output: True

🧠 Try solving it in:
1. Using string slicing
2. Without converting to string (with arithmetic)
"""

# ✍️ Start coding below:

def check_palindrome(num):
    # if num == int(str(num)[::-1]):
    #     return True
    # return False

    temp = num
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev == num



print(check_palindrome(121))
print(check_palindrome(123))
print(check_palindrome(9999))
