"""
count_unique_digits(122334)     ➞ 3   # Digits: 1, 2, 3, 4 → Unique: 1, 4
count_unique_digits(9876543210) ➞ 10  # All digits are unique
count_unique_digits(1111)       ➞ 1   # Only digit 1
count_unique_digits(1122334455) ➞ 0   # No unique digits

"""
number = 122334
# for i in str(number):
#     if number.count(i) == 1:
        

print(list(int(num) for num in str(number) if str(number).count(num) == 1))
