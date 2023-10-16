from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge to the graph.
        self.graph[u].append(v)

    def visualize(self):
        # Visualize the graph as an adjacency list.
        for vertex, neighbors in self.graph.items():
            neighbor_str = ", ".join(map(str, neighbors))
            print(f"{vertex} -> {neighbor_str}")

    def bfs(self, start):
        # Perform BFS starting from the given 'start' vertex.

        # Create a queue for BFS
        queue = []
        # Create a set to keep track of visited vertices
        visited = set()

        # Mark the start vertex as visited and enqueue it
        visited.add(start)
        queue.append(start)

        while queue:
            # Dequeue a vertex from the queue
            vertex = queue.pop(0)
            print(vertex, end=" ")  # Print the vertex

            # Get all adjacent vertices of the dequeued vertex.
            # If an adjacent vertex is not visited, mark it as visited and enqueue it.
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()

    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 0)
    g.add_edge(2, 4)
    g.add_edge(3, 3)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    g.add_edge(6, 5)
    g.add_edge(6, 7)

    print("Graph before BFS:")
    g.visualize()

    print("\nBreadth-First Traversal (starting from vertex 2):")
    g.bfs(2)
