import numpy
import random
import copy

cpu_embb = (5,5) #cpu units range for eMBB
cpu_urllc = (5,5) 
cpu_miot = (5,5) 
# bw_embb = (1,1) #Mbps
# bw_urllc = (.50,.50) #Mbps
# bw_miot = (.1,.3)

bw_embb = (.5,.5) #Mbps
bw_urllc = (.5,.5) #Mbps
bw_miot = (.01,.01)

#0:centralized, 1:edge
nsl_graph_eMBB =  {
            "vnfs": [
                        {"id":0,"function":"AMF","type":0,"backup":0},
                        {"id":1,"function":"AMF","type":0,"backup":0},
                        {"id":2,"function":"SMF","type":0,"backup":0},
                        {"id":3,"function":"UPF","type":1,"backup":0}
                        # {"id":4,"function":"UPF","type":1,"backup":0}
                        # {"id":5,"function":"UPF","type":1,"backup":0},
                        # {"id":6,"function":"UPF","type":1,"backup":0}
            ],
            "vlinks":[
                        {"source":0,"target":2},
                        {"source":1,"target":2},
                        {"source":2,"target":3}
                        # {"source":2,"target":4}
                        # {"source":3,"target":5},
                        # {"source":4,"target":6}

            ] 
}
nsl_graph_URLLC =  {
            "vnfs": [
                        {"id":0,"function":"AMF","type":0,"backup":0},
                        {"id":1,"function":"AMF","type":0,"backup":1},
                        {"id":2,"function":"SMF","type":0,"backup":0},
                        {"id":3,"function":"SMF","type":0,"backup":1},
                        {"id":4,"function":"UPF","type":1,"backup":0},
                        {"id":5,"function":"UPF","type":1,"backup":1},
                        {"id":6,"function":"UPF","type":1,"backup":2},
                        {"id":7,"function":"UPF","type":1,"backup":3},
                        {"id":8,"function":"UPF","type":1,"backup":3},
                        {"id":9,"function":"UPF","type":1,"backup":3}#,
                        #{"id":10,"function":"UPF","type":2,"backup":3}
            ],
            "vlinks":[
                        {"source":0,"target":2},
                        {"source":1,"target":3},
                        {"source":0,"target":4},
                        {"source":1,"target":5},
                        {"source":0,"target":6},
                        {"source":1,"target":7},
                        {"source":0,"target":8},
                        {"source":1,"target":9}
            ] 
}
nsl_graph_MIoT =  {
            "vnfs": [
                        {"id":0,"function":"AMF","type":0,"backup":0},
                        {"id":1,"function":"AMF","type":0,"backup":0},
                        {"id":2,"function":"AMF","type":0,"backup":0},
                        {"id":3,"function":"SMF","type":0,"backup":0},
                        {"id":4,"function":"UPF","type":0,"backup":0}
            ],
            "vlinks":[
                        {"source":0,"target":3},
                        {"source":1,"target":3},
                        {"source":2,"target":3},
                        {"source":3,"target":4}
            ] 
}

class NSLR():
    def __init__(self,id,service_type,operation_time,nsl_graph):
        self.id=id
        self.service_type = service_type
        self.operation_time = operation_time
        self.nsl_graph = nsl_graph
        self.nsl_graph_reduced = {}
        self.end_time = 0
        self.bandera = random.randint(1,100)

    def set_nsl_graph_reduced(self,reduced_graph):
        self.nsl_graph_reduced = reduced_graph

    def set_end_time(self,end_time):
        self.end_time = end_time


def get_operation_time(mean_operation_time):
    value = numpy.random.exponential(mean_operation_time,1) 
    if round(value[0])== 0: #and round(value[0]) <= 180: #60: #para evitar duraciones de 0 y mayores a un valor
        value[0] = 1     
    return round(value[0])
    #return 400

def add_resources(nsl_graph,service_type):
    cpu = 0
    # print("**",service_type)
    if service_type == "embb":
        # print("entro")
        cpu = cpu_embb
        # strg = str_embb
        bw = bw_embb
    elif service_type == "urllc": 
        #print("entro urllc")
        cpu = cpu_urllc
        # strg = str_urllc
        bw = bw_urllc
    elif service_type == "miot":
        cpu = cpu_miot
        # strg = str_miot
        bw = bw_miot

    for v in nsl_graph["vnfs"]:
        v["cpu"] = random.randint(cpu[0],cpu[1])
        # v["str"] = random.randint(strg[0],strg[1])
    for l in nsl_graph["vlinks"]:
        # l["bw"] = random.randint(bw[0],bw[1])
        l["bw"] = random.uniform(bw[0],bw[1])

    return nsl_graph

def get_nslr(id,service_type,mean_operation_time):
    
    if service_type == "embb":
        nsl_graph = nsl_graph_eMBB    
    elif service_type == "urllc":
        nsl_graph = nsl_graph_URLLC 
    elif service_type == "miot":
        nsl_graph = nsl_graph_MIoT
 
    nsl_graph = add_resources(copy.deepcopy(nsl_graph),service_type)
    request = NSLR(id,service_type,get_operation_time(mean_operation_time),nsl_graph)
    return request