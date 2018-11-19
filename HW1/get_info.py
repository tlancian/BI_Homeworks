import utils as ut

# Initialize the gene list
with open("genes_list.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]

# For each gene quet in the Uniprot DB, and return a tsv with all the results
with open("results.tsv","w") as results:
    results.write("Entry\tEntry name\tStatus\tProtein names\tGene names\tOrganism\tLength\n")
    for elem in map(ut.get_info, genes[:3]):
        results.writelines("%s\n" % line for line in elem[1:])