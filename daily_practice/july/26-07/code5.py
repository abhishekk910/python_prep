"""
Problem: Find the Sum of Digits at Even Positions (from Right)
🧠 Description:
Given a positive integer, write a function to return the sum of digits at even positions, starting from the right (i.e., units place is position 1).

📌 Example:
For number 483921
From right:

Position 1 → 1 (odd)

Position 2 → 2 (✅ even)

Position 3 → 9

Position 4 → 3 (✅ even)

Position 5 → 8

Position 6 → 4 (✅ even)

So, sum = 2 + 3 + 4 = 9

print(sum_even_position_digits(483921))    # Output: 9 (digits: 2, 3, 4)
print(sum_even_position_digits(1234))      # Output: 4 (digits: 2, 2)
print(sum_even_position_digits(7))         # Output: 0
print(sum_even_position_digits(24680))     # Output: 12 (digits: 8, 4)

"""
# num = 24680
# print(str(num)[::-1])
# counter = 0
# res = 0 
# for i in str(num)[::-1]:
#     counter += 1
#     if counter % 2 == 0:
#         res += int(i)


num = 24680
digits = str(num)[::-1]
res = sum(int(d) for i, d in enumerate(digits, start=1) if i % 2 == 0)
print(res)

