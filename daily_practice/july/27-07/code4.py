"""
Problem: Check for Palindromic Number
Write a function that checks if a given integer number is a palindrome.
A number is a palindrome if it remains the same when its digits are reversed.

print(is_palindrome_number(121))      # ➞ True
print(is_palindrome_number(12321))    # ➞ True
print(is_palindrome_number(123))      # ➞ False
print(is_palindrome_number(1001))     # ➞ True
print(is_palindrome_number(10))       # ➞ False

"""

def is_palindrome_number(number: int) -> bool:
    if str(number) == str(number)[::-1]:
        return True
    return False

print(is_palindrome_number(121))      # ➞ True
print(is_palindrome_number(12321))    # ➞ True
print(is_palindrome_number(123))      # ➞ False
print(is_palindrome_number(1001))     # ➞ True
print(is_palindrome_number(10))       # ➞ False
