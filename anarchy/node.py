"""
Node stores edges in a dictionary where the key is the other node's id and the 
value is the Edge object that has the reference to the node.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from anarchy.graph import AnarchyGraph

from anarchy.edge import AnarchyEdge
from anarchy.search import explore


class AnarchyNode:
    """
    A node is a self-contained and decentralized entity in a graph that stores
    its own data and edges.

    Parameters
    ----------
    node_id : int
        The unique identifier of the node.
    data : Any, optional
        The data to be stored in the node. Defaults to None.
    edges : AnarchyEdge, optional
        Dict-like object to store edges. Defaults to an empty AnarchyEdge and can be
        initialized with existing edges.

    Methods
    -------
    explore(strategy: str = "bfs") -> AnarchyGraph
        Explore the graph using a strategy. Defaults to "bfs".

    TODO
    ----
    - Improve the explore method
    """

    def __init__(
        self, node_id: int, data: Any = None, edges: AnarchyEdge = None
    ) -> None:
        self.node_id = node_id
        self.data = data
        self.edges = edges or AnarchyEdge()

    def explore(self, strategy: str = "bfs") -> "AnarchyGraph":
        """
        Explore the graph using a strategy.

        Returns a graph of the explored nodes.
        """
        from anarchy.graph import AnarchyGraph

        return AnarchyGraph.from_dict(explore(self, strategy=strategy))

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.
        """
        return (
            f"Node({self.node_id}, Data: {self.data}, Edges: {list(self.edges.keys())})"
        )

    def __eq__(self, other: "AnarchyNode") -> bool:
        return self.node_id == other.node_id

    def __hash__(self) -> int:
        return hash(self.node_id)

    def __ne__(self, other: "AnarchyNode") -> bool:
        return self.node_id != other.node_id
