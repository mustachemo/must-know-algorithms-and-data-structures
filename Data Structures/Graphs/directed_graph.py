class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for from_vertex, to_vertices in self.graph.items():
            for to_vertex in to_vertices:
                edges.append((from_vertex, to_vertex))
        return edges

    def visualize(self):
        # Visualize the graph as an adjacency list.
        for vertex, neighbors in self.graph.items():
            neighbor_str = ", ".join(neighbors)
            print(f"{vertex} -> {neighbor_str}")


# Example usage:
if __name__ == "__main__":
    graph = DirectedGraph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    graph.add_edge("D", "A")

    vertices = graph.get_vertices()
    edges = graph.get_edges()

    print("Vertices:", vertices)
    print("Edges:", edges)
    print("Graph:")
    graph.visualize()
