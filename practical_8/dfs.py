# Depth First Search (DFS) Implementation

def dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Sample Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal starting from node 'A':")
dfs(graph, 'A')
print()
