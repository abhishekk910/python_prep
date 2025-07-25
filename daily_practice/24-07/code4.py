"""
Problem 4: Reverse a Number
❓ Problem Statement:
Write a program that takes an integer input and prints the reverse of that number.

🔹 Example:
Input: 1234

Output: 4321
"""

input_number = int(input("Enter a number to reverse : "))
print(input_number, type(input_number))

# output_number = str(input_number)[::-1] 
# print("reverse number ", int(output_number))


reverse_number = 0

while input_number > 0:
    remainder = input_number % 10 
    input_number //= 10 
    reverse_number = reverse_number * 10 + remainder

print("reverse number ", int(reverse_number))