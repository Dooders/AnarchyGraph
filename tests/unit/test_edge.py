import pytest
from hypothesis import given
from hypothesis import strategies as st

from anarchy.edge import AnarchyEdge, Edge
from anarchy.node import AnarchyNode


class TestEdges:
    @pytest.fixture
    def node1(self):
        return AnarchyNode(1)

    @pytest.fixture
    def node2(self):
        return AnarchyNode(2)

    @pytest.fixture
    def edges(self):
        return AnarchyEdge()

    def test_edge_initialization(self, node1):
        edge = Edge(node1, edge_type="undirected")
        assert edge.node_id == node1.node_id
        assert edge.edge_type == "undirected"
        assert edge.node == node1

    def test_edges_initialization(self, edges):
        assert isinstance(edges, dict)
        assert len(edges) == 0

    def test_edges_add(self, edges, node1):
        edges.add(node1)
        assert node1.node_id in edges
        assert isinstance(edges[node1.node_id], Edge)
        assert edges[node1.node_id].node == node1

    def test_edges_remove(self, edges, node1):
        edges.add(node1)
        edges.remove(node1)
        assert node1.node_id not in edges

    @given(st.integers(), st.text())
    def test_edge_weakref(self, node_id, edge_type):
        node = AnarchyNode(node_id)
        edges = AnarchyEdge()
        edge = Edge(node, edge_type=edge_type, edge_holder=edges)
        assert edge.node == node
        del node
        assert edge.node is None

    @given(st.integers(), st.text())
    def test_edges_add_and_remove(self, node_id, edge_type):
        node = AnarchyNode(node_id)
        edges = AnarchyEdge()
        edges.add(node, edge_type=edge_type)
        assert node.node_id in edges
        edges.remove(node_id)
        assert node.node_id not in edges

    def test_edges_repr(self, edges, node1):
        edges.add(node1, edge_type="undirected")
        assert (
            repr(edges[node1.node_id])
            == f"Edge(node: {node1.node_id}, type: undirected)"
        )
