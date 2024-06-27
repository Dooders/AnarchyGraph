"""
Edge will contain the node reference and any other pertinent information.

Need to make a way for a node to have many different edge types, and an easy 
way to manage them
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from swarm.node import Node


class Edge:
    def __init__(self, node: "Node") -> None:
        """
        Parameters
        ----------
        node : Node
            The node to connect to.
        """
        self.node = node
        self.node_id = node.node_id

    def __repr__(self) -> str:
        """
        Returns
        -------
        str
            A string representation of the edge.
        """
        return f"Edge(node: {self.node.node_id})"
