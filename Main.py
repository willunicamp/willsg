from Graph import Graph

g = Graph()

g.load_from_file("edges")

print(g.closeness_centrality('74'))


