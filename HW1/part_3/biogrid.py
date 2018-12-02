import pandas as pd

# Initialize the gene list
with open("../seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]

### BioGRID

biogrid_all = pd.read_csv("biogrid_all.txt", sep = "\t", usecols = ["Official Symbol Interactor A", "Official Symbol Interactor B"])


# change col names
biogrid_all.columns = ['gene_1', 'gene_2']

# select all interactions of seed genes
sg_interactions = biogrid_all[biogrid_all['gene_1'].isin(genes) | biogrid_all['gene_2'].isin(genes)]


# select new genes
new_genes = set(sg_interactions['gene_1']).union(set(sg_interactions['gene_2'])).difference(genes)

# select interactions among new genes
other_interactions = biogrid_all[biogrid_all['gene_1'].isin(new_genes) & biogrid_all['gene_2'].isin(new_genes)]


# merge dfs
biogrid = pd.concat([sg_interactions, other_interactions])


# drop row duplicates 
biogrid.drop_duplicates(inplace = True)

# save 
biogrid.to_csv('biogrid.tsv', sep='\t', index=False)




### IID

###### Preprocessing IID

iid = pd.read_csv("iid.txt", sep = "\t", usecols = ["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"])
iid.drop_duplicates(inplace = True)
iid.to_csv("iid.tsv", sep = "\t", index = False)


iid_ac = pd.read_csv("iid_ac.txt", sep = "\t", usecols = ["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"])
iid_ac.drop_duplicates(inplace = True)
iid_ac.to_csv("iid_ac.tsv", sep = "\t", index = False)