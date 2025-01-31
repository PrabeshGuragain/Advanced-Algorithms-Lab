from itertools import permutations

def travelling_salesman(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)
    
    min_path = float('inf')
    next_permutation = permutations(vertices)
    
    for perm in next_permutation:
        current_pathweight = 0
        
        k = start
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][start]
        
        min_path = min(min_path, current_pathweight)
        
    return min_path

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_vertex = 0
    print("Graph:", graph)
    print(f"Minimum cost of travelling salesman tour: {travelling_salesman(graph, start_vertex)}")