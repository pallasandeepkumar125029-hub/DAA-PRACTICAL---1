# Prim's Algorithm for Minimum Spanning Tree (MST)

def prims_mst(graph, num_vertices):
    INF = 9999999
    selected = [False] * num_vertices
    selected[0] = True  # Start from vertex 0

    no_edge = 0
    total_cost = 0

    print("Edge : Weight")
    while no_edge < num_vertices - 1:
        minimum = INF
        x = 0
        y = 0

        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        total_cost += graph[x][y]
        selected[y] = True
        no_edge += 1

    print("\nTotal Cost of MST:", total_cost)

# Sample Graph (Adjacency Matrix)
graph = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

num_vertices = 5
print("Minimum Spanning Tree using Prim's Algorithm:\n")
prims_mst(graph, num_vertices)
