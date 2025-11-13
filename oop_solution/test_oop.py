from library_oop import Library

print("=== TESTING CLASS: Library ===")

library = Library()

print("\n--- Adding Books ---")
library.add_book(1, "Animal Farm", "George Orwell", 3)
library.add_book(2, "The Alchemist", "Paulo Coelho", 2)
library.add_book(3, "To Kill a Mockingbird", "Harper Lee", 1)

print("\n--- Adding Members ---")
library.add_member(101, "Chalee", "Chalee@kmail.com")
library.add_member(102, "Anna", "Anna@kmail.com")

print("\n--- Display Available Books ---")
library.display_available_books()

print("\n--- Borrowing Books ---")
library.borrow_book(101, 1)
library.borrow_book(101, 2)
library.borrow_book(102, 1)

print("\n--- Display Member Books ---")
library.display_member_books(101)
library.display_member_books(102)

print("\n--- Available Books After Borrowing ---")
library.display_available_books()

print("\n--- Returning Books ---")
library.return_book(101, 1)
library.return_book(102, 1)

print("\n--- Display After Returns ---")
library.display_member_books(101)
library.display_available_books()

print("\n--- Error Handling Tests ---")
library.borrow_book(999, 1)
library.borrow_book(101, 999)
library.return_book(999, 1)
library.display_member_books(999)