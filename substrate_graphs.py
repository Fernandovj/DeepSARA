"""
-If a graph is connected then edges >= n-1
-If a graph has more than (n-1)(n-2)/2 edges, then it is connected.
#G = nx.gnm_random_graph(n,(2*n)-1) # a graph is chosen uniformly at random from the set of all graphs with n nodes and m edges

barabasi_albert_graph returns a random graph according to the Barabasi-Albert preferential attachment model
A graph of n nodes is grown by attaching new nodes each with m edges that are preferentially attached to existing nodes with high degree. 1 <= m < n

"""
import json
# import networkx as nx
import random
#import matplotlib.pyplot as plt


#0:central, 1:edge

# substrate10 = {"directed": False, "multigraph": False, 
# "graph": {
# "min_cpu_cost": 2300.0, "max_cpu_revenue": 4600, 
# "edge_cpu": 700, "local_cpu": 0, "centralized_cpu": 900, "bw":80000,
# "min_bw_cost": 400.0, "max_bw_revenue": 3000.0, 
# "max_cpu_profit": 2300.0, "max_bw_profit": 2600.0}, 
# "nodes": [
#     {"type": 0, "cpu": 300, "id": 0}, 
#     {"type": 1, "cpu": 100, "id": 1}, 
#     {"type": 1, "cpu": 100, "id": 2}, 
#     {"type": 1, "cpu": 100, "id": 3}, 
#     {"type": 0, "cpu": 300, "id": 4}, 
#     {"type": 1, "cpu": 100, "id": 5}, 
#     {"type": 1, "cpu": 100, "id": 6}, 
#     {"type": 1, "cpu": 100, "id": 7}, 
#     {"type": 0, "cpu": 300, "id": 8}, 
#     {"type": 1, "cpu": 100, "id": 9}], 
# "links": [
#     {"bw": 5000, "source": 0, "target": 2}, 
#     {"bw": 5000, "source": 0, "target": 3}, 
#     {"bw": 5000, "source": 0, "target": 5}, 
#     {"bw": 5000, "source": 0, "target": 7}, 
#     {"bw": 5000, "source": 1, "target": 2}, 
#     {"bw": 5000, "source": 1, "target": 4}, 
#     {"bw": 5000, "source": 2, "target": 3}, 
#     {"bw": 5000, "source": 3, "target": 4}, 
#     {"bw": 5000, "source": 3, "target": 5}, 
#     {"bw": 5000, "source": 4, "target": 6}, 
#     {"bw": 5000, "source": 4, "target": 9}, 
#     {"bw": 5000, "source": 5, "target": 6}, 
#     {"bw": 5000, "source": 5, "target": 7}, 
#     {"bw": 5000, "source": 6, "target": 8}, 
#     {"bw": 5000, "source": 6, "target": 9}, 
#     {"bw": 5000, "source": 7, "target": 8}]}

# # substrate12 = {"directed": False, "multigraph": False, 
# # "graph": {
# #     "min_cpu_cost": 2500.0, "max_cpu_revenue": 5000, 
# #     "edge_cpu": 500, "local_cpu": 600, "centralized_cpu": 600, 
# #     "min_bw_cost": 500.0, "max_bw_revenue": 3750.0, 
# #     "max_cpu_profit": 2500.0, "max_bw_profit": 3250.0}, 
# # "nodes": [
# #     {"type": 2, "cpu": 100, "id": 0}, 
# #     {"type": 0, "cpu": 200, "id": 1}, 
# #     {"type": 1, "cpu": 150, "id": 2}, 
# #     {"type": 2, "cpu": 100, "id": 3}, 
# #     {"type": 1, "cpu": 150, "id": 4}, 
# #     {"type": 1, "cpu": 150, "id": 5}, 
# #     {"type": 0, "cpu": 200, "id": 6}, 
# #     {"type": 2, "cpu": 100, "id": 7}, 
# #     {"type": 1, "cpu": 150, "id": 8}, 
# #     {"type": 2, "cpu": 100, "id": 9}, 
# #     {"type": 0, "cpu": 200, "id": 10}, 
# #     {"type": 2, "cpu": 100, "id": 11}], 
# #     "links": [
# #     {"bw": 5000, "source": 0, "target": 2}, 
# #     {"bw": 5000, "source": 0, "target": 3}, 
# #     {"bw": 5000, "source": 1, "target": 2}, 
# #     {"bw": 5000, "source": 1, "target": 3}, 
# #     {"bw": 5000, "source": 1, "target": 4}, 
# #     {"bw": 5000, "source": 1, "target": 5}, 
# #     {"bw": 5000, "source": 1, "target": 6}, 
# #     {"bw": 5000, "source": 1, "target": 7}, 
# #     {"bw": 5000, "source": 1, "target": 9}, 
# #     {"bw": 5000, "source": 1, "target": 10}, 
# #     {"bw": 5000, "source": 3, "target": 4}, 
# #     {"bw": 5000, "source": 3, "target": 5}, 
# #     {"bw": 5000, "source": 3, "target": 6}, 
# #     {"bw": 5000, "source": 3, "target": 7}, 
# #     {"bw": 5000, "source": 3, "target": 8}, 
# #     {"bw": 5000, "source": 3, "target": 11}, 
# #     {"bw": 5000, "source": 7, "target": 8}, 
# #     {"bw": 5000, "source": 7, "target": 10}, 
# #     {"bw": 5000, "source": 7, "target": 11}, 
# #     {"bw": 5000, "source": 8, "target": 9}]}

