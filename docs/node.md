# Node

Node stores edges in a dictionary where the key is the other node's id and the 
value is the Edge object that has the reference to the node.

Node does not store the graph it belongs to??? Will it need it? Can it somehow 
reference a parent from itself?

Node doesn't know what edges comes from another node into it?

A Node is autonomous if it can operate and interact independently of other nodes.

In NodeSwarm, a Node contains everything it needs to fulfill its goals for it's self.

Keeping the node homogeneous and self-contained gives each node the freedom to operate independently of other nodes.

This is a key to the autonomous and self-organizing nature of a swarm.

Self-organizing means that the nodes in a swarm are able to self-sustain and self-organize without the need for centralized control.

A node is simple when it does the most it can, as efficiently as possible.

Efficiently as possible means that the code and design of the node must be optimized to operate quickly and  be simple and straightforward.

Simplicity allows for easier understanding of any operational complexity a graph may contain.
Optimization means it does that in the least amount of time with the least amount of work (effort, energy, etc.)

The container may be simple, but the contents can be complex.

A node is it's self when it contains all the things it needs to operate independently
of other nodes.

Operating independently of other nodes means that each node is completely unique to other nodes.

This allows for a node to be as simple as possible while still being able to operate independently.

It can have its own state, it's own data, it's own functionality, it's own rules, it's own behavior

Nodes and components. Nodes are the container and the components interact with each other. towards a goal or set of rules.


## Node Summary

A **Node** in the context of the NodeSwarm framework is a self-contained entity designed for autonomous operation and interaction within a decentralized system. Here are the key characteristics and principles:

1. **Edge Storage**: Each Node stores its edges in a dictionary where the key is the ID of the connected node, and the value is an Edge object referencing the node.

2. **Graph Independence**: A Node does not store a reference to the graph it belongs to. It operates independently and does not inherently need to know about the overall graph structure. However, it may need mechanisms to reference a parent or higher structure if necessary.

3. **Edge Awareness**: A Node is unaware of incoming edges from other nodes. It only manages its own outgoing edges.

4. **Autonomy**: 
   - A Node is autonomous, capable of operating and interacting without dependency on other nodes.
   - Each Node in NodeSwarm contains everything it needs to fulfill its goals, ensuring it is self-sufficient and independent.

5. **Homogeneity and Self-Containment**: 
   - Keeping nodes homogeneous and self-contained enables them to operate independently.
   - This autonomy and self-organization are crucial for the swarm's decentralized nature.

6. **Self-Organization**: Nodes in a swarm are designed to self-sustain and self-organize without centralized control, promoting a robust and flexible system.

7. **Simplicity and Efficiency**:
   - A Node is simple when it performs its functions as efficiently as possible.
   - Simplicity in design allows for easier understanding and management of complex operations within the graph.
   - Efficiency means optimizing the Node's operation to minimize time and resource usage.

8. **Container and Components**:
   - A Node acts as a container for various components that interact according to predefined rules or goals.
   - While the Node itself may be simple, the components it contains can be complex, allowing for sophisticated behaviors and interactions.

9. **Self-Containment**:
   - A Node is self-sufficient, containing its state, data, functionality, rules, and behaviors.
   - This self-sufficiency ensures each Node is unique and operates independently from others, fostering a diverse and dynamic system.

By adhering to these principles, Nodes in the NodeSwarm framework can achieve high levels of autonomy, efficiency, and adaptability, supporting the overall goals of a decentralized and self-organizing system.