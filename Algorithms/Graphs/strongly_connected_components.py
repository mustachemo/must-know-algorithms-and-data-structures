from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add a directed edge to the graph.
        self.graph[u].append(v)

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(vertex)

    def transpose(self):
        transposed_graph = Graph()
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def kosaraju_scc(self):
        stack = []
        visited = {vertex: False for vertex in self.graph}

        # Step 1: Perform DFS on the original graph to fill the stack
        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)

        # Step 2: Transpose the graph
        transposed_graph = self.transpose()

        # Reset visited dictionary for the second DFS
        visited = {vertex: False for vertex in self.graph}

        # Step 3: Perform DFS on the transposed graph to find SCCs
        sccs = []
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                scc = []
                transposed_graph.dfs(vertex, visited, scc)
                sccs.append(scc)

        return sccs


# Example usage:
if __name__ == "__main__":
    g = Graph()

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 3)
    g.add_edge(6, 5)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 6)

    sccs = g.kosaraju_scc()

    print("Strongly Connected Components:")
    for scc in sccs:
        print(scc)