# substrate12 = {"directed": False, "multigraph": False, 
# "graph": {
#     "min_cpu_cost": 3800.0, "max_cpu_revenue": 7600, 
#     "edge_cpu": 500, "local_cpu": 600, "centralized_cpu": 600, "bw":100000, 
#     "min_bw_cost": 500.0, "max_bw_revenue": 3750.0, 
#     "max_cpu_profit": 3800.0, "max_bw_profit": 3250.0}, 
# "nodes": [
#     {"type": 2, "cpu": 100, "id": 0}, 
#     {"type": 1, "cpu": 150, "id": 1}, 
#     {"type": 0, "cpu": 200, "id": 2}, 
#     {"type": 0, "cpu": 200, "id": 3}, 
#     {"type": 1, "cpu": 150, "id": 4}, 
#     {"type": 2, "cpu": 100, "id": 5}, 
#     {"type": 0, "cpu": 200, "id": 6}, 
#     {"type": 2, "cpu": 100, "id": 7}, 
#     {"type": 1, "cpu": 150, "id": 8}, 
#     {"type": 2, "cpu": 100, "id": 9}, 
#     {"type": 2, "cpu": 100, "id": 10}, 
#     {"type": 1, "cpu": 150, "id": 11}], 
# "links": [
#     {"bw": 5000, "source": 0, "target": 2}, 
#     {"bw": 5000, "source": 0, "target": 3}, 
#     {"bw": 5000, "source": 0, "target": 4}, 
#     {"bw": 5000, "source": 0, "target": 5}, 
#     {"bw": 5000, "source": 0, "target": 6}, 
#     {"bw": 5000, "source": 0, "target": 8}, 
#     {"bw": 5000, "source": 1, "target": 2}, 
#     {"bw": 5000, "source": 1, "target": 4}, 
#     {"bw": 5000, "source": 1, "target": 5}, 
#     {"bw": 5000, "source": 1, "target": 9}, 
#     {"bw": 5000, "source": 2, "target": 3}, 
#     {"bw": 5000, "source": 3, "target": 7}, 
#     {"bw": 5000, "source": 4, "target": 6}, 
#     {"bw": 5000, "source": 6, "target": 7}, 
#     {"bw": 5000, "source": 6, "target": 8}, 
#     {"bw": 5000, "source": 6, "target": 9}, 
#     {"bw": 5000, "source": 6, "target": 10}, 
#     {"bw": 5000, "source": 6, "target": 11}, 
#     {"bw": 5000, "source": 9, "target": 10}, 
#     {"bw": 5000, "source": 10, "target": 11}]}

