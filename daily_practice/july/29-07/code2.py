"""
Description:
Write a function that takes a string sentence and counts how many words start and end with the same letter (case-insensitive).
"""
def count_same_start_end_words(sentence: str) -> int:
    # count = 0
    # for i in sentence.split():
    #     if i[0].lower() == i[-1].lower():
    #         count += 1
    # return count 
    return sum(1 for word in sentence.split() if word[0].lower() == word[-1].lower())


print(count_same_start_end_words("Anna went to see civic duty"))  
# ➞ 2  (Anna, civic)



print(count_same_start_end_words("Python programming is great"))  
# ➞ 0

print(count_same_start_end_words("level madam noon stats"))  
# ➞ 4
