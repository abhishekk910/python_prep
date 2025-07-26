"""
Write a program that takes a list of space-separated integers as input and prints a list of their squares using the map() function.

🔹 Example:
Input: 1 2 3 4 5
Output: [1, 4, 9, 16, 25]

Try it using map() and lambda or a separate function.

result = list(map(lambda x: x * x, iterable))

"""

res = list(map(lambda x:x** 2, [1,2,3,4,5])) 

print(res)


