"""
Problem 2: Find the Maximum of Three Numbers
"""

num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split()) 
print(num1, num2, num3)

# print(max(num1,  num2,num3)) 


# if num1 > num2 and num1 > num3: 
#     print(f"{num1} is max number")
# elif num2 > num3:
#     print(f"{num2} is max number")
# else:
#     print(f"{num3} is max number") 


if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the maximum number")
    else:
        print(f"{num3} is the maximum number")
else:
    if num2 > num3:
        print(f"{num2} is the maximum number")
    else:
        print(f"{num3} is the maximum number")


