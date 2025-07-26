"""
Problem: Count Digits That Are Prime
Problem Statement:
Write a function that counts how many digits in a number are prime digits.

Prime digits are: 2, 3, 5, 7.


"""
# number = 1234567890
# prime_digits = [2, 3, 5, 7]
# total_count = sum(1 for num in str(1234567890) if int(num) in prime_digits)
# print(total_count)

def count_prime_digits(number):
    prime_digits = [2, 3, 5, 7]
    count = 0
    # return sum(1 for num in str(number) if int(num) in prime_digits)
    while number > 0:
        digit  = number % 10 
        if digit in prime_digits:
            count += 1 
        number = number // 10 
    return count


print(count_prime_digits(2357))       # ➞ 4  (All digits are prime)
print(count_prime_digits(1234567890))  # ➞ 4  (Digits 2, 3, 5, 7)
print(count_prime_digits(4680))        # ➞ 0  (No prime digits)

