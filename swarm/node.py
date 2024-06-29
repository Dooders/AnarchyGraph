"""
Node stores edges in a dictionary where the key is the other node's id and the 
value is the Edge object that has the reference to the node.

Node does not store the graph it belongs to??? Will it need it? Can it somehow 
reference a parent from itself?

Node doesn't know what edges comes from another node into it?

TODO:
- Edge container to make it a node component. Allows for node to have specialty edges
"""

from typing import Any

from swarm.edge import Edge


class Node:
    """
    A node is a self-contained and decentralized entity in a graph that stores
    it's own data and edges.

    Parameters
    ----------
    node_id : int
        The unique identifier of the node.
    data : Any, optional
        The data to be stored in the node. Defaults to None.

    Methods
    -------
    add_edge(node: Node) -> None:
        Adds an edge to the node.
    remove_edge(node: Node) -> None:
        Removes an edge from the node.
    get_edges(self) -> dict:
        Returns the edges of the node.

    TODO
    ----
    - Allow multiple edges between nodes, and a way to manage them
    """

    def __init__(self, node_id: int, data: Any = None) -> None:
        self.node_id = node_id
        self.data = data
        self._edges = {}

    def add_edge(self, node: "Node", edge_type: str = "undirected") -> None:
        """
        Adds an edge to the node.

        Parameters
        ----------
        other_node : Node
            The node to connect to.
        edge_type : str, optional
            The type of the edge. Defaults to "undirected".
        weight : int, optional
            The weight of the edge. Defaults to 1.
        """
        if node.node_id not in self._edges:
            self._edges[node.node_id] = Edge(node, edge_type=edge_type)
            if edge_type == "directed":
                node.add_edge(self, edge_type="directed")

    def remove_edge(self, node: "Node") -> None:
        """
        Removes an edge from the node.

        Parameters
        ----------
        other_node : Node
            The node to disconnect from.
        """
        if node.node_id in self._edges:
            edge = self._edges[node.node_id]
            if edge.edge_type == "directed":
                node.remove_edge(self)
            del self._edges[node.node_id]

    def edges(self) -> dict:
        """
        Returns the edges of the node.

        Returns
        -------
        dict
            The edges of the node.
        """
        return self._edges

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.

        Returns
        -------
        str
            A string representation of the node.
        """
        return f"Node({self.node_id}, Data: {self.data}, Edges: {list(self._edges.keys())})"

    def __eq__(self, other: "Node") -> bool:
        return self.node_id == other.node_id

    def __hash__(self) -> int:
        return hash(self.node_id)

    def __ne__(self, other: "Node") -> bool:
        return self.node_id != other.node_id
