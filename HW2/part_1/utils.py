import numpy as np
import os
import pyedflib
import connectivipy
import matplotlib.pyplot as plt
import networkx as nx

def read_file(file, channels = None):
    '''
    Read an EDF file, with the given channels. If channels it's not provided,
    it reads every channel in the file.
    '''
    
    f = pyedflib.EdfReader(file)
    
    if channels:
        n = len(channels)
        
        signal_labels = [name.replace(".","") for name in f.getSignalLabels()]
        
        signals = np.zeros((n, f.getNSamples()[0]))
        
        for idx,chan in enumerate(channels):
            
            signals[idx, :] = f.readSignal(signal_labels.index(chan))
        
        f._close()
        
    else:

        n = f.signals_in_file
    
        signals = np.zeros((n, f.getNSamples()[0]))
        
        for chan in np.arange(n):
            signals[chan, :] = f.readSignal(chan)
    
        f._close()

    del f
    
    return signals

def fit_model(data, fs, resolution, method, freq = None, boot = False):
    '''
    Fit an MVAR model, and compute connecitvity estimation via PDC or DTF.
    '''
    
    if boot:
        
        data = connectivipy.Data(data = data, fs = 160, chan_names = get_labels_nodes(19))
        data.fit_mvar(method = "yw")
        data.conn("pdc")
        res = data.significance(Nrep = 200, alpha = 0.05, verbose = False)
        np.fill_diagonal(res,0)
        return res
    
    
    model = connectivipy.Mvar().fit(data, method = "yw")
      
    
    if method == "dtf":
        if freq:
            res = connectivipy.conn.dtf_fun(model[0],model[1],fs = fs, resolution = resolution)[freq,:,:]
            np.fill_diagonal(res,0)
            return res
        else:
            return connectivipy.conn.dtf_fun(model[0],model[1],fs = fs, resolution = resolution)
    elif method == "pdc":
        if freq:
            res = connectivipy.conn.pdc_fun(model[0],model[1],fs = fs, resolution = resolution)[freq,:,:]
            np.fill_diagonal(res,0)
            return res
        else:
            return connectivipy.conn.pdc_fun(model[0],model[1],fs = fs, resolution = resolution)
    else:
        return "Wrong method. Use \"pdc\" or \"dtf\""
    
    
def graph_density(edges,n):
    return (2*edges)/(n*(n-1))


def find_threshold(network, density):
        
    n = network.shape[0]
    
    num_edges = int((density*n*(n-1))/2)
    
    threshold = -np.sort(-network, axis = None)[num_edges+1]
    
    return threshold

def adjacency_matrix(network, threshold, file=None):
    adj = (network > threshold).astype(int)
    if file:
        #Save the npy
        np.save("results/npy/"+file+".npy",adj)
        
        #Save the png
        
        plt.figure(figsize = (20,20))
        
        ############################ MODIFY HERE FOR THE VISUALIZATION
            
        plt.imshow(adj, cmap='Blues', interpolation='none')
       
        
        ############################
        
        plt.savefig("results/png/adj_matrices/"+file+".png")
        plt.close()
        
        return
    return adj
  
    

def get_networks():
    return os.listdir("results/npy")

def get_coordinates():
    
    with open("../data/channel_locations.txt") as f:
        
        coord = {}
        
        channels = [row.split(" ") for row in f.readlines()]
        
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
    

def viz_graph(file):
    
    adj = np.load("../part_1/results/npy/"+file+".npy")
    G = nx.from_numpy_matrix(adj, create_using = nx.DiGraph())
    G = nx.relabel_nodes(G, dict(enumerate(get_labels_nodes(adj.shape[0]))))
    node_sizes = list(G.degree().items())
    
    ############################ MODIFY HERE FOR THE VISUALIZATION
    
    nx.draw(G, pos = get_coordinates(), with_labels = True, nodelist = [elem[0] for elem in node_sizes],
            node_size = [(elem[1]+1)*50 for elem in node_sizes], cmap=plt.cm.autumn_r, node_color = range(len(G.nodes())))
    
    
    ############################
    
        
    plt.title(file, fontsize=25)
    plt.savefig("results/png/networks/"+file+".png", bbox_inches='tight')
    plt.close()
    return