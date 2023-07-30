import osmium
import networkx as nx
import matplotlib.pyplot as plt

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, graph):
        super(OSMHandler, self).__init__()
        self.graph = graph
        self.added_nodes = set()
        self.multiple_edges_nodes = []

   