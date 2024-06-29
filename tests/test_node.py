import pytest
from hypothesis import given
from hypothesis import strategies as st

from swarm.node import Node


@pytest.fixture
def node1():
    return Node(1)


@pytest.fixture
def node2():
    return Node(2)


def test_node_initialization(node1):
    # Test node initialization
    assert node1.node_id == 1
    assert node1.data is None
    assert node1.edges() == {}


def test_node_add_edge(node1, node2):
    # Test adding an edge
    node1.edges.add(node2)
    assert node1.edges() == {2: node2}
    # Ensure the added node has no edges unless specified
    assert node2.edges() == {}


def test_node_add_duplicate_edge(node1, node2):
    # Test adding the same edge twice
    node1.edges.add(node2)
    node1.edges.add(node2)
    assert node1.edges() == {2: node2}


def test_node_remove_edge(node1, node2):
    # Test removing an edge
    node1.edges.add(node2)
    node1.edges.remove(node2)
    assert node1.edges() == {}


def test_node_remove_nonexistent_edge(node1, node2):
    # Test removing an edge that doesn't exist
    node1.edges.remove(node2)
    assert node1.edges() == {}


def test_node_repr(node1):
    # Test string representation
    assert str(node1) == "Node(1, Data: None, Edges: [])"


@pytest.mark.parametrize(
    "node_id,expected_repr",
    [(1, "Node(1, Data: None, Edges: [])"), (2, "Node(2, Data: None, Edges: [])")],
)
def test_node_repr_parametrized(node_id, expected_repr):
    # Test string representation with parameterized inputs
    node = Node(node_id)
    assert str(node) == expected_repr


def test_node_set_data(node1):
    # Test setting data
    node1.data = "test_data"
    assert node1.data == "test_data"


@given(st.integers())
def test_node_initialization(node_id):
    node = Node(node_id)
    assert node.node_id == node_id
    assert node.data is None
    assert node.edges() == {}


@given(st.integers(), st.integers())
def test_node_add_edge(node_id1, node_id2):
    node1 = Node(node_id1)
    node2 = Node(node_id2)
    node1.edges.add(node2)
    assert node2 in node1.edges().values()


@given(st.integers(), st.integers())
def test_node_remove_edge(node_id1, node_id2):
    node1 = Node(node_id1)
    node2 = Node(node_id2)
    node1.edges.add(node2)
    node1.edges.remove(node2)
    assert node2 not in node1.edges().values()


@given(st.integers(), st.text())
def test_node_set_data(node_id, data):
    node = Node(node_id)
    node.data = data
    assert node.data == data


@given(st.integers())
def test_node_repr(node_id):
    node = Node(node_id)
    expected_repr = f"Node({node_id}, Data: None, Edges: [])"
    assert str(node) == expected_repr
