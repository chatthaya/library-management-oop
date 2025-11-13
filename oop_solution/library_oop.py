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