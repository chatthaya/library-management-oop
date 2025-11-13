from library_oop import Book, Member

print("=== TESTING CLASS: Member ===")

m1 = Member(101, "Chalee", "Chalee@kmail.com")

b1 = Book(1, "The Alchemist", "Paulo Coelho", 2)
b2 = Book(2, "Animal Farm", "George Orwell", 1)

print("\n--- Member info ---")
print(f"ID: {m1.id}")
print(f"Name: {m1.name}")
print(f"Email: {m1.email}")
print(f"Borrowed books: {len(m1.borrowed_books)}")

print("\n--- Borrowing books ---")
m1.borrow_book(b1)
m1.borrow_book(b2)

print(f"Books borrowed by {m1.name}:")
for book in m1.borrowed_books:
    print(f"  - {book.title}")

print("\n--- Trying to borrow more than 3 books ---")
b3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
b4 = Book(4, "Design Patterns", "Gang of Four", 1)
m1.borrow_book(b3)
m1.borrow_book(b4)

print(f"\nBorrowed books count: {len(m1.borrowed_books)}")

print("\n--- Returning a book ---")
m1.return_book(b1)
print(f"Books remaining after return:")
for book in m1.borrowed_books:
    print(f"  - {book.title}")

print("\n--- Returning a book not borrowed ---")
m1.return_book(b1)