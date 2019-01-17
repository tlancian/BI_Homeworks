import networkx as nx
import pandas as pd
import markov_clustering as mc
import community
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import hypergeom

### TODO: nella funzione louvain, return i cluster e non la partizione

def read_graph(file):
    
    G = nx.Graph()
    
    with open("../interactomes/"+file+".tsv", "r") as f:
        for row in f.readlines()[1:]:
            edge = row[:-1].split("\t")
            G.add_edge(edge[0],edge[1])
    
    return G


def find_best_inflation(mat):
    
    infl_lst = []
    for inflation in [i/10 for i in range(15, 26)]:
        
        result = mc.run_mcl(mat, inflation=inflation)
        clusters = mc.get_clusters(result)
        Q = mc.modularity(matrix=np.asmatrix(result), clusters=clusters)
        infl_lst.append((Q, inflation))
    
    return(max(infl_lst)[1])

def get_labels(G_lcc, clusters):
    
    # map node name to numbers
    lbls = {}
    for k in range(len(G_lcc)):
        lbls[k] = list(G_lcc.nodes())[k]

    # use labels
    for i in range(len(clusters)):
        clusters[i] = [lbls.get(item, item) for item in clusters[i]]
    
    return(clusters)


def MCL(G_lcc):
    
    mat = nx.to_numpy_matrix(G_lcc)
    
    # find best inflation
    max_infl = find_best_inflation(mat)
    
    result = mc.run_mcl(mat, inflation = max_infl)
    clusters = mc.get_clusters(result)
    
    # return name of genes
    return(get_labels(G_lcc, clusters))


def louvain(G_lcc):
    
    partition = community.best_partition(G_lcc)

    return(partition)


def hypergeom_test(mod, genes, G_lcc):
    
    M = len(G_lcc.nodes())
    n = len(genes)
    N = len(mod)
    x = len(set(genes).intersection(set(mod)))
    
    pval = hypergeom.cdf(x, M, n, N)
    
    return(pval, x, M, n, N)



def find_modules(clusters):
    modules = [i for i in clusters if len(i) >=10]
    
    return(modules)

