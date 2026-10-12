# Kruskal's Algorithm for Minimum Spanning Tree (MST)

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


def kruskal_mst(num_vertices, edges):
    # Sort edges based on weight
    edges.sort(key=lambda edge: edge[2])

    dsu = DisjointSet(num_vertices)
    mst = []
    total_cost = 0

    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_cost += w

    print("Edges in Minimum Spanning Tree:")
    print("Edge : Weight")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")

    print("\nTotal Cost of MST:", total_cost)


# Sample Graph (Vertices count and list of edges: u, v, weight)
num_vertices = 6
edges = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 3, 6),
    (2, 3, 8),
    (2, 4, 9),
    (3, 4, 9),
    (3, 5, 5),
    (4, 5, 7)
]

print("Minimum Spanning Tree using Kruskal's Algorithm:\n")
kruskal_mst(num_vertices, edges)
