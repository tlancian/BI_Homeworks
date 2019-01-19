import networkx as nx
import pandas as pd
import pickle
import matplotlib.pyplot as plt


def read_graph(file):
    
    G = nx.Graph()
    
    with open("../interactomes/"+file+".tsv", "r") as f:
        for row in f.readlines()[1:]:
            edge = row[:-1].split("\t")
            G.add_edge(edge[0],edge[1])
    
    return G


def graph_global_measures(graph, file, cc = False):
    
    if cc:
        graph = max(nx.connected_component_subgraphs(graph), key=len)
        with open("results/lcc/"+file+"_lcc.pickle","wb") as f:
            pickle.dump(graph, f)
            f.close()
                
        measures = ["# of Nodes", "# of Edges", "Average Path Length", "Average Degree", "Average Clustering Coefficient",
                "Network Diameter", "Network Radius", "Centralization"]
        path = "results/lcc/"+file+"_lcc_global_measures.txt"
    else:
        measures = ["# of Nodes", "# of Edges", "# of Connected Components", "# of Isolated Nodes", "Average Path Length", "Average Degree", "Average Clustering Coefficient",
                "Network Diameter", "Network Radius", "Centralization"]
        path = "results/interactomes/"+file+"_global_measures.txt"
    
    nodes = len(graph.nodes())
    
    if nodes < 20:
        with open(path, "w") as f:
            f.write("The graph has less than 20 nodes.")
            f.close()
            return
    
    edges = len(graph.edges())
    
    num_cc = nx.number_connected_components(graph)
    isolated = len(list(nx.isolates(graph)))
    
    try:
        avg_sp = nx.average_shortest_path_length(graph)
    except:
        avg_sp = "Graph not connected"
        
    avg_dg = sum(dict(graph.degree).values())/len(graph.degree)
    
    avg_clust = nx.average_clustering(graph)
    
    try:
        diam = nx.diameter(graph)
    except:
        diam = "Graph not connected"
    
    try:
        radius = nx.radius(graph)
    except:
        radius = "Graph not connected"
        
    centralization = None
    
    if cc:
        values = [nodes, edges, avg_sp, avg_dg, avg_clust, diam, radius, centralization]
        
    else:
        values = [nodes, edges, num_cc, isolated, avg_sp, avg_dg, avg_clust, diam, radius, centralization]
        
    
    with open(path, "w") as f:
        f.writelines([str(elem[0])+"\t"+str(elem[1])+"\n" for elem in list(zip(measures,values))])
        f.close()
    
    if cc:
        lcc_local_measures(graph).to_excel("results/lcc/"+file+"_lcc_local_measures.xlsx")


def lcc_local_measures(graph):
    res = {}
    deg = dict(graph.degree())
    b_cen = nx.betweenness_centrality(graph)
    e_cen = nx.eigenvector_centrality(graph)
    c_cen = nx.closeness_centrality(graph)
    
    for elem in deg.keys():
        res[elem] = [deg[elem]]
        res[elem].append(b_cen[elem])
        res[elem].append(e_cen[elem])
        res[elem].append(c_cen[elem])
        res[elem].append(b_cen[elem]/deg[elem])
    
    return pd.DataFrame.from_dict(res, orient = "index", columns = ["degree", "betweenness", "eigenvector", "closeness" ,"ratio"])


    
def viz_graph(G, filename, cc = False):
    
    if cc:
        G = max(nx.connected_component_subgraphs(G), key=len)
        plt.figure(num=None, figsize=(15,15), dpi=50)
        nx.draw(G, node_size=500,  node_color='#8b9dc3')
        plt.savefig('results/images/' + filename + '.png')
    
    
    else:
        plt.figure(num=None, figsize=(15,15), dpi=50)
        nx.draw(G, with_labels=True, node_size=1000, font_size=18, node_color='#8b9dc3')
        plt.savefig('results/images/' + filename + '.png')
        
        