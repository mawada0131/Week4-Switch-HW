# Option A: Library Management System with Dictionaries

class Library:
    def __init__(self):
        self.books = {}  # book_id -> book details
        self.titles = {}  # title -> book_id
        self.authors = {}  # author -> list of book_ids

    def add_book(self, book_id, title, author, genre, year):
        self.books[book_id] = {"title": title, "author": author, "genre": genre, "year": year}
        
  
        self.titles[title] = book_id
    
        if author not in self.authors:
            self.authors[author] = []
        self.authors[author].append(book_id)

    def find_by_title(self, title):
        book_id = self.titles.get(title)
        return self.books.get(book_id, "Book not found.")

    def find_by_author(self, author):
        book_ids = self.authors.get(author, [])
        return [self.books[book_id] for book_id in book_ids] if book_ids else "No books found for this author."

library = Library()
library.add_book(1, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
library.add_book(2, "1984", "George Orwell", "Dystopian", 1949)

print(library.find_by_title("1984"))
print(library.find_by_author("F. Scott Fitzgerald"))
