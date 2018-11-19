import utils as ut

# Initialize the gene list
with open("genes_list.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]

with open("results.tsv","w") as results:
    results.write("Entry\tEntry name\tStatus\tProtein names\tGene names\tOrganism\tLength\n")
    for elem in map(ut.get_info, genes):
        results.writelines("%s\n" % line for line in elem[1:])