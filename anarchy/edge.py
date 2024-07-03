"""
Edge will contain the node reference and any other pertinent information.
"""

import uuid
import weakref
from typing import TYPE_CHECKING, Dict, Optional, Union

if TYPE_CHECKING:
    from anarchy.node import AnarchyNode


class Edge:
    """
    An Edge is a connection between two nodes.

    A weakref is used to reference the node. This allows the node to be garbage
    collected when it is deleted, as well as any edges that reference it.

    Parameters
    ----------
    node : Node
        The node this edge is connected to.
    edge_type : str, optional
        The type of the edge. Defaults to "directed".
    edge_holder : AnarchyEdge, optional
        The edge dictionary this edge belongs to. Used to remove the edge
        from the dictionary when the node is deleted.

    Attributes
    ----------
    node_ref : weakref.ref
        A weakref to the node. Deleting the node will remove the edge.
    edge_type : str
        See parameter.
    node_id : int
        The node_id of the node this edge is connected to.
    edge_holder : AnarchyEdge
        See parameter.
    finalizer : weakref.finalizer
        A weakref finalizer that will remove the edge from the edge dictionary
        when the node is deleted.
    """

    def __init__(
        self,
        node: "AnarchyNode",
        edge_type: str = "directed",
        edge_holder: Optional["AnarchyEdge"] = None,
    ) -> None:
        self.node_ref = weakref.ref(node)
        self.edge_type = edge_type
        self.node_id = node.node_id
        self.edge_id = str(uuid.uuid4())
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
    def node(self) -> Optional["AnarchyNode"]:
        """
        Returns
        -------
        Node or None
            The node this edge is connected to.
        """
        return self.node_ref()

    def __repr__(self) -> str:
        return f"Edge(node: {self.node_id}, type: {self.edge_type})"


class AnarchyEdge(dict):
    """
    Dict-like object to store edges.

    Methods
    -------
    add(node: "AnarchyNode", edge_type: str = "directed") -> None
        Adds an edge to the node.
    remove(node_or_id: Union["AnarchyNode", int, str]) -> None
        Removes an edge from the node.
    edges() -> Dict[int, "AnarchyEdge"]
        Returns the edges of the node.

    TODO
    ----
    -  Access nodes by traversing edges (by [] or by method)
    """

    def __init__(self) -> None:
        super().__init__()

    def add(self, node: "AnarchyNode", edge_type: str = "directed") -> None:
        """
        Adds an edge to the node.

        Parameters
        ----------
        node : Node
            The node to connect to.
        edge_type : str, optional
            The type of the edge. Defaults to "directed".
        """

        if node.node_id not in self:
            edge = Edge(node, edge_type=edge_type, edge_holder=self)
            self[node.node_id] = edge
            if edge_type == "undirected":
                node.edges.add(node, edge_type="directed")

    def remove(self, node_or_id: Union["AnarchyNode", int, str]) -> None:
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
                edge.node.edges.remove(edge)
            del self[node_id]

    def edges(self) -> Dict[int, "AnarchyEdge"]:
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

    def __call__(self) -> Dict[int, "AnarchyEdge"]:
        return self.edges()
