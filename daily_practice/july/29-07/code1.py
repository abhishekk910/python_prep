"""Problem Statement:
Write a Python function that takes a string as input and returns a dictionary where each vowel (a, e, i, o, u) is a key and its value is the number of times it appears in the string (case-insensitive).
"""

def count_vowels(text: str) -> dict:
    result = {}
    text = text.lower()
    for i in text:
        if i in "aeiou":
            result[i] = result.get(i, 0) + 1
    return result

print(count_vowels("Automation Testing"))  
# ➞ {'a': 1, 'u': 1, 'o': 2, 'i': 2, 'e': 1}

print(count_vowels("HELLO World"))  
# ➞ {'e': 1, 'o': 2}

print(count_vowels("PYTHON"))  
# ➞ {'o': 1}

print(count_vowels("qwrtypsdfghjklzxcvbnm"))  
# ➞ {}   # no vowels

print(count_vowels("aeiouAEIOU"))  
# ➞ {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}