# substrate14 = {"directed": False, "multigraph": False, 
# "graph": {
#     "min_cpu_cost": 4600.0, "max_cpu_revenue": 9200, 
#     "edge_cpu": 700, "local_cpu": 600, "centralized_cpu": 600, "bw":120000,
#     "min_bw_cost": 600.0, "max_bw_revenue": 4500.0, 
#     "max_cpu_profit": 4600.0, "max_bw_profit": 3900.0}, 
# "nodes": [
#     {"type": 2, "cpu": 100, "id": 0}, 
#     {"type": 2, "cpu": 100, "id": 1}, 
#     {"type": 1, "cpu": 150, "id": 2}, 
#     {"type": 0, "cpu": 200, "id": 3}, 
#     {"type": 2, "cpu": 100, "id": 4}, 
#     {"type": 2, "cpu": 100, "id": 5}, 
#     {"type": 1, "cpu": 150, "id": 6}, 
#     {"type": 0, "cpu": 200, "id": 7}, 
#     {"type": 1, "cpu": 150, "id": 8}, 
#     {"type": 0, "cpu": 200, "id": 9}, 
#     {"type": 2, "cpu": 100, "id": 10}, 
#     {"type": 1, "cpu": 150, "id": 11}, 
#     {"type": 2, "cpu": 100, "id": 12}, 
#     {"type": 2, "cpu": 100, "id": 13}], 
# "links": [
#     {"bw": 5000, "source": 0, "target": 2}, 
#     {"bw": 5000, "source": 1, "target": 2}, 
#     {"bw": 5000, "source": 1, "target": 3}, 
#     {"bw": 5000, "source": 1, "target": 4}, 
#     {"bw": 5000, "source": 1, "target": 5}, 
#     {"bw": 5000, "source": 1, "target": 7}, 
#     {"bw": 5000, "source": 1, "target": 8}, 
#     {"bw": 5000, "source": 1, "target": 11}, 
#     {"bw": 5000, "source": 2, "target": 3}, 
#     {"bw": 5000, "source": 3, "target": 4}, 
#     {"bw": 5000, "source": 3, "target": 6}, 
#     {"bw": 5000, "source": 3, "target": 7}, 
#     {"bw": 5000, "source": 4, "target": 5}, 
#     {"bw": 5000, "source": 4, "target": 6}, 
#     {"bw": 5000, "source": 4, "target": 10}, 
#     {"bw": 5000, "source": 5, "target": 8}, 
#     {"bw": 5000, "source": 5, "target": 9}, 
#     {"bw": 5000, "source": 5, "target": 10}, 
#     {"bw": 5000, "source": 5, "target": 11}, 
#     {"bw": 5000, "source": 5, "target": 12}, 
#     {"bw": 5000, "source": 5, "target": 13}, 
#     {"bw": 5000, "source": 6, "target": 9}, 
#     {"bw": 5000, "source": 6, "target": 12}, 
#     {"bw": 5000, "source": 6, "target": 13}]}

'''
    node cost = edge*3 + central 
'''

substrate16 = {"directed": False, "multigraph": False, 
"graph": {
    "min_cpu_cost": 4800, "max_cpu_revenue": 9600, 
    "edge_cpu": 1200, "local_cpu": 0, "centralized_cpu": 1200, "bw":1400, 
    "min_bw_cost": 700.0, "max_bw_revenue": 5250.0, 
    "max_cpu_profit": 4800, "max_bw_profit": 4550.0,

"nodes": [
    {"type": 0, "cpu": 300, "id": 0}, 
    {"type": 1, "cpu": 100, "id": 1}, 
    {"type": 1, "cpu": 100, "id": 2}, 
    {"type": 0, "cpu": 300, "id": 3}, 
    {"type": 1, "cpu": 100, "id": 4}, 
    {"type": 1, "cpu": 100, "id": 5}, 
    {"type": 1, "cpu": 100, "id": 6}, 
    {"type": 1, "cpu": 100, "id": 7}, 
    {"type": 0, "cpu": 300, "id": 8}, 
    {"type": 1, "cpu": 100, "id": 9}, 
    {"type": 1, "cpu": 100, "id": 10}, 
    {"type": 1, "cpu": 100, "id": 11}, 
    {"type": 1, "cpu": 100, "id": 12}, 
    {"type": 0, "cpu": 300, "id": 13}, 
    {"type": 1, "cpu": 100, "id": 14}, 
    {"type": 1, "cpu": 100, "id": 15}], 
"links": [
    {"bw": 50, "source": 0, "target": 2}, 
    {"bw": 50, "source": 0, "target": 8}, 
    {"bw": 50, "source": 0, "target": 10},
    {"bw": 50, "source": 0, "target": 12}, 
    {"bw": 50, "source": 1, "target": 2}, 
    {"bw": 50, "source": 1, "target": 3}, 
    {"bw": 50, "source": 1, "target": 5}, 
    {"bw": 50, "source": 1, "target": 6}, 
    {"bw": 50, "source": 1, "target": 11}, 
    {"bw": 50, "source": 1, "target": 13}, 
    {"bw": 50, "source": 1, "target": 14}, 
    {"bw": 50, "source": 2, "target": 3}, 
    {"bw": 50, "source": 2, "target": 4}, 
    {"bw": 50, "source": 2, "target": 7}, 
    {"bw": 50, "source": 2, "target": 12}, 
    {"bw": 50, "source": 2, "target": 15}, 
    {"bw": 50, "source": 3, "target": 4}, 
    {"bw": 50, "source": 3, "target": 15}, 
    {"bw": 50, "source": 4, "target": 5}, 
    {"bw": 50, "source": 5, "target": 6}, 
    {"bw": 50, "source": 5, "target": 7}, 
    {"bw": 50, "source": 5, "target": 9}, 
    {"bw": 50, "source": 6, "target": 8}, 
    {"bw": 50, "source": 7, "target": 11}, 
    {"bw": 50, "source": 8, "target": 9}, 
    {"bw": 50, "source": 8, "target": 14}, 
    {"bw": 50, "source": 9, "target": 10}, 
    {"bw": 50, "source": 9, "target": 13}]
    }
}

