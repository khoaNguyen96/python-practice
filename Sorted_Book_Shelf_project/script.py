"""
Sorting books on a bookshelf with these methods:
    1. By author name
    2. By title name
    3. By number of characters in the title
    4. By the reverse of the author's name
"""

import utils
import sorts

# Sort the bookshelf by title ascending with bubble-sort
bookshelf = utils.load_books("book_small.csv")

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b["title_lower"]

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book["title"])
print("\n")

# Sort bookshelf by author ascending with bubble-sort
bookshelf_v1 = utils.load_books("book_small.csv")

def by_author_ascending(book_a, book_b):
    return book_a["author_lower"] > book_b["author_lower"]

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for book in sort_2:
    print(book["author"])
print("\n")

# Sort bookshelf with quicksort algorithm
bookshelf_v2 = utils.load_books("book_small.csv")
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
    print(book["author"])
print("\n")

# Sorting by the length of the sum of the number of characters in the book and author's name
def by_total_length(book_a, book_b):
    return (len(book_a["author"]) + len(book_a["title"])) > (len(book_b["title"]) + len(book_b["author"]))

long_bookshelf = utils.load_books("book_large.csv")
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
# sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)
for book in sort_3:

    print(len(book["author"])+len(book["title"]))