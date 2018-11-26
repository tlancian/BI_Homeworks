from bioservices import BioGRID

# Return a list of tuples representing all the interactions of a given list.
def query_biogrid(genes_lst):
    b = BioGRID(query=genes_lst, taxId = "9606")
    interactors = b.biogrid.interactors
    return interactors
