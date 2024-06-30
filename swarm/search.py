"""
Since this is a decentralized graph approach, there are different considerations 
and results from common graph search algorithms.

If the graph is directed, the completeness of the returning subgraph does not 
consider incoming edges into a node, only edges originating from a node.

It's possible to work around this limitation by storing the state of the graph 
and performing a search from a holistic level

TODO
----
- random walk algorithm
- a* algorithm
- dijkstra algorithm
"""

import heapq
from collections import deque
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from swarm.node import Node


def ping(entry_node: "Node", strategy: str = "bfs") -> dict:
    """
    Function to search through a decentralized graph through an entry point.

    By selected strategy until all connected nodes have been reached.

    Like node count, IDs, etc (state)

    TODO
    ----
    - Add max hops
    - Add max depth
    - Different return data like just the count, the structure, subgraph,
        or the nodes themselves
    """
    if strategy == "bfs":
        return bfs(entry_node)
    elif strategy == "dfs":
        return dfs(entry_node)
    else:
        raise ValueError("Invalid strategy")


def bfs(entry_node):
    """
    Breadth-first search through an entry point node.
    Returns the structure of the subgraph headed by the entry node.

    BFS explores all neighbors of a node before moving to the next level of nodes.
    Each node maintains a queue of neighbors to visit.

    #! Working
    """
    graph_structure = {entry_node.node_id: {}}
    visited = set(
        [entry_node.node_id]
    )  # Initialize the visited set with the entry node
    queue = deque([(entry_node, graph_structure[entry_node.node_id])])

    while queue:
        current_node, current_structure = queue.popleft()

        for edge in current_node.edges.values():
            neighbor = edge.node  # Access the node connected by the edge
            if neighbor.node_id not in visited:
                visited.add(neighbor.node_id)
                current_structure[neighbor.node_id] = {}
                queue.append((neighbor, current_structure[neighbor.node_id]))

    return graph_structure


def dfs(entry_node: "Node") -> dict:
    """
    Depth-first search through an entry point node.
    Returns the structure of the subgraph headed by the entry node.

    DFS explores as far as possible along a branch before backtracking.

    #! Working
    """
    graph_structure = {entry_node.node_id: {}}
    visited = set()

    def dfs_helper(current_node, current_structure):
        visited.add(current_node.node_id)

        for edge in current_node.edges.values():
            neighbor = edge.node  # Access the node connected by the edge
            if neighbor.node_id not in visited:
                current_structure[neighbor.node_id] = {}
                dfs_helper(neighbor, current_structure[neighbor.node_id])

    dfs_helper(entry_node, graph_structure[entry_node.node_id])

    return graph_structure


def dijkstra(start_node: "Node") -> dict:
    """
    Dijkstra's algorithm through an entry point node.
    Returns the shortest path to all connected nodes.

    Dijkstra's algorithm is a greedy algorithm in graph theory that finds the
    shortest path between two nodes. It uses a priority queue to select the
    node with the lowest distance from the start node.

    TODO
    ----
    - Work out a way to get weighted edges

    #! Not Working
    """
    distances = {start_node: 0}
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances.get(current_node, float("inf")):
            continue

        for neighbor, weight in current_node.get_neighbors_with_weights():
            distance = current_distance + weight
            if distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def a_star(start_node: "Node", goal_node: "Node", heuristic: Callable) -> list["Node"]:
    """
    A* algorithm through an entry point node.
    Returns the shortest path to all connected nodes.

    A* is a heuristic search algorithm that uses a priority queue to select the
    node with the lowest cost from the start node.

    #! Not Working
    """
    open_set = [(0, start_node)]
    g_score = {start_node: 0}
    f_score = {start_node: heuristic(start_node, goal_node)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal_node:
            return reconstruct_path(current)

        for neighbor, weight in current.get_neighbors_with_weights():
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal_node)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


def reconstruct_path(node: "Node") -> list["Node"]:
    """
    Reconstruct the path from the goal node to the start node.

    TODO
    ----
    - Resolve bug, node has no parent attribute. Need a way to keep track of the
        parent node.
    """
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    return path


def random_walk(start_node: "Node", steps: int) -> list["Node"]:
    """
    Random walk through an entry point node.
    Returns the path taken to all connected nodes.

    Random walk is a random search algorithm that explores the graph by
    randomly selecting a neighbor node.
    """
    pass
