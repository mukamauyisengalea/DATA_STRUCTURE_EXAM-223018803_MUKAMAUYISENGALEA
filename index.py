# book class represents each book with attributes ISBN, title, author and availability
class Book:
    def __init__(self, isbn, title, author,availability):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.availability = availability
        self.left = None
        self.right = None
# binary search tree (BST) for efficient book searching based on isbn
class BST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        if not self.root:
            self.root = book
        else:
            self._insert_recursive(self.root, book)

    def _insert_recursive(self, node, book):
        if book.isbn < node.isbn:
            if node.left is None:
                node.left = book
            else:
                self._insert_recursive(node.left, book)
        elif book.isbn > node.isbn:
            if node.right is None:
                node.right = book
            else:
                self._insert_recursive(node.right, book)

    def search(self, isbn):
        return self._search_recursive(self.root, isbn)

    def _search_recursive(self, node, isbn):
        if node is None or node.isbn == isbn:
            return node
        if isbn < node.isbn:
            return self._search_recursive(node.left, isbn)
        return self._search_recursive(node.right, isbn)
# Min-Heap for priority reservations based on user priority
class Reservation:
    def __init__(self, user_id,book_isbn,priority):
        self.user_id = user_id
        self.book_isbn = book_isbn
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority
class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, reservation):
        self.heap.append(reservation)
        self._heapify_up(len(self.heap)-1)
    def _heapify_up(self, index):
        parent= (index-1)//2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    def remove_min(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    def _heapify_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest!= index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
# Circular Queue for handling cyclic reservations (e.g., when the borrowing period expires)

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, book):
        if self.is_full():
            print("Queue is full. Cannot add more books.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = book

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No books to borrow.")
            return None
        book = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return book

# Fixed Queue for managing a fixed number of orders in a specific borrowing session

class FixedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, book):
        if len(self.queue) >= self.capacity:
            print("Queue is full. Removing oldest request.")
            self.dequeue()  
        self.queue.append(book)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty.")
            return None
        return self.queue.pop(0)

# Tree structure to represent hierarchical data like book categories and subcategories
class CategoryNode:
    def __init__(self, genre_name):
        self.genre_name = genre_name
        self.subgenres = []  # A list to store subgenres
        self.books = []

    def add_subgenre(self, subgenre):
        self.subgenres.append(subgenre)

    def add_book(self, book):
        self.books.append(book)
class LibraryTree:
    def __init__(self):
        self.root = CategoryNode("Library")  # The root node represents the whole library

    def add_category(self, category_node):
        self.root.add_subgenre(category_node)

    def add_book_to_category(self, category_name, book):
        # Traverse the tree to find the right category and add a book
        category = self.find_category(self.root, category_name)
        if category:
            category.add_book(book)

    def find_category(self, node, category_name):
        if node.genre_name == category_name:
            return node
        for subgenre in node.subgenres:
            result = self.find_category(subgenre, category_name)
            if result:
                return result
        return None
# Heap sort to prioritize reservations by sorting based on the user priority
def heap_sort(reservations):
    min_heap = MinHeap()
    for res in reservations:
        min_heap.insert(res)

    sorted_reservations = []
    while len(min_heap.heap) > 0:
        sorted_reservations.append(min_heap.remove_min())
    
    return sorted_reservations
if __name__== '__main__':
    bst = BST()
    heap = MinHeap()
    # create some books
    book1 = Book(1001, "things fall apart", "M. Lea",True)
    book2 = Book(1002, "to kill a mockingbird", "Harper Lee",True)
    book3 = Book(1003, "The Great Gatsby", "F. Scott Fitzgerald", True)
    book4 = Book(1004, "1984", "George Orwell", True)
    book5 = Book(1005, "To Kill a Mockingbird", "Harper Lee", True)
   # insert book into bst
    bst.insert(book1)
    bst.insert(book2)
    bst.insert(book3)
    bst.insert(book4)
    bst.insert(book5)
    # search for a book by isbn
    book = bst.search(1002)
    if book:
        print(f"Found book: {book.title} by {book.author}")
    # Create reservations with priority
    reservation1 = Reservation(1, 1001, 2)  
    reservation2 = Reservation(2, 1002, 1)  
    reservation3 = Reservation(3, 1003, 3)  

    # Add reservations to the MinHeap
    heap.insert(reservation1)
    heap.insert(reservation2)
    heap.insert(reservation3)
    # Sort reservations by priority
    sorted_reservations = heap_sort([reservation1, reservation2, reservation3])
    print("Sorted reservations by priority:")
    for res in sorted_reservations:
        print(f"User ID: {res.user_id}, with  Priority: {res.priority}")
    # create circular queue for reservation
    cq = CircularQueue(3)
    cq.enqueue(book1)
    cq.enqueue(book2)
    cq.enqueue(book3)
    
    print(f"Dequeued book: {cq.dequeue().title}")
    print(f"Dequeued book: {cq.dequeue().title}")
    # Create a library tree for categories and subgenres
    tree = LibraryTree()
    fiction = CategoryNode("Fiction")
    fiction.add_subgenre(CategoryNode("Thriller"))
    fiction.add_subgenre(CategoryNode("Romance"))
    tree.add_category(fiction)

    # Add books to categories
    tree.add_book_to_category("Fiction", book1)
    tree.add_book_to_category("Fiction", book2)
    tree.add_book_to_category("Romance", book3)
    tree.add_book_to_category("Romance", book4)
    

    print("Books in Fiction Category:")
    for book in fiction.books:
        print(book.title)