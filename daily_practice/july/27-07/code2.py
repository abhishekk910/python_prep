from collections import Counter

number = 9988776655
digits = str(number)
freq = Counter(digits)

print(freq)
print(freq.keys())
print(freq.values())
for digit, count in freq.items():
    print(digit, count)

max_freq = max(freq.values())
# print(max_freq)

most_frequent_digits = [int(digit) for digit, count in freq.items() if count == max_freq]
print(min(most_frequent_digits))