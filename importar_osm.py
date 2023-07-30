import osmium
import networkx as nx
import matplotlib.pyplot as plt

class OSMHandler(osmium.SimpleHandler):
    def __init__(self, graph):
        super(OSMHandler, self).__init__()
        self.graph = graph
        self.added_nodes = set()
        self.multiple_edges_nodes = []

    def node(self, n):
        self.graph.add_node(n.id, lon=n.location.lon, lat=n.location.lat)
        self.added_nodes.add(n.id)

    def way(self, w):
        nodes = w.nodes
        if len(nodes) < 2:
            return

