from collections import deque
from book import Book

class DynamicQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, book):
        self.queue.append(book)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue.popleft()

# Example usage
dq = DynamicQueue()
dq.enqueue(Book(1001, "Things Fall Apart", "Chinua Achebe"))
dq.enqueue(Book(1002, "1984", "George Orwell"))

book = dq.dequeue()
if book:
    print(f"Dequeued book: {book.title}")