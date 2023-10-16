class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        current = self.head
        if not current:
            new_node.next = new_node  # Circular reference to itself
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        current = self.head
        prev = None
        while current.next != self.head:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def display(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")


# Example usage:
if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()
    circular_linked_list.append(1)
    circular_linked_list.append(2)
    circular_linked_list.append(3)
    circular_linked_list.prepend(0)
    circular_linked_list.display()
    circular_linked_list.delete(2)
    circular_linked_list.display()
