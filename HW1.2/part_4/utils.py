import pandas as pd
from Bio import Entrez


def create_network():
    
    data = pd.read_csv("data/biogrid_all.txt", sep = "\t", usecols = ["Entrez Gene Interactor A", "Entrez Gene Interactor B"])
    
    data.to_csv("DIAMOnD/biogrid.txt", index = False, header = False)


# Return the results of a query of NCBI DB
def query_ncbi(gene):
    
    Entrez.email = "lanciano.1661409@studenti.uniroma1.it"
    
    handle = Entrez.esearch(db= "gene", term = "("+gene+"[Gene Name]) AND \"Homo sapiens\"[porgn] AND (alive[prop])")
    record = Entrez.read(handle)
    return int(record["IdList"][0])

def translate(file, output_file):
    
    with open("data/"+file+".txt", "r") as f:
        genes = [gene.rstrip() for gene in f.readlines()]
        
    with open("DIAMOnD/"+output_file+".txt","w") as g:
        g.writelines("%s\n" % line for line in map(query_ncbi, genes))
        
        
def join_files(file_1, file_2, output_file):
    with open("DIAMOnD/"+file_1+".txt", "r") as f1:
        genes_1 = [gene.rstrip() for gene in f1.readlines()]
    
    file_2 = pd.read_csv("DIAMOnD/"+file_2+".txt", sep = "\t")
    genes_2 = list(file_2["DIAMOnD_node"])
        
    
    with open("results/"+output_file+".txt","w") as g:
        g.writelines("%s\n" % line for line in list(set(genes_1+genes_2)))
        
        
def top_ten(file):
    
    data = pd.read_csv("results/" + file + ".txt", sep = "\t")
    
    data.sort_values(by = ["Pathway p-value (corrected)"], inplace = True)
    
    data.iloc[:10,:].to_excel("results/"+ file +".xlsx")
    
    