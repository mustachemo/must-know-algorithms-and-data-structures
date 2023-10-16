class CyclicGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)

    def topological_sort(self):
        # Perform a topological sort using depth-first search (DFS).
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)

            stack.append(node)

        for vertex in self.graph:
            if vertex not in visited:
                dfs(vertex)

        return stack[::-1]

    def is_cyclic(self):
        # Check if the directed graph has a cycle.
        topological_order = self.topological_sort()

        # If the topological order is not the same as the graph's vertices, there is a cycle.
        return topological_order != list(self.graph.keys())

    def visualize(self):
        # Visualize the graph as an adjacency list.
        for vertex, neighbors in self.graph.items():
            neighbor_str = ", ".join(neighbors)
            print(f"{vertex} -> {neighbor_str}")


# Example usage:
if __name__ == "__main__":
    graph = CyclicGraph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    graph.add_edge("D", "A")

    print("Graph:")
    graph.visualize()

    if graph.is_cyclic():
        print("The graph has a cycle.")
    else:
        print("The graph is acyclic.")
