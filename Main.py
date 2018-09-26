#!/usr/bin/env python
__author__ = "William Roberto de Paiva"
__copyright__ = "Copyright 2018, Will's simple graph"
__credits__ = ["William Roberto de Paiva"]
__license__ = "MIT"
__maintainer__ = "William Roberto de Paiva"
__email__ = "will.unicamp@gmail.com"
__status__ = "Production"

import operator
from Graph import Graph

g = Graph()
#Load the graph from a file named 'edges'
g.load_from_file("edges")
#Calculate the closeness centrality to all vertices
cc = g.closeness_centrality()
#Sort the centrality resulting dict by closeness
sorted_cc = sorted(cc.items(), key=operator.itemgetter(1))

#Show the vertices and its centrality formatted
for node, closeness in sorted_cc:
    print("Node: {:s}, Closeness: {:f}".format(node, closeness))
