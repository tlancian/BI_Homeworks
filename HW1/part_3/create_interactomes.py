import pandas as pd

# Initialize the gene list
with open("../seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


### BioGRID

# Load the entire Biogrid Dataset
biogrid_all = pd.read_csv("biogrid_all.txt", sep = "\t", usecols = ["Official Symbol Interactor A", "Official Symbol Interactor B"])

#Changing column names in a more useful way
biogrid_all.columns = ['gene_1', 'gene_2']

#Selecting interactions where seed genes are involved
sg_interactions = biogrid_all[biogrid_all['gene_1'].isin(genes) | biogrid_all['gene_2'].isin(genes)]

#Selecting genes that are connected at least to one seed genes
new_genes = set(sg_interactions['gene_1']).union(set(sg_interactions['gene_2'])).difference(genes)

#Selecting interactions among the genes that has at least an interaction with the seed genes
other_interactions = biogrid_all[biogrid_all['gene_1'].isin(new_genes) & biogrid_all['gene_2'].isin(new_genes)]

#Merging the two dataframes and droppin duplicates
biogrid = pd.concat([sg_interactions, other_interactions])
biogrid.drop_duplicates(inplace = True)
biogrid.to_csv('results/biogrid.tsv', sep='\t', index=False)


### IID

#IID dataframes were obtained directly by the website. iid represents the one where the query was made with the names of the genes, iid_ac with
#Uniprot accession number.

#Below we just drop duplicates for these 2 datasets.

iid = pd.read_csv("iid.txt", sep = "\t", usecols = ["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"])
iid.drop_duplicates(inplace = True)
iid.to_csv("results/iid.tsv", sep = "\t", index = False, columns = ["Query Symbol", "Partner Symbol"])
iid.to_csv("iid.txt", sep = "\t", index = False)


iid_ac = pd.read_csv("iid_ac.txt", sep = "\t", usecols = ["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"])
iid_ac.drop_duplicates(inplace = True)
iid_ac.to_csv("results/iid_ac.tsv", sep = "\t", index = False, columns = ["Query Symbol", "Partner Symbol"])
iid_ac.to_csv("iid_ac.txt", sep = "\t", index = False)
