import numpy as np
import pyedflib
import connectivipy


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


def fit_model(data, fs, resolution, method, freq = None):
    '''
    Fit an MVAR model, and compute connecitvity estimation via PDC or DTF.
    '''
    
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
        np.save(file,adj)
        return
    return adj
    
def create_graph_image(G, name):
    for node in G.nodes():
        G.node[node]['node_size'] = G.degree(node)*100
        G.node[node]['label'] = node

    plt.figure(num=None, figsize=(15,15), dpi=50)
    nx.draw(G, node_shape= 'o', node_size=list(nx.get_node_attributes(G,'node_size').values()),
           cmap=plt.cm.autumn_r, node_color=range(64), labels=nx.get_node_attributes(G,'label'))
    plt.title(name, fontsize=25)
    plt.savefig(name + '.png', bbox_inches='tight')
    
