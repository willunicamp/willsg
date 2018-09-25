import os

#This graph is a digraph
class Graph:
    def __init__(self):
        self.graph = None
        self.dist = None

    def load_from_file(self, file_path):
        self.graph = dict()
        if os.path.exists(file_path):
            f = open(file_path, "r")
            for line in f:
                edge = line.replace('\n','').split(' ')
                v1 = edge[0]
                v2 = edge[1]
                #check if nodes are already in the graph
                if v1 not in self.graph.keys():
                    self.graph[v1] = list()
                if v2 not in self.graph.keys():
                    self.graph[v2] = list();
                #add neighbor to the node, if not yet included
                if v2 not in self.graph[v1]:
                    self.graph[v1].append(v2)
                if v1 not in self.graph[v2]:
                    self.graph[v2].append(v1)

    def all_shortest_path_length(self):
        if self.graph is not None:
            dist = dict()
            for v1 in self.graph.keys():
                dist[v1] = dict()
                for v2 in self.graph.keys():
                    dist[v1][v2] = float("inf")
                    if v1 == v2:
                        dist[v1][v1] = 0.0
            for v, neighbors in self.graph.items():
                for n in neighbors:
                    dist[v][n] = 1.0
            for k in self.graph.keys():
                for i in self.graph.keys():
                    for j in self.graph.keys():
                        dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
        else:
            dist = None
        return dist

    def closeness_centrality(self, node):
        self.dist = self.all_shortest_path_length()
        if node in self.dist.keys():
            n = len(self.dist.keys())-1
            return n/sum(i for i in self.dist[node].values())
