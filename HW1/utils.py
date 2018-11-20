import bioservices.uniprot as up
from Bio import Entrez

# Return the results of a query of UniProt DB
#TODO: check which columns has to be taken into account
def get_info(gene):
    u = up.UniProt()
    return u.search("gene_exact:"+gene+"+AND+reviewed:yes+AND+organism:9606",
                    columns = "id, entry name, protein names, genes, comment(FUNCTION)").split("\n")
    

# Return the results of a query of NCBI DB
def query_ncbi(gene):
    
    Entrez.email = "lanciano.1661409@studenti.uniroma1.it"
    
    handle = Entrez.esearch(db= "gene", term = "("+gene+"[Gene Name]) AND \"Homo sapiens\"[porgn] AND (alive[prop])")
    record = Entrez.read(handle)
    return record["IdList"]
    

