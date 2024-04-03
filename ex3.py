class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        self.parent[root1] = root2

    def same_component(self, vertex1, vertex2):
        return self.find(vertex1) == self.find(vertex2)


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))

    def mst(self):
        mst_graph = Graph(self.vertices)
        self.edges.sort(key=lambda x: x[2])  # Sort edges by weight
        uf = UnionFind(self.vertices)

        for edge in self.edges:
            start, end, weight = edge
            if not uf.same_component(start, end):
                mst_graph.add_edge(start, end, weight)
                uf.union(start, end)

        return mst_graph


# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 8)
graph.add_edge('B', 'C', 11)
graph.add_edge('B', 'D', 8)
graph.add_edge('C', 'E', 7)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 2)

mst_graph = graph.mst()
for edge in mst_graph.edges:
    print(edge)