abilene = {'directed': False, 'multigraph': False, 
'graph': {
    'DateObtained': '3/02/11', 'GeoLocation': 'US', 'GeoExtent': 'Country', 'Network': 'Abilene', 
    'Provenance': 'Primary', 'Access': 0, 'Source': 'http://www.internet2.edu/pubs/200502-IS-AN.pdf', 
    'Version': '1.0', 'Type': 'REN', 'DateType': 'Historic', 'Backbone': 1, 'Commercial': 0, 'label': 
    'Abilene', 'ToolsetVersion': '0.3.34dev-20120328', 'Customer': 0, 'IX': 0, 'SourceGitVersion': 'e278b1b', 
    'DateModifier': '=', 'DateMonth': '02', 'LastAccess': '3/02/11', 'Layer': 'IP', 'Creator': 'Topology Zoo Toolset', 
    'Developed': 0, 'Transit': 0, 'NetworkDate': '2005_02', 'DateYear': '2005', 'LastProcessed': '2011_09_01', 
    'Testbed': 0,
    "min_cpu_cost": 3300, "max_cpu_revenue": 6600, 
    "edge_cpu": 800, "local_cpu": 0, "centralized_cpu": 900, "bw":700, 
    "min_bw_cost": 350.0, "max_bw_revenue": 2625.0, 
    "max_cpu_profit": 3300, "max_bw_profit": 2275.0, 
'nodes': [
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -74.00597, 'Internal': 1, 'Latitude': 40.71427, 'id': 'New York'}, 
    {"type": 0, "cpu": 300,'Country': 'United States', 'Longitude': -87.65005, 'Internal': 1, 'Latitude': 41.85003, 'id': 'Chicago'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -77.03637, 'Internal': 1, 'Latitude': 38.89511, 'id': 'Washington DC'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -122.33207, 'Internal': 1, 'Latitude': 47.60621, 'id': 'Seattle'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -122.03635, 'Internal': 1, 'Latitude': 37.36883, 'id': 'Sunnyvale'}, 
    {"type": 0, "cpu": 300,'Country': 'United States', 'Longitude': -118.24368, 'Internal': 1, 'Latitude': 34.05223, 'id': 'Los Angeles'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -104.9847, 'Internal': 1, 'Latitude': 39.73915, 'id': 'Denver'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -94.62746, 'Internal': 1, 'Latitude': 39.11417, 'id': 'Kansas City'}, 
    {"type": 0, "cpu": 300,'Country': 'United States', 'Longitude': -95.36327, 'Internal': 1, 'Latitude': 29.76328, 'id': 'Houston'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -84.38798, 'Internal': 1, 'Latitude': 33.749, 'id': 'Atlanta'}, 
    {"type": 1, "cpu": 100,'Country': 'United States', 'Longitude': -86.15804, 'Internal': 1, 'Latitude': 39.76838, 'id': 'Indianapolis'}
], 
'links': [
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'New York', 'target': 'Chicago'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'New York', 'target': 'Washington DC'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Chicago', 'target': 'Indianapolis'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Washington DC', 'target': 'Atlanta'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Seattle', 'target': 'Sunnyvale'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Seattle', 'target': 'Denver'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Sunnyvale', 'target': 'Los Angeles'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Sunnyvale', 'target': 'Denver'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Los Angeles', 'target': 'Houston'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Denver', 'target': 'Kansas City'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Kansas City', 'target': 'Houston'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Kansas City', 'target': 'Indianapolis'},
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Houston', 'target': 'Atlanta'}, 
    {"bw": 50,'LinkType': 'OC-192', 'LinkLabel': 'OC-192c', 'LinkNote': 'c', 'source': 'Atlanta', 'target': 'Indianapolis'}
 ]}
 }

def calculate_degree_centrality(substrate):
    links = substrate.graph["links"]
    nodes = substrate.graph["nodes"]
    for i in range(len(substrate.graph["nodes"])):
        degree = 0
        for l in range(len(links)):            
            if links[l]["source"] == i or links[l]["target"] == i:
                degree += 1
        nodes[i]["degree_centrality"] = degree/(len(links)-1)      

def get_graph(n):
    substrate = Substrate()
    if n == 10:
        substrate.set_graph(substrate10["graph"])
    elif n == 12:
        substrate.set_graph(substrate12["graph"])
    elif n == 14:
        substrate.set_graph(substrate14["graph"])
    elif n == "16node_BA":        
        substrate.set_graph(substrate16["graph"])
    elif n == "abilene":
        substrate.set_graph(abilene["graph"])
    else:   
        return "no substrate"
    calculate_degree_centrality(substrate)    
    return substrate 

class Substrate:
    def __init__(self):
        # self.id=id
        self.graph = {}

    def set_graph(self,graph):
        self.graph = graph


    # def set_run_till(self, t):
    #     self.run_till = t

#otras topos: NSF, ANSNET