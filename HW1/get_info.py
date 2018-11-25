import utils as ut


# Initialize the gene list
with open("genes_list.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


#### Official Gene Symbol - HGNC  
    
with open('hgnc_list.tsv', 'w') as results:
    results.write("Gene\tApproved_Symbol\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes, map(ut.query_hgnc, genes))) 

#### Uniprot AC + Protein Name

with open("uniprot.tsv","w") as results:
    results.write("gene\tuniprot_ac\tprotein_name\tfunction\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes,map(ut.query_uniprot, genes)))     

#### Entrez Gene ID

with open("ncbi.tsv","w") as results:
    results.write("Gene\tID\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes,map(ut.query_ncbi, genes)))
    

    
### Merge DFs

df_name_list = ['uniprot.tsv', 'hgnc.tsv', 'ncbi.tsv']
df_final = merge_dfs(df_name_list)
df_final.to_csv('df_final.tsv', sep='\t')


### BioGRID

# from the list of seed genes get all the interactions
interactor_lst = query_biogrid(genes)

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
interactor_lst_new_genes = query_biogrid(new_genes_lst)

# save
with open("biogrid.tsv","w") as results:
    results.write("Gene_1\tGene_2\n")
    results.writelines("%s\t%s\n" % line for line in interactor_lst_new_genes)


# TODO: Check how to print protein names
# TODO: check if function can be taken from elsewhere