from typing import Dict

import pytest
from hypothesis import given
from hypothesis import strategies as st

from swarm.graph import Graph, RandomGraph
from swarm.node import Node


class TestGraph:
    @pytest.fixture
    def graph(self):
        return Graph()

    # Simple pytest tests
    def test_graph_initialization(self):
        g = Graph(5)
        assert len(g) == 5
        assert all(isinstance(node, Node) for node in g.values())

    def test_random_node(self):
        g = Graph(5)
        node = g.random()
        assert isinstance(node, Node)
        assert node in g.values()

    def test_to_dict(self):
        g = Graph(5)
        graph_dict = g.to_dict()
        assert isinstance(graph_dict, dict)
        assert "nodes" in graph_dict
        assert "edges" in graph_dict

    def test_to_json(self):
        g = Graph(5)
        graph_json = g.to_json()
        assert isinstance(graph_json, str)
        assert graph_json.startswith("{") and graph_json.endswith("}")

    # Property-based tests using hypothesis
    @given(st.integers(min_value=0, max_value=100))
    def test_graph_size(self, node_count):
        g = Graph(node_count)
        assert len(g) == node_count
