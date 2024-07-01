import pyperf
from anarchy.edge import Edges
from anarchy.node import Node
from functools import partial
from memory_profiler import memory_usage

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

def memory_benchmark(func, *args):
    """
    Function to benchmark memory usage.
    """
    mem_usage = memory_usage((func, args), interval=0.1)
    return max(mem_usage) - min(mem_usage)


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

    # Use functools.partial to pass the additional parameter
    create_nodes_partial = partial(benchmark_create_nodes, n=n)
    create_and_connect_nodes_partial = partial(benchmark_create_and_connect_nodes, n=n)

    # Add benchmarks
    runner.bench_func('create_nodes', create_nodes_partial)
    runner.bench_func('create_and_connect_nodes', create_and_connect_nodes_partial)

    # Memory benchmarks
    create_nodes_memory = memory_benchmark(benchmark_create_nodes, 1, n)
    create_and_connect_nodes_memory = memory_benchmark(benchmark_create_and_connect_nodes, 1, n)

    print(f"Memory usage for creating {n} nodes: {create_nodes_memory} MiB")
    print(f"Memory usage for creating and connecting {n} nodes: {create_and_connect_nodes_memory} MiB")


if __name__ == "__main__":
    main()
