"""
Write a Python function that returns the first character that appears more than once in a string.
If there is no repeating character, return "None".
"""

from collections import Counter

def first_repeating_char(s: str) -> str:
    freq = Counter(s)
    # print(freq)
    for char in s:
        if freq[char] > 1:
            return char
    return "None"

print(first_repeating_char("aabbcde"))
print(first_repeating_char("abc"))