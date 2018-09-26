#!/usr/bin/env python
__author__ = "William Roberto de Paiva"
__copyright__ = "Copyright 2018, Will's simple graph"
__credits__ = ["William Roberto de Paiva"]
__license__ = "MIT"
__maintainer__ = "William Roberto de Paiva"
__email__ = "will.unicamp@gmail.com"
__status__ = "Production"

from flask import Flask, request
from flask_restful import Resource, Api
import operator
from Graph import Graph

app = Flask(__name__)
api = Api(app)

class Closeness(Resource):
    def get(self):
        cc = g.closeness_centrality()
        sorted_cc = sorted(cc.items(), key=operator.itemgetter(1))
        return {'closeness_centrality': sorted_cc}

class AddEdge(Resource):
    def get(self, node1, node2):
        result = g.add_edge(node1,node2)
        ret = ("Successfully inserted" if result else "Edge could not be inserted")
        return ret

api.add_resource(Closeness, '/closeness') # Route_1
api.add_resource(AddEdge, '/addedge/<node1>/<node2>') # Route_1

if __name__ == '__main__':
    g = Graph()
    app.run(port='4242')
