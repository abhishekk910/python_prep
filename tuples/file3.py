#Tuple Problem: Extract Even Numbers from Tuple
"""
Write a Python program to:

    Extract all even numbers from the tuple.

    Store them in a new tuple.

    Print the new tuple.
"""
numbers = (10, 15, 22, 33, 40, 55, 60)

even_tuples = tuple()
odd_tuples = tuple() 
for number in numbers:
    if number % 2 == 0:
        even_tuples += (number,)
    else:
        odd_tuples += (number,)
print(even_tuples)  

