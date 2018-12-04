import pandas as pd

def rank_dataset_go(file):
    data = pd.read_csv(file, sep = "\t")
    data.sort_values(["Pathway p-value (corrected)"], inplace = True, ascending = False)
    
    cl= data[data["Source Name"] == "cellular component"].iloc[:10]
    mf = data[data["Source Name"] == "molecular function"].iloc[:10]
    bp = data[data["Source Name"] == "biological process"].iloc[:10]
     
    return cl, mf, bp
    
   
def rank_dataset_path(file):
    data = pd.read_csv(file, sep = "\t", encoding='latin-1')
    data.sort_values(["Pathway p-value (corrected)"], inplace = True, ascending = False)
    
    return data.iloc[:10]