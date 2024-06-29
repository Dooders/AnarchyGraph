"""
Edge will contain the node reference and any other pertinent information.

Need to make a way for a node to have many different edge types, and an easy 
way to manage them
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from swarm.node import Node


class Edge:
    """
    An Edge is a connection between two nodes.
    """

    def __init__(self, node: "Node", edge_type: str = "directed") -> None:
        self.node = node
        self.edge_type = edge_type
        self.node_id = node.node_id

    def __repr__(self) -> str:
        return f"Edge(node: {self.node.node_id})"
