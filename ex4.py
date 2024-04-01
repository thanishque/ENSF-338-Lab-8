import time

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = {}

class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        return node

    def removeNode(self, node):
        del self.nodes[node.data]
        for n in self.nodes.values():
            if node.data in n.neighbors:
                del n.neighbors[node.data]

    def addEdge(self, n1, n2, weight=1):
        if n1 not in self.nodes:
            self.addNode(n1)
        if n2 not in self.nodes:
            self.addNode(n2)
        self.nodes[n1].neighbors[n2] = weight
        self.nodes[n2].neighbors[n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n2 in self.nodes[n1].neighbors:
                del self.nodes[n1].neighbors[n2]
            if n1 in self.nodes[n2].neighbors:
                del self.nodes[n2].neighbors[n1]

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()

            # Check if the graph type is undirected
            if 'strict graph' not in lines[0]:
                return None

            for line in lines[1:]:
                if line.strip() and line.strip()[0] != '}':
                    nodes = line.strip().split('--')
                    n1 = nodes[0].strip()
                    n2 = nodes[1].split('[')[0].strip()
                    weight = 1
                    if 'weight' in line:
                        weight = int(line.split('[')[1].split('=')[1].split(']')[0].strip())
                    self.addEdge(n1, n2, weight)

        except FileNotFoundError:
            return None
        return None
    
class Graph2:
    def __init__(self):
        self.nodes = {}
        self.adj_matrix = {}

    def addNode(self, data):
        node = GraphNode(data)
        self.nodes[data] = node
        self.adj_matrix[data] = {}
        for n in self.adj_matrix:
            self.adj_matrix[n][data] = 0
        return node

    def removeNode(self, node):
        del self.nodes[node.data]
        del self.adj_matrix[node.data]
        for n in self.adj_matrix:
            if node.data in self.adj_matrix[n]:
                del self.adj_matrix[n][node.data]

    def addEdge(self, n1, n2, weight=1):
        if n1 not in self.nodes:
            self.addNode(n1)
        if n2 not in self.nodes:
            self.addNode(n2)
        self.adj_matrix[n1][n2] = weight
        self.adj_matrix[n2][n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.nodes and n2 in self.nodes:
            if n2 in self.adj_matrix[n1]:
                del self.adj_matrix[n1][n2]
            if n1 in self.adj_matrix[n2]:
                del self.adj_matrix[n2][n1]

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.adj_matrix[start]:
            if neighbor not in visited and self.adj_matrix[start][neighbor] != 0:
                self.dfs(neighbor, visited)
        return list(visited)

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()

            # Check if the graph type is undirected
            if 'strict graph' not in lines[0]:
                return None

            for line in lines[1:]:
                if line.strip() and line.strip()[0] != '}':
                    nodes = line.strip().split('--')
                    n1 = nodes[0].strip()
                    n2 = nodes[1].split('[')[0].strip()
                    weight = 1
                    if 'weight' in line:
                        weight = int(line.split('[')[1].split('=')[1].split(']')[0].strip())
                    self.addEdge(n1, n2, weight)

        except FileNotFoundError:
            return None
        return None


# Measure performance of DFS traversal
def measure_dfs_performance(graph):
    times = []
    for _ in range(10):
        start_time = time.time()
        graph.dfs(list(graph.nodes.keys())[0])
        end_time = time.time()
        times.append(end_time - start_time)
    return times

# Create graph from file
graph = Graph2()
graph.importFromFile("random.dot")

# Measure performance of DFS traversal on Graph2
graph2_times = measure_dfs_performance(graph)

# Output results
print("Graph2 DFS performance (in seconds):")
print("Maximum time:", max(graph2_times))
print("Minimum time:", min(graph2_times))
print("Average time:", sum(graph2_times) / len(graph2_times))


# The first way is faster for this particular graph as it has more vertices 
# than edges. The adjacency matrix would perform better in that case but since 
# it's the former adjaceny list outperforms it.

#Used ChatGPT for help with code
