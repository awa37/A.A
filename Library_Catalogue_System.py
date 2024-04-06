class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Availability:", "Available" if self.available else "Not Available")

    def check_out(self):
        if self.available:
            self.available = False
            print("Book checked out successfully.")
        else:
            print("Sorry, the book is not available.")

    def return_book(self):
        self.available = True
        print("Book returned successfully.")

# Sample scenario
def main():
    # Create new books
    book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    # Display book information
    print("Book 1:")
    book1.display_info()
    print()

    print("Book 2:")
    book2.display_info()
    print()

    # Check out and return books
    book1.check_out()
    book2.check_out()
    print()

    book1.return_book()
    print()

    # Add new book
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print("New Book Added:")
    book3.display_info()

if __name__ == "__main__":
    main()

