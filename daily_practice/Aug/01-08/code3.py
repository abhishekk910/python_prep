# def first_non_repeating_char(s: str) -> str:
    
#     for i in s:
#         if s.count(i) == 1:
#             return i 

# print(first_non_repeating_char("aabbcde"))


from collections import Counter

def first_non_repeating_char(s: str) -> str:
    freq = Counter(s)
    print(freq)
    for char in s:
        if freq[char] == 1:
            return char
    return "None"

print(first_non_repeating_char("aabbcde"))