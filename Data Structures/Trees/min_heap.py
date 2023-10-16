# MinHeap is a class representing the min heap. It uses a list to store the elements.

# The insert method adds a value to the min heap and ensures that the heap property is maintained by calling _heapify_up to move the value up the tree as needed.

# The extract_min method removes and returns the minimum value (the root of the heap) and then restores the heap property by calling _heapify_down to move the last element down the tree.

# The _heapify_up method is used during insertion to move a newly inserted value up the tree as long as it's smaller than its parent.

# The _heapify_down method is used during extraction to move the root value down the tree to the correct position.

# The peek method allows you to see the minimum value without removing it from the heap.

# The size method returns the number of elements in the heap.

# The is_empty method checks if the heap is empty.


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] < self.heap[smallest]
        ):
            smallest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] < self.heap[smallest]
        ):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

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
    min_heap = MinHeap()
    values = [5, 9, 3, 10, 2, 7, 6]

    for value in values:
        min_heap.insert(value)

    print("Min Heap:")
    while not min_heap.is_empty():
        print(min_heap.extract_min())
