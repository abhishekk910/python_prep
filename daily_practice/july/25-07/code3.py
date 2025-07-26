

"""
🧩 Problem Statement:
Write a Python program that takes a positive integer as input 
and counts how many digits are in that number.

📥 Input:
- A single positive integer (e.g., 73421)

📤 Output:
- The total number of digits (e.g., 5)

🔁 Examples:
Input: 123     → Output: 3
Input: 98976   → Output: 5

🧠 Try solving it in:
1. While loop method
2. One-line using len(str(...))
"""

# num = 123
num = 98976 

# print(len(str(num)))


count = 0
while num > 0: 
    
    num = num // 10 
    count += 1
    
print(count)