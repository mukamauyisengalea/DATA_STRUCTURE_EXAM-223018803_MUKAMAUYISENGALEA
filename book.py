class Book:
    def __init__(self, isbn, title, author, availability=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.availability = availability

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Available: {self.availability})"
