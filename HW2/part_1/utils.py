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
        
        signal_labels = f.getSignalLabels()
        
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


def fit_model(data, order, fs, resolution, method):
    '''
    Fit an MVAR model, and compute connecitvity estimation via PDC or DTF.
    '''
    
    
    model = connectivipy.Mvar().fit(data, order = order)
    
    
    if method == "dtf":
        return connectivipy.conn.dtf_fun(model[0],model[1],fs = fs, resolution = resolution)
    elif method == "pdc":
        return connectivipy.conn.pdc_fun(model[0],model[1],fs = fs, resolution = resolution)
    else:
        return "Wrong method. Use \"pdc\" or \"dtf\""