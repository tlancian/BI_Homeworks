import bioservices.uniprot as up

def get_info(gene):
    u = up.UniProt()
    return u.search(gene+"+AND+reviewed:yes", columns="genes(PREFERRED)").split("\n")

