import heapq

def prims_algorithm(graph):
    start_node = list(graph.keys())[0]
    visited = set()
    min_heap = [(0, start_node)]
    mst_cost = 0
    mst_edges = []

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_cost += cost
            if cost != 0:
                mst_edges.append((cost, node))

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    return mst_cost, mst_edges

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 6},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 6, 'C': 5}
}

mst_cost, mst_edges = prims_algorithm(graph)
print("Minimum Spanning Tree cost:", mst_cost)
print("Edges in the Minimum Spanning Tree:", mst_edges)