from itertools import combinations

def is_clique(graph, vertices):
    for u, v in combinations(vertices, 2):
        if v not in graph[u]:
            return False
    return True

def find_cliques(graph, k):
    nodes = list(graph.keys())
    for vertices in combinations(nodes, k):
        if is_clique(graph, vertices):
            yield vertices

# Example usage
if __name__ == "__main__":
    graph = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
    k = 3
    cliques = list(find_cliques(graph, k))
    print("Graph:", graph)
    print(f"Cliques of size {k}: {cliques}")