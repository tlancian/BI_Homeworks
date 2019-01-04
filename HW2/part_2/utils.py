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
    

def topology(G, filename):
    plt.figure(figsize=(20,10))
    plt.subplot(1,3,1)
    values=[]
    for x in list(G.degree):
        values.append(x[1])
    plt.hist(values)
    plt.xlabel('Degree')
    plt.ylabel('Frequency of nodes')
    plt.title('Degree')

    plt.subplot(1,3,2)
    values=[]
    for x in list(G.in_degree):
        values.append(x[1])
    plt.hist(values)
    plt.xlabel('Degree')
    plt.ylabel('Frequency of nodes')
    plt.title('In-Degree')

    plt.subplot(1,3,3)
    values=[]
    for x in list(G.out_degree):
        values.append(x[1])
    plt.hist(values)
    plt.xlabel('Degree')
    plt.ylabel('Frequency of nodes')
    plt.title('Out-Degree')
    
    plt.savefig('results/' + filename + '.png')