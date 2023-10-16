# A disjoint-set (or union-find) data structure is used to maintain a
# collection of disjoint (non-overlapping) sets with two main operations:
# union (merge two sets) and find (determine which set an element belongs to).
# Here's a basic implementation of a disjoint-set in Python using the
# union-by-rank and path compression techniques, which ensure efficient operations:

# The DisjointSet class initializes the disjoint-set data structure with a specified size, where each element is initially its own representative.

# The find method finds the representative (root) of the set to which an element belongs, applying path compression for optimization.

# The union method merges two sets by attaching the set with lower rank to the one with higher rank, using union-by-rank to maintain balanced trees.

# The example usage code demonstrates how to create a disjoint-set, perform union operations, and find representatives of elements in the merged sets.

class DisjointSet:
    def __init__(self, size):
        # Initialize the disjoint-set data structure with 'size' sets.
        self.parent = list(range(size))
        self.rank = [0] * size  # Rank is used for union-by-rank optimization

    def find(self, element):
        # Find the representative (root) of the set to which 'element' belongs.
        if self.parent[element] != element:
            # Apply path compression by making the element's parent the representative.
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        # Union two sets to which 'element1' and 'element2' belong.
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            # Attach the set with lower rank to the one with higher rank (union-by-rank).
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                # If ranks are the same, choose one as the parent and increment its rank.
                self.parent[root2] = root1
                self.rank[root1] += 1


# Example usage:
if __name__ == "__main__":
    num_elements = 6
    disjoint_set = DisjointSet(num_elements)

    # Perform union operations to merge sets.
    disjoint_set.union(0, 1)
    disjoint_set.union(1, 2)
    disjoint_set.union(3, 4)
    disjoint_set.union(4, 5)

    # Find representatives of elements.
    # Should print 0 (representative of the merged set)
    print("Find representative of 2:", disjoint_set.find(2))
    # Should print 3 (representative of the merged set)
    print("Find representative of 3:", disjoint_set.find(3))
    # Should print 3 (representative of the merged set)
    print("Find representative of 5:", disjoint_set.find(5))
