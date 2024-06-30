import pyperf
from anarchy.edge import Edges
from anarchy.node import Node
from functools import partial

def create_nodes(n):
    """
    Function to create n nodes.
    """
    nodes = []
    for i in range(n):
        node = Node(node_id=i, data=f"data_{i}")
        nodes.append(node)
    return nodes

def create_and_connect_nodes(n):
    """
    Function to create n nodes and connect them in a chain.
    """
    nodes = create_nodes(n)
    for i, node in enumerate(nodes):
        if i < n-1:
            node.edges.add(nodes[i+1])
    return nodes

def search_nodes(n):
    """
    Function to search n nodes.
    """
    nodes = create_nodes(n)
    return nodes

def benchmark_create_nodes(loops, n):
    """
    Benchmark function for creating n nodes.
    """
    for _ in range(loops):
        create_nodes(n)

def benchmark_create_and_connect_nodes(loops, n):
    """
    Benchmark function for creating and connecting n nodes.
    """
    for _ in range(loops):
        create_and_connect_nodes(n)
        
def benchmark_search_nodes(loops, n):
    """
    Benchmark function for searching n nodes.
    """
    for _ in range(loops):
        search_nodes(n)

def main():
    runner = pyperf.Runner()

    # Parameters for the benchmarks
    n = 1000  # Number of nodes
    loops = 100

    # Use functools.partial to pass the additional parameter
    runner.bench_func('create_nodes', partial(benchmark_create_nodes, loops=loops, n=n))
    runner.bench_func('create_and_connect_nodes', partial(benchmark_create_and_connect_nodes, loops=loops, n=n))
    runner.bench_func('search_nodes', partial(benchmark_search_nodes, loops=loops, n=n))

if __name__ == "__main__":
    main()
