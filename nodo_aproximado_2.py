from geopy.distance import geodesic
from importar_osm import *
import networkx as nx
import math

import networkx as nx
import math

def find_closest_node(graph, target_lat, target_lon):
    closest_node = None
    closest_distance = math.inf

    for node in graph.nodes():
        node_lat = graph.nodes[node]['lat']
        node_lon = graph.nodes[node]['lon']
        distance = math.sqrt((target_lat - node_lat)**2 + (target_lon - node_lon)**2)

        if distance < closest_distance:
            closest_node = node
            closest_distance = distance

    if closest_node is not None:
        # Comprobar si el nodo más cercano está conectado a otros nodos
        if len(list(graph.neighbors(closest_node))) > 0:
            return closest_node
        else:
            return None
    else:
        return None
    
    
    
    





