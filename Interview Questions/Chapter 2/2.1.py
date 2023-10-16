# 3 Remove Dups: Write code to remove duplicates from an unsorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = None
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_duplicates(self):
        current = self.head
        values = []

        while current:
            values.append(current.data)
            current = current.next
        print(values)


# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.prepend(0)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.display()
    linked_list.delete(2)
    linked_list.display()
    linked_list.remove_duplicates()
