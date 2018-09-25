from Graph import Graph

g = Graph()

g.load_from_file("edges")

print(g.all_shortest_path_length())
