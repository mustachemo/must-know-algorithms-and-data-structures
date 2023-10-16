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

    def dfs(self, start):
        # Perform DFS starting from the given 'start' vertex.
        visited = set()

        def dfs_recursive(node):
            # Mark the current node as visited and print it.
            visited.add(node)
            print(node, end=" ")

            # Recur for all the adjacent vertices that are not visited.
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)


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

    print("Graph before DFS:")
    g.visualize()

    print("Depth-First Traversal (starting from vertex 2):")
    g.dfs(2)
