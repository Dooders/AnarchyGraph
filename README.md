![AnarchyGraph Logo](docs/img/anarchy_graph_logo.png)

![Project Status](https://img.shields.io/badge/status-in%20development-orange)

# Rules of AnarchyGraph

1. Be [**independent**](docs/independent.md)
2. Be [**simple**](docs/simple.md)
3. Be [**optimized**](docs/optimized.md)

# Installation

```bash
pip install anarchygraph
```

# Usage

## Adding Edges

```python
from anarchy import AnarchyNode

node1 = AnarchyNode(1)
node2 = AnarchyNode(2)
node3 = AnarchyNode(3)

# Add edges to Node1
node1.edges.add(node2.node_id, node2)
node1.edges.add(node3.node_id, node3)

print(node1.edges())
```

## Random Graph

```python
from anarchy.graph import RandomGraph

g = RandomGraph()

g.edges()
```
