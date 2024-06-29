"""
Edge will contain the node reference and any other pertinent information.
"""

import weakref
from typing import TYPE_CHECKING, Dict, Optional, Union

if TYPE_CHECKING:
    from swarm.node import Node


class Edge:
    """
    An Edge is a connection between two nodes.

    A weakref is used to reference the node. This allows the node to be garbage collected
    when it is deleted, as well as any edges that reference it.

    Parameters
    ----------
    node : Node
        The node this edge is connected to.
    edge_type : str, optional
        The type of the edge. Defaults to "directed".
    edge_holder : Edges, optional
        The edge dictionary this edge belongs to. Used to remove the edge
        from the dictionary when the node is deleted.

    Attributes
    ----------
    node : Node
        See parameter.
    edge_type : str
        See parameter.
    node_id : int
        The node_id of the node this edge is connected to.
    edge_holder :
        See parameter.
    finalizer : weakref.finalizer
        A weakref finalizer that will remove the edge from the edge dictionary
        when the node is deleted.
    """

    def __init__(
        self,
        node: "Node",
        edge_type: str = "directed",
        edge_holder: Optional["Edges"] = None,
    ) -> None:
        self.node_ref = weakref.ref(node)
        self.edge_type = edge_type
        self.node_id = node.node_id
        self.edge_holder = edge_holder
        if edge_holder is not None:
            self.finalizer = weakref.finalize(node, self._remove_edge)

    def _remove_edge(self) -> None:
        """
        Removes the edge from the edge collection when the node is deleted.
        """
        if self.edge_holder is not None:
            self.edge_holder.remove(self.node_id)

    @property
    def node(self) -> Optional["Node"]:
        """
        Returns
        -------
        Node or None
            The node this edge is connected to.
        """
        return self.node_ref()

    def __repr__(self) -> str:
        return f"Edge(node: {self.node_id}, type: {self.edge_type})"


class Edges(dict):
    """
    Dict-like object to store edges.

    TODO
    ----
    -  Access nodes by traversing edges (by [] or by method)
    """

    def __init__(self) -> None:
        super().__init__()

    def add(self, node: "Node", edge_type: str = "undirected") -> None:
        """
        Adds an edge to the node.

        Parameters
        ----------
        node : Node
            The node to connect to.
        edge_type : str, optional
            The type of the edge. Defaults to "undirected".
        """
        if node.node_id not in self:
            edge = Edge(node, edge_type=edge_type, edge_holder=self)
            self[node.node_id] = edge
            if edge_type == "directed":
                node.edges.add(self, edge_type="directed")

    def remove(self, node_or_id: Union["Node", int, str]) -> None:
        """
        Removes an edge from the node.

        Parameters
        ----------
        node_or_id : Union[Node, int, str]
            The node or node_id to disconnect from.
        """
        if isinstance(node_or_id, (int, str)):
            node_id = node_or_id
        else:
            node_id = node_or_id.node_id

        if node_id in self:
            edge = self[node_id]
            if edge.edge_type == "directed" and edge.node is not None:
                edge.node.remove_edge(self)
            del self[node_id]

    def edges(self) -> Dict[int, "Edge"]:
        """
        Returns the edges of the node.

        Returns
        -------
        dict
            The edges of the node.
        """
        return {
            node_id: edge for node_id, edge in self.items() if edge.node is not None
        }

    def __call__(self) -> Dict[int, "Edge"]:
        return self.edges()
