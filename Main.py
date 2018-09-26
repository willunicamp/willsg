import operator
from Graph import Graph

g = Graph()

g.load_from_file("edges")

cc = g.closeness_centrality()

sorted_cc = sorted(cc.items(), key=operator.itemgetter(1))

for node, closeness in sorted_cc:
    print("Node: {:s}, Closeness: {:f}".format(node, closeness))
