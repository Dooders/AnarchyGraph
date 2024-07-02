"""
Node stores edges in a dictionary where the key is the other node's id and the 
value is the Edge object that has the reference to the node.

TODO:
- Edge container to make it a node component. Allows for node to have specialty edges
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from anarchy.graph import Graph

from anarchy.edge import Edges
from anarchy.search import explore


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

    Methods
    -------
    explore(strategy: str = "bfs") -> Graph
        Explore the graph using a strategy. Defaults to "bfs".
    """

    def __init__(self, node_id: int, data: Any = None, edges: Edges = None) -> None:
        self.node_id = node_id
        self.data = data
        self.edges = edges or Edges()

    def explore(self, strategy: str = "bfs") -> "Graph":
        """
        Explore the graph using a strategy.

        Returns a graph of the explored nodes.
        """
        from anarchy.graph import Graph

        return Graph.from_dict(explore(self, strategy=strategy))

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
