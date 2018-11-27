import bioservices.uniprot as up

def query_uniprot(gene):  
    u = up.UniProt()
    try:
        return u.search("gene_exact:"+gene+"+AND+reviewed:yes+AND+organism:9606", 
                        columns = "id").split("\n")[1:-1]
    except:
        return "pippo"
