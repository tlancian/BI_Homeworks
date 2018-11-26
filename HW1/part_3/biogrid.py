import utils as ut

# Initialize the gene list
with open("../seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]

### BioGRID

# from the list of seed genes get all the interactions
interactor_lst = ut.query_biogrid(genes)

# select all the genes not in the given list
set_1st_col = set(i[0] for i in interactor_lst)
set_2nd_col = set(i[1] for i in interactor_lst)

# eliminare 'UNQ574/PRO1136'
set_2nd_col.remove('UNQ574/PRO1136')

set_all = set_1st_col.union(set_2nd_col)
set_given_genes = set(genes)
set_new_genes = set_all.difference(set_given_genes)
new_genes_lst = list(set_new_genes)

# list of interactions
interactor_lst_new_genes = ut.query_biogrid(new_genes_lst)

# save
with open("biogrid.tsv","w") as results:
    results.write("Gene_1\tGene_2\n")
    results.writelines("%s\t%s\n" % line for line in interactor_lst_new_genes)


# TODO: Check how to print protein names
# TODO: check if function can be taken from elsewhere