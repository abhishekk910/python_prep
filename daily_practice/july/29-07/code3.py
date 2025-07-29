# str = "Each word must be unique"
# for i in str.split():
#     print(set(i), i)
#     print(len(set(i)), len(i))
    


def remove_words_with_duplicates(sentence):
    return " ".join(list(word for word in sentence.split() if len(set(word.lower())) == len(word.lower())))

print(remove_words_with_duplicates("Each word must be unique"))  
# ➞ "Each word be"

print(remove_words_with_duplicates("Hello world"))  
# ➞ "world"

print(remove_words_with_duplicates("Python is fun"))  
# ➞ "Python is fun"

print(remove_words_with_duplicates("I love programming"))  
# ➞ "I"
