"""
Check if Two Strings are Anagrams
Write a function that checks whether two given strings are anagrams.
Two strings are anagrams if they contain the same characters with the same frequencies, but possibly in a different order.
"""

word1 = "listen"
word2 = "silent"
# dict1 = {}
# dict2 = {}

# for i in word1: 
#     if i not in dict1:
#         dict1[i] = 1
#     else:
#         dict1[i] += 1

# print(dict1)

from collections import Counter

def are_anagrams(word1, word2):
    return Counter(word1) == Counter(word2)

print(are_anagrams("listen", "silent"))   # True
print(are_anagrams("hello", "world"))     # False
