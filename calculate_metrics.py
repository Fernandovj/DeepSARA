def calculate_profit_nodes(nslr,end_simulation_time):
    #Calculates profit per time unit and then multiplies it by the nslr op. time
    #profit = revenue-cost 
    cost = 0
    revenue = 0    
    vnfs = nslr.nsl_graph_reduced["vnodes"]
    time = 0.0

    cf_cpu = 0 #cost factor of physical nodes(depends on node type)
    for vnf in vnfs:
        if vnf["type"] == 0:#central
            cf_cpu = 1
        elif vnf["type"] == 1:#edge
            cf_cpu = 3
        # else:
        #     cf_cpu = 4 
        cost += vnf["cpu"]*cf_cpu
        revenue += vnf["cpu"]*cf_cpu*2#revenue es el doble del costo (hasta ahora) 

    if nslr.end_time > end_simulation_time:
        #si es mayor, se considera la porcion de tiempo hasta acabar la simulacion  
        time = nslr.operation_time - (nslr.end_time-end_simulation_time)
    else:
        time = nslr.operation_time

    profit = (revenue-cost)*time 
    return profit

def calculate_profit_links(nslr,end_simulation_time):
    #Calculates profit per time unit and then multiplies it by the nslr op. time
    #profit = revenue-cost 
    cost = 0
    revenue = 0        
    vlinks = nslr.nsl_graph_reduced["vlinks"]    
    cf_bw =  0.5#cost factor of physical links    
    time = 0.0

    for vlink in vlinks:
        try:
            hops = len(vlink["mapped_to"])-1
        except KeyError:
            hops=0
        cost += vlink["bw"]*cf_bw*hops #cost is proportional to the number of hops
        revenue += vlink["bw"]*cf_bw*5*1.5 #(5:se cobra considerando el max num de hops permitido y 1.5: un 50% adicional al cost con 5hops)

    if nslr.end_time > end_simulation_time:
        #si es mayor, se considera la porcion de tiempo hasta acabar la simulacao  
        time = nslr.operation_time - (nslr.end_time-end_simulation_time)
    else:
        time = nslr.operation_time

    profit = (revenue-cost)*time
    return profit

def calculate_request_utilization(nslr,end_simulation_time,substrate):
    vnfs = nslr.nsl_graph_reduced["vnodes"]
    vlinks = nslr.nsl_graph_reduced["vlinks"]
    time = 0.0
    central_sum = 0
    edge_sum = 0
    bw_sum = 0 
    
    for vnf in vnfs:
        if vnf["type"] == 0:#central
            central_sum += vnf["cpu"]
        elif vnf["type"] == 1:#edge
            edge_sum += vnf["cpu"]

    for vlink in vlinks:
        bw_sum += vlink["bw"]      
        

    if nslr.end_time > end_simulation_time:
        #si es mayor, se considera la porcion de tiempo hasta acabar la simulacion  
        time = nslr.operation_time - (nslr.end_time-end_simulation_time)
    else:
        time = nslr.operation_time

    edge_utl = edge_sum*time
    central_utl = central_sum*time
    links_utl = bw_sum*time  

    return edge_utl, central_utl, links_utl

# def calculate_request_utilization(nslr,end_simulation_time,substrate):
#     '''
#         Calculates resource utilization of the current requests
#         utilization: the time the resource was busy
#         profit = revenue-cost 
#     '''
#     utl = 0 
#     vnfs = nslr.nsl_graph_reduced["vnodes"]
#     vlinks = nslr.nsl_graph_reduced["vlinks"]  
#     time = 0.0
#     central_sum = 0
#     # local_sum = 0 
#     edge_sum = 0
#     bw_sum = 0
#     # print("substrate",substrate["nodes"])
#     # print("vnfs",vnfs)
#     for vnf in vnfs:
#         # print("**+",substrate["nodes"][vnf["mapped_to"]]["type"])
#         if substrate["graph"]["nodes"][vnf["mapped_to"]]["type"] == 0:
#             central_sum += vnf["cpu"]
#         # elif substrate["nodes"][vnf["mapped_to"]]["type"] == 1:
#         #     local_sum += vnf["cpu"]
#         elif substrate["graph"]["nodes"][vnf["mapped_to"]]["type"] == 1:
#             edge_sum += vnf["cpu"]
        
#         # else:
#         #     edge_sum += vnf["cpu"]  
    
#     for vlink in vlinks:
#         bw_sum += vlink["bw"]        

#     if nslr.end_time > end_simulation_time:
#         #si es mayor, se considera la porcion de tiempo hasta acabar la simulacion  
#         time = nslr.operation_time - (nslr.end_time-end_simulation_time)
#     else:
#         time = nslr.operation_time
#     # print("**++",edge_sum)
#     edge_utl = edge_sum*time 
#     # local_utl = local_sum*time 
#     central_utl = central_sum*time
#     # print("**++",central_utl)
#     links_utl = bw_sum*time 
#     # print("**++",edge_utl)
#     return edge_utl, central_utl, links_utl


