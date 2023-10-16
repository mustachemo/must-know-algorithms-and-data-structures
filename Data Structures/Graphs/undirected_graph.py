class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        # Add a vertex to the graph.
        if vertex not in self.graph:
            self.graph[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        # Add an undirected edge between 'vertex1' and 'vertex2'.
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].add(vertex2)
            self.graph[vertex2].add(vertex1)

    def get_vertices(self):
        # Get a list of all vertices in the graph.
        return list(self.graph.keys())

    def get_edges(self):
        # Get a list of all undirected edges in the graph as tuples (vertex1, vertex2).
        edges = []
        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                if (vertex, neighbor) not in edges and (neighbor, vertex) not in edges:
                    edges.append((vertex, neighbor))
        return edges

    def visualize(self):
        # Visualize the graph as an adjacency list.
        for vertex, neighbors in self.graph.items():
            neighbor_str = ", ".join(neighbors)
            print(f"{vertex} -> {neighbor_str}")


# Example usage:
if __name__ == "__main__":
    graph = UndirectedGraph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Add undirected edges
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    graph.add_edge("D", "A")

    # Get vertices and edges
    vertices = graph.get_vertices()
    edges = graph.get_edges()

    # Print the graph
    print("Vertices:", vertices)
    print("Edges:", edges)
    print("Graph:")
    graph.visualize()
