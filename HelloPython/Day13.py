"""
Day 13 — Counting & Grouping with Dictionaries
Problem: Given a sentence (use any long sentence you like — at least 15 words):

1. Count the frequency of each word (case-insensitive, ignore punctuation).
2. Find the top 3 most frequent words.
3. Group words by their first letter into a dictionary of lists.
    Example: {"a": ["and", "apple"], "b": ["bird"], ...}
4. Find which letter group has the most words.
Concepts: .get(), defaultdict style logic, string methods, sorting
"""
from collections import defaultdict
import string

sentence = "this is a sentence for problem solving for day 13 and I am trying to produce the sentence with atleast 15 words"
# 1
clean_sentence = sentence.lower().strip()
words = clean_sentence.split(" ")
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print(f"{word_counts}")

# 2
sorted_counts = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
top3 = sorted_counts[:3]
print(f"{top3}")

# 3
grouped = {}
for word in words:
    first_char = word[0]
    # If key doesn't exist, start an empty list, then append
    if first_char not in grouped:
        grouped[first_char] = []

    # Avoid duplicate words in the same list
    if word not in grouped[first_char]:
        grouped[first_char].append(word)
print(grouped)

# 4
max_letter = max(grouped, key=lambda k: len(grouped[k]))
print(f"The letter group with the most words is '{max_letter}' with {len(grouped[max_letter])} words.")