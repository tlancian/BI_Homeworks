import operator
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt



def save_highest_10(degree_lst, filename):
    df = pd.DataFrame(degree_lst, columns=['channel', 'degree'])
    df.to_csv('results/' + filename + '.csv')


    
def global_indeces(graph_names_lst):
    global_cc = []
    avg_path = []
    for g in graph_names_lst:

        adj = np.load('../part_1/results/npy/' + g + '.npy')
        G = nx.from_numpy_matrix(adj, create_using=nx.DiGraph())
        
        if nx.is_weakly_connected(G):
            global_cc.append(nx.average_clustering(G))
            avg_path.append(nx.average_shortest_path_length(G))
            
        else:
            global_cc.append(nx.average_clustering(G))
            
            G_un = nx.from_numpy_matrix(adj)
            connected_components = nx.connected_component_subgraphs(G_un)
            subgraphs = map(lambda smallGraph : G.subgraph(smallGraph.nodes()), connected_components)
            avgShortestPaths = np.mean(list(map(lambda x: nx.average_shortest_path_length(x), subgraphs )))
            avg_path.append(avgShortestPaths)

    return(global_cc, avg_path)



def global_plot(global_cc, avg_path, filename):
    densities = [5, 10, 20, 30, 50]
    
    plt.subplot(1,2,1)
    plt.plot(densities, global_cc, 'o-')
    plt.title('global_cc - PDC')

    plt.subplot(1,2,2)
    plt.plot(densities, avg_path, 'o-')
    plt.title('avg_path - PDC')
    #plt.show()
    plt.savefig('results/' + filename + '.png')
    

def get_coordinates():
    
    with open("../data/channel_locations.txt") as f:
        
        coord = {}
        
        channels = [row.split("        ") for row in f.readlines()[1:]]

        for elem in channels:
            coord[elem[1]] = (float(elem[2]), float(elem[3]))
        
        return coord
    
    
    
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
    
def topology(G, filename, adj):
    
    G= nx.relabel_nodes(G, dict(enumerate(get_labels_nodes(adj.shape[0]))))

    # degree
    d = dict(nx.degree(G))
    plt.figure(num=None, figsize=(15,15), dpi=50)
    nx.draw(G, nodelist= list(d.keys()), node_size=[v*40  for v in d.values()], with_labels = True, pos = get_coordinates())
    plt.savefig('results/' + filename + '_degree' + '.png')
    
    # in degree
    d = dict(G.in_degree)
    plt.figure(num=None, figsize=(15,15), dpi=50)
    nx.draw(G, nodelist= list(d.keys()), node_size=[v*40  for v in d.values()], with_labels = True, pos = get_coordinates())
    plt.savefig('results/' + filename + '_in_degree' + '.png')
    
    # out degree
    d = dict(G.out_degree)
    plt.figure(num=None, figsize=(15,15), dpi=50)
    nx.draw(G, nodelist= list(d.keys()), node_size=[v*40  for v in d.values()], with_labels = True, pos = get_coordinates())
    plt.savefig('results/' + filename + '_out_degree' + '.png')