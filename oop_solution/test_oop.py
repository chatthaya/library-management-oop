from library_oop import Book

print("=== TESTING CLASS: Book ===")

b1 = Book(1, "The Alchemist", "Paulo Coelho", 3)

print(f"Title: {b1.title}")
print(f"Author: {b1.author}")
print(f"Total copies: {b1.total_copies}")
print(f"Available copies: {b1.available_copies}")

print("\n--- Borrowing copies ---")
b1.borrow()
b1.borrow()
print(f"Available copies after 2 borrows: {b1.available_copies}") 

print("\n--- Trying to borrow more than available ---")
borrow_success = b1.borrow() 
print(f"Borrow success? {borrow_success}")
print(f"Available copies now: {b1.available_copies}")

print("\n--- Returning a copy ---")
b1.return_b()
print(f"Available copies after return: {b1.available_copies}")