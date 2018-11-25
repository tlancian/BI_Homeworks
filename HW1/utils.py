import bioservices.uniprot as up
from bioservices.hgnc import HGNC
from Bio import Entrez
from functools import reduce
from bioservices import BioGRID

# Return the results of a query in HGCN
def query_hgnc(gene):
    h = HGNC()
    return h.search(gene)['response']['docs'][0]['symbol']



# Return the results of a query of UniProt DB
def query_uniprot(gene):
    u = up.UniProt()
    return u.search("gene_exact:"+gene+"+AND+reviewed:yes+AND+organism:9606",
                    columns = "id, protein names, comment(FUNCTION)").split("\n")[1]
    

# Return the results of a query of NCBI DB
def query_ncbi(gene):
    
    Entrez.email = "lanciano.1661409@studenti.uniroma1.it"
    
    handle = Entrez.esearch(db= "gene", term = "("+gene+"[Gene Name]) AND \"Homo sapiens\"[porgn] AND (alive[prop])")
    record = Entrez.read(handle)
    return record["IdList"]
    

# Merge the DFs: read data from a name list and merge the DFs
def merge_dfs(dfs_name_list):
    dfs_list = []
    for filename in df_name_list:
        df = pd.read_csv(filename, sep='\t', index_col=False).loc[:, 'gene':]
        dfs_list.append(df)
 
    df_final = reduce(lambda left,right: pd.merge(left,right,on='gene'), dfs_list)
    return(df_final)


# Return a list of tuples representing all the interactions of a given list.
def query_biogrid(genes_lst):
    b = BioGRID(query=genes_lst, taxId = "9606")
    interactors = b.biogrid.interactors
    return(interactors)





