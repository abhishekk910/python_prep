"""
Problem Statement:
Count the number of digits in a number that are divisible by 3

🔍 Example:
python
Copy
Edit
Input: 93126  
Output: 3  
# Explanation: Digits divisible by 3 are: 9, 3, 6
"""
def count_digits_div_by_3(number):
    count = 0
    while number > 0:
        digit = number % 10 
        if digit % 3 == 0:
            count += 1
        number = number // 10


    
    return count

print(count_digits_div_by_3(123456789))     # Output: 3 → digits: 3, 6, 9
print(count_digits_div_by_3(303))           # Output: 3 → digits: 3, 0, 3 (0 is divisible by 3)
print(count_digits_div_by_3(1001))          # Output: 1 → digit: 0
print(count_digits_div_by_3(222222))        # Output: 0 → no digit divisible by 3
print(count_digits_div_by_3(99999))         # Output: 5 → all 9s
