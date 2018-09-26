# Will's simple graph

This code allow someone to create a simple graph and calculates its closeness centrality. It uses the Floyd-Warshall algorithm to calculate the shortest distance from each node to all the other nodes, needed to find the closeness centrality.

The Graph.py file has the class responsible to deal with the graph and calculate its properties. It is possible to add nodes and edges, calculate the shortest distance and the closeness centrality. The class also has a method to load the edges from a file. Each line of the file consists of two vertex names separated by a single space, representing an edge between those two nodes. An example can be found on the file named edges.

The graph does not accept self loops, repeated edges or weighted edges. The closeness centrality does not work for weakly connected graphs.

## Examples

The Main.py file is an example that creates a graph object, load the edges from the file and show the closeness centrality from all the nodes, sorted by closeness value in ascending order.

The REST.py file creates a RESTful local server on port 4242. Two resources are available in this server to get the graph closeness centrality and to add new edges to the graph, respectively on the following routes:
- [http://127.0.0.1:4242/closeness](http://127.0.0.1:4242/closeness) - returns the closeness dictionary, sorted by the closeness value.
- [http://127.0.0.1:4242/addedge/\<node1\>/<node2\>](http://127.0.0.1:4242/addedge/\<node1\>/<node2\>), where \<node1\> and \<node2\> should be the names of each node.

## How to run
- Main file:
	- python Main.py
- RESTful server
	- python REST.py

## Requirements
- Python 3.x
- Python Flask libraries for the RESTful server:
	- python-flask
	- python-flask-restful 
