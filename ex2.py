'''
1. Ways to Implement Queue for Dijkstra's Algorithm:

a. Slow Implementation with Linear Search:

In this implementation, you can use a simple list to represent the queue, where you append new nodes to the end and remove nodes from the beginning when selecting the next node to explore. 
However, when selecting the node with the minimum distance, you would iterate through the entire list to find the node with the minimum distance. This approach has a time complexity of O(n) for each node selection, 
making it inefficient as the number of nodes increases.

b. Faster Implementation using Priority Queue:

Instead of using a simple list, you can utilize a priority queue (e.g., heapq in Python) to implement a more efficient version. With a priority queue, you can maintain the nodes in the queue ordered by their distances, 
allowing you to efficiently select the node with the minimum distance in O(log n) time. This approach significantly improves the efficiency of the algorithm.
'''

# 2. Implementation of Dijkstra's Algorithm:

import time
import matplotlib.pyplot as plt
from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))


def slowSP(graph, start):
    # Initialize distances and visited dictionary
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph.graph):
        # Find the node with the minimum distance (inefficient)
        min_distance = float('inf')
        min_node = None
        for node in graph.graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        # Add the selected node to visited set
        visited.add(min_node)

        # Update distances for adjacent nodes
        for neighbor, weight in graph.graph[min_node]:
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


def fastSP(graph, start):
    # Initialize distances and visited dictionary
    distances = {node: float('inf') for node in graph.graph}
    distances[start] = 0
    visited = set()

    # Initialize priority queue with start node
    pq = [(0, start)]

    while pq:
        # Extract the node with the minimum distance
        min_distance, min_node = heapq.heappop(pq)

        # If already visited, skip
        if min_node in visited:
            continue

        # Add the selected node to visited set
        visited.add(min_node)

        # Update distances for adjacent nodes
        for neighbor, weight in graph.graph[min_node]:
            new_distance = distances[min_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances

# 3.


# Function to measure performance


def measure_performance(graph, start_node):
    slow_times = []
    fast_times = []

    for node in graph.graph:
        start_time = time.time()
        slowSP(graph, start_node)
        slow_times.append(time.time() - start_time)

        start_time = time.time()
        fastSP(graph, start_node)
        fast_times.append(time.time() - start_time)

    # Calculate statistics
    slow_avg_time = sum(slow_times) / len(slow_times)
    slow_max_time = max(slow_times)
    slow_min_time = min(slow_times)

    fast_avg_time = sum(fast_times) / len(fast_times)
    fast_max_time = max(fast_times)
    fast_min_time = min(fast_times)

    return slow_times, fast_times, slow_avg_time, slow_max_time, slow_min_time, fast_avg_time, fast_max_time, fast_min_time

# Main function


def main():
    # Load graph from file (random.dot)
    # graph = load_graph_from_file('random.dot')

    # Measure performance
    slow_times, fast_times, slow_avg_time, slow_max_time, slow_min_time, fast_avg_time, fast_max_time, fast_min_time = measure_performance(
        graph, start_node)

    # Report performance statistics
    print("Slow Algorithm:")
    print("Average Time:", slow_avg_time)
    print("Maximum Time:", slow_max_time)
    print("Minimum Time:", slow_min_time)
    print("\nFast Algorithm:")
    print("Average Time:", fast_avg_time)
    print("Maximum Time:", fast_max_time)
    print("Minimum Time:", fast_min_time)


if __name__ == "__main__":
    main()

# 4.


# Plot histogram

def plot_histogram(slow_times, fast_times):
    plt.hist(slow_times, bins=20, alpha=0.5, label='Slow Algorithm')
    plt.hist(fast_times, bins=20, alpha=0.5, label='Fast Algorithm')
    plt.xlabel('Execution Time (s)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Execution Times')
    plt.legend()
    plt.show()

# Main function


def main():
    # Load graph from file (random.dot)
    # graph = load_graph_from_file('random.dot')

    # Assuming the graph is loaded and the start node is defined

    # Measure performance
    slow_times, fast_times, _, _, _, _, _, _ = measure_performance(
        graph, start_node)

    # Plot histogram
    plot_histogram(slow_times, fast_times)


if __name__ == "__main__":
    main()

# Used ChatGPT for help with code
