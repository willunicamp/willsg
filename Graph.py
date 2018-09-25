import os

#This graph is a digraph
class Graph:
    def __init__(self):
        self.graph = dict()

    def load_from_file(self, file_path):
        if os.path.exists(file_path):
            f = open(file_path, "r")
            for line in f:
                edge = line.replace('\n','').split(' ')
                print(line)
                v1 = edge[0]
                v2 = edge[1]
                #check if nodes are already in the graph
                if v1 not in self.graph:
                    self.graph[v1] = list()
                if v2 not in self.graph:
                    self.graph[v2] = list();
                #add edge to the graph, if not yet included
                if v2 not in self.graph[v1]:
                    self.graph[v1].append(v2)
                if v1 not in self.graph[v2]:
                    self.graph[v2].append(v1)

    def all_shortest_path_length(self):
        dist = list()
        for v1 in self.graph:
            dist[v1] = list()
            for v2 in self.graph:
                dist[v1].append(v2)
                if(v1 == v2):
                    dist[v1][v2] = 0
                if(v1 != v2):
                    dist[v1][v2] = 1
        for k in self.graph:
            for i in self.graph:
                for j in self.graph:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist





    def closeness_centrality(self):
        return 0
