import pickle
import networkx as nx
import pandas as pd
import markov_clustering as mc
import community
import numpy as np
from scipy.stats import hypergeom

def read_graph(file):
    
    with open("../part_1/results/lcc/" + file + "_lcc.pickle","rb") as f:
        return pickle.load(f)


def mcl(graph):
    
    mat = nx.to_numpy_matrix(graph)
    
    mod = -1
    
    for val in np.arange(1.2,3,0.1):
        
        res = mc.run_mcl(mat, inflation=val)
        clust = mc.get_clusters(res)
        q = mc.modularity(matrix=np.asmatrix(res), clusters=clust)
        if q > mod:
            clusters = clust
    
    labels = dict(zip(range(len(graph)),graph.nodes()))
    
    return [[labels.get(item) for item in clust] for clust in clusters]


def louvain(G_lcc):
    
    partition = community.best_partition(G_lcc)
    return [[nodes for nodes in partition.keys() if partition[nodes] == com] for com in set(partition.values())]


def check_length_mod(mod):
    if len(mod) >= 10:
        return True

def hypergeom_test(graph, mod):
    
    # Initialize the gene list
    with open("../../HW1/seed_genes.txt","r") as f:
        genes = [gene.rstrip() for gene in f.readlines()]
    
    M = len(graph.nodes())
    n = len(set(genes).intersection(set(graph.nodes())))
    N = len(mod)
    x = len(set(genes).intersection(set(mod)))
    
    pval = hypergeom.sf(x-1, M, n, N)
    
    return [x, N, set(genes).intersection(set(mod)), set(mod).difference(set(genes)), pval]



    
    
def create_table(file, lou_mod, mcl_mod):
    
    lou_mod = [["Louvain"]+elem for elem in lou_mod]
    mcl_mod = [["MCL"]+elem for elem in mcl_mod]
    
    mods = lou_mod + mcl_mod
    
    cols = ["Clustering Algorithm", "Number of Seed Genes", "Number of Genes", "List of Seed Genes", "List of Non-Seed Genes", "P-Value"]
    
    table = pd.DataFrame(data = mods, columns = cols)
    table["Id"] = np.arange(1, table.shape[0]+1)
    
    table.to_excel("results/"+file+".xlsx")
    
    
    put_mod = table[table["P-Value"] < 0.05]
    
    if not put_mod.empty:
        
        for index, row in put_mod.iterrows():
            with open("../part_3/putative_disease_modules/"+file+"_"+str(row["Id"])+".txt", "w") as f:
                f.writelines("%s\n" % l for l in list(row["List of Seed Genes"].union(row["List of Non-Seed Genes"])))
                f.close()
    
    return table






############### Reference

# https://blog.alexlenail.me/understanding-and-implementing-the-hypergeometric-test-in-python-a7db688a7458
