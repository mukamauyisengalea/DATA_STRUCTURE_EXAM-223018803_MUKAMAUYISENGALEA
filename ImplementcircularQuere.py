from book import Book
class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, book):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = book

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return None
        book = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return book

# Example usage
cq = CircularQueue(3)
cq.enqueue(Book(1001, "Things Fall Apart", "Chinua Achebe"))
cq.enqueue(Book(1002, "1984", "George Orwell"))
cq.enqueue(Book(1003, "To Kill a Mockingbird", "Harper Lee"))

dequeued_book = cq.dequeue()
if dequeued_book:
    print(f"Dequeued book: {dequeued_book.title}")