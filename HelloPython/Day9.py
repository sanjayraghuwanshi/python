"""
Day 9 — Iterating Dictionaries
Problem: You have a word frequency dictionary: {"python": 5, "code": 3, "list": 7, "loop": 2, "dict": 6, "function": 4}

1. Print all words with frequency > 4.
2. Find the word with the highest frequency.
3. Sort the dictionary by frequency (highest first) and print it.
4. Create a new dictionary with only words that have 4+ letters.
Concepts: .items(), sorting dicts, dictionary comprehensions
"""

word_frequency = {"python": 5, "code": 3, "list": 7, "loop": 2, "dict": 6, "function": 4}

# 1
for key, val in word_frequency.items():
    if val > 4:
        print(f"{key} : {val}")

# 2
# max(data): By default, this only looks at the keys alphabetically ("python" would be the max).
# key=data.get: This forces max to evaluate the values (5, 3, 7...) while still returning the key ("list") associated with the highest number.

highest_frequency = max(word_frequency, key=word_frequency.get)
print(f"{highest_frequency}:  {word_frequency[highest_frequency]}")

# 3
sorted_by_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
print(f"{next(iter(sorted_by_frequency))}")

# 4
filtered_dict = {word: count for word, count in word_frequency.items() if len(word) >= 4}
print(filtered_dict)