"""
Given an integer number, write a function to count how many digits in the number are strictly less than the average of all digits in that number.
"""
# number = 3056

# average = sum(map(int, str(number)))/ len(str(number))
# total_sum = 0
# i = 0
# while number > 0:
#     digit = number % 10 
#     total_sum = total_sum + digit 
#     number = number // 10 
#     i += 1

# print(total_sum/i)

# print(average)
# counter = 0
# while number > 0:
#     digit = number % 10 
#     if digit > average:
#         counter += 1
# return counter 
    

def count_digits_below_average(number):
    average = sum(map(int, str(number)))/ len(str(number))
    counter = 0
    while number > 0:
        digit = number % 10 
        if digit < average:
            counter += 1
        number = number // 10 
    return counter 

print(count_digits_below_average(12345))     # ➞ 2 (Average = 3.0 → digits < 3: 1, 2)
print(count_digits_below_average(55555))     # ➞ 0 (Average = 5.0 → no digit < 5)
print(count_digits_below_average(987654321)) # ➞ 4 (Average = 5.0 → digits < 5: 1, 2, 3, 4)
print(count_digits_below_average(111))       # ➞ 0 (Average = 1.0)
print(count_digits_below_average(3056))      # ➞ 2 (Average = 3.5 → digits < 3.5: 0, 3)
print(count_digits_below_average(30569))