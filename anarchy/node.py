"""
Node stores edges in a dictionary where the key is the other node's id and the 
value is the Edge object that has the reference to the node.

TODO:
- Edge container to make it a node component. Allows for node to have specialty edges
"""

from typing import Any

from anarchy.edge import Edges


class Node:
    """
    A node is a self-contained and decentralized entity in a graph that stores
    its own data and edges.

    Parameters
    ----------
    node_id : int
        The unique identifier of the node.
    data : Any, optional
        The data to be stored in the node. Defaults to None.
    edges : Edges, optional
        Dict-like object to store edges. Defaults to an empty Edges and can be
        initialized with existing edges.
    """

    def __init__(self, node_id: int, data: Any = None, edges: Edges = None) -> None:
        self.node_id = node_id
        self.data = data
        self.edges = edges or Edges()

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.
        """
        return (
            f"Node({self.node_id}, Data: {self.data}, Edges: {list(self.edges.keys())})"
        )

    def __eq__(self, other: "Node") -> bool:
        return self.node_id == other.node_id

    def __hash__(self) -> int:
        return hash(self.node_id)

    def __ne__(self, other: "Node") -> bool:
        return self.node_id != other.node_id
