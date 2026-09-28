# Breadth First Search (BFS) Implementation

def bfs(graph, start_node):
    visited = []
    queue = [start_node]
    visited.append(start_node)

    while queue:
        # Pop the first element from queue (FIFO)
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Sample Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal starting from node 'A':")
bfs(graph, 'A')
print()
