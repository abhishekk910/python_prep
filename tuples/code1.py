"""
🧩 Problem 1: Tuple Index Finder

You are given a tuple of integers. Your task is to write a Python program that:

1. Takes a number as input from the user.
2. Searches for that number in the tuple.
3. If found, prints the index of its first occurrence.
4. If not found, print a message saying the number is not in the tuple.

Example:
----------
numbers = (5, 8, 12, 7, 8, 15)

Input: 8
Output: 1

Input: 10
Output: 10 is not in the tuple
"""
tuple_numbers = (5, 8, 12, 7, 8, 15)

number = int(input("Enter a number to search in the tuple: "))



if number in tuple_numbers:
    print(f"The index of {number} is: {tuple_numbers.index(number)}")
else:
    print(f"{number} is not in the tuple")
        
        