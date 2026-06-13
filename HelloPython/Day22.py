"""
Day 22 — Reading & Writing Text Files
Problem:
=======
Write a program that creates a file notes.txt and writes 5 lines of any text to it.
Read the file back and print each line with its line number.
Append 3 more lines to the same file without overwriting.
Count the total number of lines and words in the file.
Search the file for a word (user input) and print all lines containing it.
Concepts: open(), write(), read(), readlines(), with statement, modes r/w/a
"""

with open('Day22.txt', "w") as file:
    file.write(
        """Write a program that creates a file notes.txt and writes 5 lines of any text to it.
        Read the file back and print each line with its line number.
        Append 3 more lines to the same file without overwriting.
        Count the total number of lines and words in the file.
        Search the file for a word (user input) and print all lines containing it.
        Concepts: open(), write(), read(), readlines(), with statement, modes r/w/a"""
    )
with open('Day22.txt', "r") as file:
    for line_num, content in enumerate(file, 1):
        print(f"Line  {line_num}: {content.strip()}")

with open('Day22.txt', "a") as file:
    file.write("\nAppending line 1"
               "\nAppending line 2"
               "\nAppending line 3"
               "\nAppending line 4")

with open('Day22.txt', "r") as file:
    print(f"\nHere comes the appended output")
    for line_num, content in enumerate(file, 1):
        print(f"Line  {line_num}: {content.strip()}")


line_count = 0
word_count = 0

with open("Day22.txt", "r") as file:
    for line in file:
        line_count += 1
        # .split() breaks the line into a list of words based on whitespace
        words = line.split()
        word_count += len(words)

print(f"Total Lines: {line_count}")
print(f"Total Words: {word_count}")

search_term = input("Enter search term: ").lower()
found = False

with open("Day22.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        if search_term in line.lower():
            print(f"Line  {line_num}: {line.strip()}")
            found = True
if not found:
    print(f"The word {search_term} was not found in the file.")