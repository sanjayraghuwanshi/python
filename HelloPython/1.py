"""
### Day 1 — List Basics & Indexing
**Problem:**
You are managing a bookshelf. Create a list of 5 book titles. Then:
1. Print the first and last book using indexing.
2. Add a new book at the end.
3. Insert a book at position 2.
4. Remove the third book.
5. Print the final list and its length.

**Concepts:** `append()`, `insert()`, `remove()`, indexing, `len()`
"""

book_titles = ['book1','book2','book3','book4','book5']
print(f"First Book : {book_titles[0]}, Last Book : {book_titles[-1]}")
book_titles.append("book6")
print(f"Last Book : {book_titles[-1]}")
book_titles.insert(2,"book7")
print(f"Printing book at second position : {book_titles[2]}")
book_titles.pop(3)
print (f"{book_titles} and length is {len(book_titles)}")   