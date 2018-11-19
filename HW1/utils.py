import bioservices.uniprot as up

# Return the results of a query of UniProt DB
#TODO: check which columns has to be taken into account
def get_info(gene):
    u = up.UniProt()
    return u.search(gene+"+AND+reviewed:yes+AND+organism:9606").split("\n")

