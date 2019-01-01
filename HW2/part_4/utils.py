import networkx as nx
import numpy as np
from modularity_maximization import partition
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

import igraph
import louvain

def get_labels_nodes(number_of_nodes = 64):
    if number_of_nodes == 64:
        return ['Fc5', 'Fc3', 'Fc1', 'Fcz', 'Fc2', 'Fc4', 'Fc6', 'C5', 'C3', 'C1',
                'Cz', 'C2', 'C4', 'C6', 'Cp5', 'Cp3', 'Cp1', 'Cpz', 'Cp2', 'Cp4',
                'Cp6', 'Fp1', 'Fpz', 'Fp2', 'Af7', 'Af3', 'Afz', 'Af4', 'Af8', 'F7',
                'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6', 'F8', 'Ft7', 'Ft8', 'T7',
                'T8', 'T9', 'T10', 'Tp7', 'Tp8', 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2',
                'P4', 'P6', 'P8', 'Po7', 'Po3', 'Poz', 'Po4', 'Po8', 'O1', 'Oz', 'O2', 'Iz']
    else:
        return ["Fp1", "Fp2", "F7", "F3", "Fz", "F4", "F8", "T7", "C3", "Cz",
                "C4", "T8", "P7", "P3", "Pz", "P4", "P8", "O1", "O2"]

def read_graph(file):
    adj = np.load("../part_1/results/npy/"+file+".npy")
    
    G = igraph.Graph.Adjacency((adj > 0).tolist())
    #G = nx.from_numpy_matrix(adj, create_using = nx.DiGraph())
    #G = nx.relabel_nodes(G, dict(enumerate(get_labels_nodes(adj.shape[0]))))
    return G


def get_communities(graph):
    return louvain.find_partition(graph,louvain.ModularityVertexPartition)
    
    #res = defaultdict(list)
    
    #for key, value in partition_com.items():
    #    res[value].append(key)
        
    #communities = res.items()
    
    #pd.DataFrame({"community": [elem[0] for elem in communities], "members": [elem[1] for elem in communities]}).to_excel("results/"+file+".xlsx")
    
    #return partition_com

def get_coordinates():
    
    with open("../data/channel_locations.txt") as f:
        
        coord = {}
        
        channels = [row.split(" ") for row in f.readlines()]
        
        for elem in channels:
            coord[elem[1]] = (float(elem[2]), float(elem[3]))
        
        return coord
    
def draw_communities(network, communities, file_name):
    
    ##################### MODIFY HERE FOR THE VISUALIZATION
    
    nx.draw(network, pos = get_coordinates(), node_color = list(communities.values()), with_labels = True)
    
    #####################
    
    plt.savefig("results/"+file_name+".png")
    plt.close()