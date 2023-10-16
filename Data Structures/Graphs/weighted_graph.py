class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph.
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        # Add an edge between 'vertex1' and 'vertex2' with the given 'weight'.
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight  # For an undirected graph

    def get_vertices(self):
        # Get a list of all vertices in the graph.
        return list(self.graph.keys())

    def get_edges(self):
        # Get a list of all edges in the graph as tuples (vertex1, vertex2, weight).
        edges = []
        for vertex1, neighbors in self.graph.items():
            for vertex2, weight in neighbors.items():
                if (vertex1, vertex2, weight) not in edges and (vertex2, vertex1, weight) not in edges:
                    edges.append((vertex1, vertex2, weight))
        return edges

    def visualize(self):
        # Visualize the graph as an adjacency list with weights.
        for vertex, neighbors in self.graph.items():
            neighbor_str = ", ".join(
                [f"{neighbor} ({weight})" for neighbor, weight in neighbors.items()])
            print(f"{vertex} -> {neighbor_str}")


# Example usage:
if __name__ == "__main__":
    graph = WeightedGraph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Add weighted edges
    graph.add_edge("A", "B", 2)
    graph.add_edge("B", "C", 3)
    graph.add_edge("C", "A", 1)
    graph.add_edge("D", "A", 4)

    # Get vertices and edges
    vertices = graph.get_vertices()
    edges = graph.get_edges()

    # Print the graph
    print("Vertices:", vertices)
    print("Edges:", edges)
    print("Graph:")
    graph.visualize()
