from book import Book
class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, book):
        if len(self.queue) >= self.capacity:
            print("Queue is full.")
        else:
            self.queue.append(book)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue.pop(0)

# Example usage
queue = Queue(2)
queue.enqueue(Book(1001, "Things Fall Apart", "Chinua Achebe"))
queue.enqueue(Book(1002, "1984", "George Orwell"))
queue.enqueue(Book(1003, "To Kill a Mockingbird", "Harper Lee"))

book = queue.dequeue()
if book:
    print(f"Dequeued book: {book.title}")