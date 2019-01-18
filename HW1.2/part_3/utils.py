import bioservices.uniprot as up
import pandas as pd
import os

# Return the results of a query of UniProt DB
def query_uniprot(gene):
    u = up.UniProt()
    return u.search("gene_exact:"+gene+"+AND+reviewed:yes+AND+organism:9606",
                    columns = "id").split("\n")[1]
    
    
def translate(mod):
    with open("putative_disease_modules/"+mod, "r") as f:
        genes = f.readlines()
        f.close()
    
    with open("putative_disease_modules/"+mod[:-4]+"_uniprot.txt", "w") as f:
        f.writelines("%s\n" % l for l in map(query_uniprot, genes))
        

def mod_files(folder):
    return os.listdir(folder)


def top_ten(file):
    
    data = pd.read_csv("results/innate/" + file, sep = "\t")
    
    data.sort_values(by = ["Pathway p-value (corrected)"], inplace = True)
    
    data.iloc[:10,:].to_excel("results/"+ file[:-4] +".xlsx")