class Book:
    def __init__(self, id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_b(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False


class Member:
    def __init__(self, id, name, email="N/A"):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = [] 

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        if not book.borrow():
            print("Error: No copies available!")
            return False
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'")
        return True
    
    def return_book(self, book):
        if book not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        self.borrowed_books.remove(book)
        book.return_b()
        print(f"{self.name} returned '{book.title}'")
        return True
    
    
class Library:
    """A simple library system to manage books and members."""

    def __init__(self):
        self.book_list = []
        self.member_list = []
        self.borrowed_records = []

        self.members = self.member_list
        self.books = self.book_list
        self.borrowed_books = self.borrowed_records
        
    def add_book(self, book_id, title, author, total_copies):
        """Add a new book to the library."""
        if any(book.id == book_id for book in self.book_list):
            print(f"Error: Book ID {book_id} already exists!")
            return

        book = Book(book_id, title, author, total_copies)
        self.book_list.append(book)
        print(f"Book '{book.title}' added successfully!")

    def find_book(self, book_id):
        """Find and return a book by its ID."""
        for book in self.book_list:
            if book.id == book_id:
                return book
        return None

    def add_member(self, member_id, name, email="N/A"):
        """Register a new library member."""
        if any(member.id == member_id for member in self.member_list):
            print(f"Error: Member ID {member_id} already exists!")
            return

        member = Member(member_id, name, email)
        self.member_list.append(member)
        print(f"Member '{member.name}' registered successfully!")

    def find_member(self, member_id):
        """Find and return a member by ID."""
        for member in self.member_list:
            if member.id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        """Allow a member to borrow a book."""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Error: Member not found!")
            return False
        if not book:
            print("Error: Book not found!")
            return False

        if member.borrow_book(book):
            self.borrowed_records.append({
                "member_id": member.id,
                "member_name": member.name,
                "book_id": book.id,
                "book_title": book.title,
            })
            return True

        return False

    def return_book(self, member_id, book_id):
        """Allow a member to return a borrowed book."""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or book not found!")
            return False

        if member.return_book(book):
            self.borrowed_records = [
                record for record in self.borrowed_records
                if not (
                    record["member_id"] == member.id
                    and record["book_id"] == book.id
                )
            ]
            return True

        return False

    def display_available_books(self):
        """Display all available books in the library."""
        print("\n=== Available Books ===")
        for book in self.book_list:
            if book.available_copies > 0:
                print(
                    f"{book.title} by {book.author} "
                    f"- {book.available_copies} copies available"
                )

    def display_member_books(self, member_id):
        """Display all books currently borrowed by a specific member."""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if member.borrowed_books:
            for book in member.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books currently borrowed.")
