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
    

#Used ChatGPT for help with code
