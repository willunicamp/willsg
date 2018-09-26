#!/usr/bin/env python
__author__ = "William Roberto de Paiva"
__copyright__ = "Copyright 2018, Will's simple graph"
__credits__ = ["William Roberto de Paiva"]
__license__ = "MIT"
__maintainer__ = "William Roberto de Paiva"
__email__ = "will.unicamp@gmail.com"
__status__ = "Production"

import os

#This graph is a digraph. It does not accept self loops,
#repeated edges or weighted edges.
class Graph:
    def __init__(self):
        #store the graph and the distance matrix
        self.graph = None
        self.dist = None

    def load_from_file(self, file_path):
        self.graph = dict()
        #Check if file exists befor load it
        if os.path.exists(file_path):
            #Open file in readonly mode
            f = open(file_path, "r")
            for line in f:
                #Read each line and split by spaces, removing line breaks
                edge = line.replace('\n','').split(' ')
                #The edge must have 2 vertices, not less, not more
                if len(edge) == 2:
                    v1 = edge[0]
                    v2 = edge[1]
                    self.add_edge(v1,v2)

    def add_vertex(self, v):
        #If we try to add a self loop, a vertex is created
        self.add_edge(v1, v1)

    def add_edge(self, v1, v2):
        #Check if the vertices are not null
        if None not in (v1,v2):
            #if graph is still not initialized, do it now
            if self.graph == None:
                self.graph = dict()
            #check if nodes are already in the graph
            if v1 not in self.graph.keys():
                self.graph[v1] = list()
            if v2 not in self.graph.keys():
                self.graph[v2] = list()
            #nex line prevent self loops
            if v1 != v2:
                #add each vertex as neighbor to the other, if not yet done yet
                if v2 not in self.graph[v1]:
                    self.graph[v1].append(v2)
                if v1 not in self.graph[v2]:
                    self.graph[v2].append(v1)
            return True
        else:
            return False

    #calculates shortest distance from all nodes to all other nodes
    #using Floyd-Warshall algorithm
    def all_shortest_path_length(self):
        #the graph needs to be previously created for
        #this method to be executed
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

    #Normalized closeness centrality -> c_i = sum((n-1)/d(i,j)), j in G
    #Does not works for weakly connected graphs
    #If the node is not defined, the method returns a dictionary with
    #all nodes closeness, else it returns the closeness to the given node
    #if it exists
    def closeness_centrality(self, node=None):
        self.dist = self.all_shortest_path_length()
        n = len(self.dist.keys())-1
        if node is None:
            cc_dict = dict()
            for node in self.graph.keys():
                cc_dict[node] = n/sum(i for i in self.dist[node].values())
            return cc_dict
        if node in self.dist.keys():
            n = len(self.dist.keys())-1
            return n/sum(i for i in self.dist[node].values())
