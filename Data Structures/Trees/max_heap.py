# MaxHeap is a class representing the max heap. It uses a list to store the elements.

# The insert method adds a value to the max heap and ensures that the heap property is maintained by calling _heapify_up to move the value up the tree as needed.

# The extract_max method removes and returns the maximum value (the root of the heap) and then restores the heap property by calling _heapify_down to move the last element down the tree.

# The _heapify_up method is used during insertion to move a newly inserted value up the tree as long as it's greater than its parent.

# The _heapify_down method is used during extraction to move the root value down the tree to the correct position.

# The peek method allows you to see the maximum value without removing it from the heap.

# The size method returns the number of elements in the heap.

# The is_empty method checks if the heap is empty.

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] > self.heap[largest]
        ):
            largest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] > self.heap[largest]
        ):
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


# Example usage:
if __name__ == "__main__":
    max_heap = MaxHeap()
    values = [5, 9, 3, 10, 2, 7, 6]

    for value in values:
        max_heap.insert(value)

    print("Max Heap:")
    while not max_heap.is_empty():
        print(max_heap.extract_max())
