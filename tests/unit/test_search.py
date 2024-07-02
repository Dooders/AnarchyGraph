import pytest
from hypothesis import given
from hypothesis import strategies as st

from anarchy.node import Node
from anarchy.search import bfs, dfs


# Helper function to create a graph from a dictionary
def create_graph(graph_dict):
    nodes = {node_id: Node(node_id) for node_id in graph_dict}
    for node_id, edges in graph_dict.items():
        for edge_id in edges:
            nodes[node_id].edges.add(nodes[edge_id])
    return nodes


# Sample graph for deterministic testing
sample_graph = {1: [2, 3], 2: [4], 3: [], 4: []}


# Test BFS with a sample graph
def test_bfs_sample_graph():
    nodes = create_graph(sample_graph)
    result = bfs(nodes[1])
    assert result == {1: {2: {4: {}}, 3: {}}}


# Test DFS with a sample graph
def test_dfs_sample_graph():
    nodes = create_graph(sample_graph)
    result = dfs(nodes[1])
    assert result == {1: {2: {4: {}}, 3: {}}}


# Hypothesis test for BFS and DFS with random graphs
@st.composite
def random_graph(draw):
    node_ids = draw(
        st.lists(st.integers(min_value=0, max_value=100), min_size=1, unique=True)
    )
    edges = draw(
        st.lists(
            st.tuples(st.sampled_from(node_ids), st.sampled_from(node_ids)), min_size=1
        )
    )
    graph_dict = {node_id: [] for node_id in node_ids}
    for src, dst in edges:
        graph_dict[src].append(dst)
    return graph_dict


@given(random_graph())
def test_bfs_hypothesis(graph_dict):
    nodes = create_graph(graph_dict)
    entry_node_id = list(graph_dict.keys())[0]
    result = bfs(nodes[entry_node_id])
    # No specific assertions, just ensuring it doesn't raise errors


@given(random_graph())
def test_dfs_hypothesis(graph_dict):
    nodes = create_graph(graph_dict)
    entry_node_id = list(graph_dict.keys())[0]
    result = dfs(nodes[entry_node_id])
    # No specific assertions, just ensuring it doesn't raise errors
