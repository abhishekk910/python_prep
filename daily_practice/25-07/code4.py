# 🚀 Problem 4: Find the Sum of All Even Numbers in a List

"""
🧩 Problem Statement:
Given a list of integers, write a program to find the **sum of all even numbers**.

📥 Input:
- A list of integers (e.g., [10, 21, 4, 45, 66, 93])

📤 Output:
- Sum of even numbers (e.g., 10 + 4 + 66 = 80)

🔁 Examples:
Input: [1, 2, 3, 4, 5, 6]   → Output: 12
Input: [11, 13, 17]         → Output: 0

🧠 Try solving it in:
1. Basic `for` loop with `if`
2. List comprehension + `sum()`
"""

# ✍️ Start coding below:


def even_number_sum(nums):
    # even_num_sum = 0
    # for num in nums: 
    #     if num%2 == 0:
    #         even_num_sum += num
    
    # return even_num_sum 
    return sum(num for num in nums if num%2 == 0)


print(even_number_sum([10, 21, 4, 45, 66, 93]))
print(even_number_sum([1, 2, 3, 4, 5, 6]))
print(even_number_sum([11, 13, 17]))