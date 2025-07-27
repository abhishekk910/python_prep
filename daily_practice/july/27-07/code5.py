"""
Problem: Sum of Digits Until Single Digit
Description:
Given an integer number, repeatedly sum its digits until the result is a single-digit number. Return that single-digit.

sum_to_single_digit(942)       ➞ 6    # 9 + 4 + 2 = 15 → 1 + 5 = 6  
sum_to_single_digit(132189)    ➞ 6    # 1+3+2+1+8+9 = 24 → 2+4 = 6  
sum_to_single_digit(493193)    ➞ 2    # 4+9+3+1+9+3 = 29 → 2+9 = 11 → 1+1 = 2
sum_to_single_digit(9)         ➞ 9    # Already a single-digit

"""

def sum_to_single_digit(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
        print(n)
    return n

print(sum_to_single_digit(493193))