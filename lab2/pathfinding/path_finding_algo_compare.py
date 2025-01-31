import time
import networkx as nx

import matplotlib.pyplot as plt

def kruskal_algorithm(graph):
    return nx.minimum_spanning_tree(graph, algorithm='kruskal')

def prim_algorithm(graph):
    return nx.minimum_spanning_tree(graph, algorithm='prim')

def measure_time(graph, algorithm):
    start_time = time.time()
    algorithm(graph)
    end_time = time.time()
    return end_time - start_time

def generate_graph(num_nodes, num_edges):
    return nx.gnm_random_graph(num_nodes, num_edges)

def main():
    num_nodes_list = range(10, 101, 10)
    kruskal_times = []
    prim_times = []

    for num_nodes in num_nodes_list:
        graph = generate_graph(num_nodes, num_nodes * 2)  # Assuming a dense graph
        kruskal_times.append(measure_time(graph, kruskal_algorithm))
        prim_times.append(measure_time(graph, prim_algorithm))

    plt.plot(num_nodes_list, kruskal_times, label='Kruskal\'s Algorithm')
    plt.plot(num_nodes_list, prim_times, label='Prim\'s Algorithm')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (seconds)')
    plt.title('Kruskal\'s vs Prim\'s Algorithm Time Complexity')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()