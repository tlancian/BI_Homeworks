import bioservices.uniprot as up

def query_uniprot(gene):  
    u = up.UniProt()
    res = u.search("gene_exact:"+gene+"+AND+reviewed:yes+AND+organism:9606", 
                        columns = "id").split("\n")
    
    if len(res[1:-1]) == 1:
        return res[1]
    else:
        return res[1:-1]
