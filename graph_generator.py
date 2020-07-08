
"""
-If a graph is connected then edges >= n-1
-If a graph has more than (n-1)(n-2)/2 edges, then it is connected.
#G = nx.gnm_random_graph(n,(2*n)-1) # a graph is chosen uniformly at random from the set of all graphs with n nodes and m edges
barabasi_albert_graph returns a random graph according to the Barabasi-Albert preferential attachment model
A graph of n nodes is grown by attaching new nodes each with m edges that are preferentially attached to existing nodes with high degree. 1 <= m < n
"""
import json
import networkx as nx
import random
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

#configuration parameters
# cpu_central = (80,100) #cpu range for centralized nodes, se usa una tupla que es un obj inmutable 
# str_central = (120,200)
# cpu_local = (65,85)
# cpu_edge = (50,70) #storage range for edge nodes
# str_edge = (60,100)


cpu_central = (300,300) #cpu range for centralized nodes, se usa una tupla que es un obj inmutable 
#str_central = (200,200)
#cpu_local = (150,150)
cpu_edge = (100,100) #storage range for edge nodes
#str_edge = (100,100)
bw_range = (50,50) #bandwidth range


# lista = [0,0,0,1,1,1,1,2,2,2,2,2,2]
lista_dos = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#50
#lista_uno = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#35
lista_cero = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#17
lista = lista_dos + lista_cero

    
def ba_graph(name,n):
    print("***")
    # n = random.randint(10,15)    
    G = nx.barabasi_albert_graph(n,2) #n:Number of nodes m:Number of edges to attach from a new node to existing nodes

    G.graph["min_cpu_cost"] = 0#min cost possible in a time unit
    G.graph["max_cpu_revenue"] = 0#max revenue possible in a time unit
    G.graph["edge_cpu"] = 0
    #G.graph["local_cpu"] = 0
    G.graph["centralized_cpu"] = 0
    G.graph["min_bw_cost"] = 0 
    G.graph["max_bw_revenue"] = 0
    #capacities (cpu,str) are added to nodes randomly considering the intervals above:    
    # random.seed(n)
    for n in G.nodes():
        # r = random.randint(1,10)
        # if r <= 4: #probabilidad de edge nodes
        #     node_type = 2 #edge node
        # elif r <= 7: 
        #     node_type = 1 #local node
        # else:
        #     node_type = 0 #centralized node
        
        node_type = random.choice(lista)
        print("node type:", node_type)    
        G.nodes[n]["type"] = node_type 
        
        if node_type == 1:
            G.nodes[n]["cpu"] = random.randint(cpu_edge[0],cpu_edge[1])
            # G.nodes[n]["str"] = random.randint(str_edge[0],str_edge[1])
            G.graph["edge_cpu"] += G.nodes[n]["cpu"]
            G.graph["min_cpu_cost"] += G.nodes[n]["cpu"]*3#()
            G.graph["max_cpu_revenue"] += G.nodes[n]["cpu"]*6#(ganancia)
        
        #elif node_type == 1:
            #G.nodes[n]["cpu"] = random.randint(cpu_local[0],cpu_local[1])
            #G.nodes[n]["str"] = random.randint(str_local[0],str_local[1])
            #G.graph["local_cpu"] += G.nodes[n]["cpu"]
            #G.graph["min_cpu_cost"] += G.nodes[n]["cpu"]*1.5
            #G.graph["max_cpu_revenue"] += G.nodes[n]["cpu"]*3

        else:    
            G.nodes[n]["cpu"] = random.randint(cpu_central[0],cpu_central[1])
            # G.nodes[n]["str"] = random.randint(str_central[0],str_central[1])
            G.graph["centralized_cpu"] += G.nodes[n]["cpu"]
            G.graph["min_cpu_cost"] += G.nodes[n]["cpu"]*1
            G.graph["max_cpu_revenue"] += G.nodes[n]["cpu"]*2

    #max_cpu_profit in a time unit        
    G.graph["max_cpu_profit"] = G.graph["max_cpu_revenue"]-G.graph["min_cpu_cost"]

    for l in G.edges():
        G.edges[l]["bw"] = random.randint(bw_range[0],bw_range[1])
        G.graph["min_bw_cost"] += G.edges[l]["bw"] * 0.5
        G.graph["max_bw_revenue"] += G.edges[l]["bw"] * 0.5*5*1.5

    G.graph["max_bw_profit"] = G.graph["max_bw_revenue"]-G.graph["min_bw_cost"]
    
    nx.draw(G, with_labels=True, font_weight='bold')    
    plt.savefig("graph_"+name+".png") # save as png    
    plt.close()
    #print(G.nodes())
    #print(G.nodes().data())     
    G_nl_format = nx.node_link_data(G) # returns the graph in a node-link format     
    # print("G_nl_format:",G_nl_format)
    #plt.show() # display
    with open(name+'.json', 'w') as json_file:
        json.dump(G_nl_format, json_file)    
    return G_nl_format

    # return substrate ##quitarrrr

topo = ba_graph("10",10)