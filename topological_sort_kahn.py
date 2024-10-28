from collections import deque

def topological_sort_kahn(graph):
    # Step 1: Calculate in-degrees
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Initialize the queue with nodes of in-degree 0
    queue = deque([u for u in in_degree if in_degree[u] == 0])

    # Step 3: List for the topological order
    topological_order = []

    # Step 4: Process the queue
    while queue:
        u = queue.popleft()
        topological_order.append(u)

        # Decrease the in-degree of neighbors
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Step 5: Check for cycles
    if len(topological_order) != len(graph):
        return None  # Cycle detected

    return topological_order

# Example usage
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': ['X', 'Y', 'Z'],
    "X": ["Z"],
    "Y": ["X", "Z"],
    "Z": []
}

print(topological_sort_kahn(graph))
