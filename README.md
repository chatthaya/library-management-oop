# 📚 OOP Library Management System

## Project Overview
This project refactors a procedural library management system into an **Object-Oriented Programming (OOP)** design in Python.  
It allows management of:
- Books (add, track availability)  
- Members (register, track borrowed books)  
- Borrowing and returning books  
- Edge case handling: unavailable books, exceeding borrowing limit, invalid member/book IDs  

---

## Project Structure
library-management-oop/
│
├── README.md # This file
├── oop_solution
│      ├── library_oop.py # OOP implementation of library system
│      ├── test_oop.py # Test suite for OOP version
├── procedural_version
       ├── library_procedural.py # Original   procedural code
       └── test_procedural.py # Tests for procedural version


---

## Design Overview

### Book Class
- **Attributes:**  
  `id`, `title`, `author`, `total_copies`, `available_copies`  
- **Methods:**  
  `borrow()` — Decrease available copies if possible  
  `return_b()` — Increase available copies  
  `is_available()` — Check if book is available  

### Member Class
- **Attributes:**  
  `id`, `name`, `email`, `borrowed_books`  
- **Methods:**  
  `borrow_book(book)` — Borrow a book (max 3 books)  
  `return_book(book)` — Return a borrowed book  
  `show_borrowed_books()` — List all books borrowed by the member  

### Library Class
- **Attributes:**  
  `books` (list of Book objects), `members` (list of Member objects), `borrowed_records`  
- **Methods:**  
  `add_book(id, title, author, total_copies)` — Add a new book  
  `find_book(book_id)` — Return a book by ID  
  `add_member(id, name, email)` — Register a new member  
  `find_member(member_id)` — Return a member by ID  
  `borrow_book(member_id, book_id)` — Process borrowing  
  `return_book(member_id, book_id)` — Process returning  
  `display_available_books()` — Show all books with available copies  
  `display_member_books(member_id)` — Show books borrowed by a member  

---

## Testing

All tests are included in `test_oop.py`.

**Basic Tests:**
1. Add books and members  
2. Borrow and return books  
3. Display available books  
4. Display member’s borrowed books  

**Edge Cases:**
- Borrowing unavailable books  
- Borrowing more than 3 books  
- Returning books not borrowed  
- Borrowing/returning with invalid member or book IDs  

Run tests:

```bash
python test_oop.py
