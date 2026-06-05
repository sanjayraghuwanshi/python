"""
Day 11 — Dictionary Comprehensions
Problem:

1. Create a dictionary of {number: square} for numbers 1–10 using a comprehension.
2. From a list of words ["sky", "ocean", "mountain", "river", "cloud"], create a dict of {word: length}.
3. Filter the above to only include words with length > 4.
4. Invert a dictionary: {"a": 1, "b": 2, "c": 3} → {1: "a", 2: "b", 3: "c"}.
   Concepts: Dictionary comprehensions, .items(), filtering
"""

# 1
num_squares = {}
for number in range(1, 11):
    number_str = str(number)
    square = number ** 2
    num_squares[number_str] = square
print(num_squares)

# 2
words = ["sky", "ocean", "mountain", "river", "cloud"]
word_len = {}
for word in words:
    word_str = word
    length = len(word_str)
    word_len[word_str] = length
print(word_len)

# Dictionary comprehension
word_length = {word: len(word) for word in words}
print(word_length)

# 3
lengthy_words = {word: len(word) for word in words if len(word) > 4}
print(lengthy_words)

# 4
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print(inverted)