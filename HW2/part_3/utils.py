import numpy as np
import networkx as nx
import os
import pandas as pd
import matplotlib.pyplot as plt

def create_network_file(file):
    
    adj = np.load("../part_1/results/npy/"+file+".npy")
    
    
    with open("mfinder1.2/"+file+".txt", "w") as f:
        for row in range(adj.shape[0]):
            for col in range(adj.shape[1]):
                if adj[row,col] == 1:
                    f.write(str(row+1)+" "+str(col+1) + " 1\n")
        f.close()


def parse_mfinder_output(file):
    
    with open("mfinder1.2/"+file+".txt") as f:
        
        lines = f.readlines()
        
        res = []
        
        for idx,line in enumerate(lines):
            if "Full list of subgraphs" in line:
                nrows = int(''.join(i for i in lines[idx+2] if i.isdigit())[1:])
                
                res.append("Motif ID\tN_Real\tN_Rand\tZ_Score\tP-value\tCREAL\tUniqueness\n")
                
                for i in range(nrows):
                    res.append(lines[idx+6+(2*i)])
        
        f.close()
    
    with open("res.tsv","w") as f:
        f.writelines(res)
        f.close()
    
    data = pd.read_csv("res.tsv", sep = "\t")
    
    data.to_excel("results/"+file+".xlsx")
    
    os.remove("res.tsv")
    
    return

        
    

def subgraph_by_motif(file, motif):
    
    with open("mfinder1.2/"+file+".txt") as f:
        
        members = {}
        
        lines = f.readlines()
        
        for idx,line in enumerate(lines):
            if "subgraph id = " in line:
                motif_id = int(''.join(i for i in line if i.isdigit()))
                num_members = int(''.join(i for i in lines[idx+1] if i.isdigit()))
                triplets = [[int(elem) for elem in row.split("\t")[:-1]] for row in lines[idx+5:idx+5+num_members]]
                
                members[motif_id] = triplets
                
        graph = nx.DiGraph()
    
        for triplet in members[motif]:
            graph.add_edge(triplet[0]-1, triplet[2]-1)
            graph.add_edge(triplet[1]-1, triplet[2]-1)
        
        graph = nx.relabel_nodes(graph, dict(enumerate(get_labels_nodes())))
    
        plt.figure(num=None, figsize=(15,15), dpi=50)
        nx.draw(graph, node_shape= 'o', with_labels = True, pos = get_coordinates(), node_size = 2000, font_size=18)
        #plt.title(file[:9], fontsize=25) 
        

        plt.savefig("results/"+file[:9]+".png")
        plt.close()
    
def get_labels_nodes(number_of_nodes = 64):
    if number_of_nodes == 64:
        return ['Fc5', 'Fc3', 'Fc1', 'Fcz', 'Fc2', 'Fc4', 'Fc6', 'C5', 'C3', 'C1',
                'Cz', 'C2', 'C4', 'C6', 'Cp5', 'Cp3', 'Cp1', 'Cpz', 'Cp2', 'Cp4',
                'Cp6', 'Fp1', 'Fpz', 'Fp2', 'Af7', 'Af3', 'Afz', 'Af4', 'Af8', 'F7',
                'F5', 'F3', 'F1', 'Fz', 'F2', 'F4', 'F6', 'F8', 'Ft7', 'Ft8', 'T7',
                'T8', 'T9', 'T10', 'Tp7', 'Tp8', 'P7', 'P5', 'P3', 'P1', 'Pz', 'P2',
                'P4', 'P6', 'P8', 'Po7', 'Po3', 'Poz', 'Po4', 'Po8', 'O1', 'Oz', 'O2', 'Iz']
    else:
        return ["Fp1", "Fp2", "F7", "F3", "Fz", "F4", "F8", "T7", "C3", "Cz", "C4", "T8", "P7", "P3", "Pz", "P4", "P8", "O1", "O2"]


def get_involved_motifs(file, channel, motifs):
    
    with open("mfinder1.2/"+file+".txt") as f:
        
        res = []

        lines = f.readlines()
        
        for idx,line in enumerate(lines):
            if "subgraph id = " in line:
                motif_id = int(''.join(i for i in line if i.isdigit()))
                num_members = int(''.join(i for i in lines[idx+1] if i.isdigit()))
                if motif_id in motifs:
                    triplets = [[motif_id,triplet] for triplet in [[int(elem) for elem in row.split("\t")[:-1]] for row in lines[idx+5:idx+5+num_members]] if channel in triplet]
                    res.extend(triplets)
        
        data = pd.DataFrame(res,columns = ["Motif_Id", "Triplet"])
        
        data.to_excel("results/"+file[:9]+"_node_"+str(channel)+"_motif.xlsx")
                    
        return
    
    
def get_coordinates():
    
    with open("../data/channel_locations.txt") as f:
        
        coord = {}
        
        channels = [row.split("        ") for row in f.readlines()[1:]]

        for elem in channels:
            coord[elem[1]] = (float(elem[2]), float(elem[3]))
        
        return coord