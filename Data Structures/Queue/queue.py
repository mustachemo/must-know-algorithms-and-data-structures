# THERES A HELPER CLASS FOR QUEUE CALLED DEQUE

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from an empty queue")

    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue:", queue.items)
    print("Peek:", queue.peek())
    print("Dequeue:", queue.dequeue())
    print("Queue:", queue.items)
    print("Size:", queue.size())
