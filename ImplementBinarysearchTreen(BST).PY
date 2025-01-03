from book import Book

class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if not self.root:
            self.root = BSTNode(book)
        else:
            self._insert(self.root, book)

    def _insert(self, node, book):
        if book.isbn < node.book.isbn:
            if node.left:
                self._insert(node.left, book)
            else:
                node.left = BSTNode(book)
        else:
            if node.right:
                self._insert(node.right, book)
            else:
                node.right = BSTNode(book)

    def search(self, isbn):
        return self._search(self.root, isbn)

    def _search(self, node, isbn):
        if not node:
            return None
        if isbn == node.book.isbn:
            return node.book
        elif isbn < node.book.isbn:
            return self._search(node.left, isbn)
        else:
            return self._search(node.right, isbn)

# Example usage
bst = BST()
bst.insert(Book(1001, "Things Fall Apart", "Chinua Achebe"))
bst.insert(Book(1002, "1984", "George Orwell"))
bst.insert(Book(1003, "To Kill a Mockingbird", "Harper Lee"))

book = bst.search(1002)
if book:
    print(f"Found Book: {book}")
else:
    print("Book not found.")
