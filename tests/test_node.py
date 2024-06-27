import pytest

from swarm.node import Node


def test_node():
    node = Node(1)
    assert node.node_id == 1
    assert node.data is None
    assert node.edges() == {}


def test_node_add_edge():
    node1 = Node(1)
    node2 = Node(2)
    node1.add_edge(node2)
    assert node1.edges() == {2: node2}


def test_node_remove_edge():
    node1 = Node(1)
    node2 = Node(2)
    node1.add_edge(node2)
    node1.remove_edge(node2)
    assert node1.edges() == {}


def test_node_repr():
    node1 = Node(1)
    assert str(node1) == "Node(1, Data: None, Edges: [])"
