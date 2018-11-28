import pandas as pd
import utils as ut


# Initialize the gene list
with open("../seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


###### Preprocessing Biogrid

# Load the file
biogrid = pd.read_csv("../part_3/biogrid.tsv", sep = "\t", nrows = 20)

# Take the genes involved in interactions
unique_genes = list((biogrid["Gene_1"].append(biogrid["Gene_2"])).unique())

# Create a dictionary gene:uniprot_ac
ground_truth = dict(zip(unique_genes,map(ut.query_uniprot, unique_genes)))

#Assign the uniprot_ac according to the gene
biogrid["interactor_1_uniprot"] = biogrid["Gene_1"].map(ground_truth)
biogrid["interactor_2_uniprot"] = biogrid["Gene_2"].map(ground_truth)

# Add DB information
biogrid["database"] = ["BioGrid" for _ in range(biogrid.shape[0])]


###### Preprocessing IID

iid = pd.read_csv("../part_3/iid.txt", sep = "\t", usecols = ["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"], nrows = 20)
iid = iid[["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"]]
iid["database"] = ["IID" for _ in range(iid.shape[0])]



# Uniform column names
biogrid.columns = iid.columns = ["interactor_1", "interactor_2", "interactor_1_uniprot", "interactor_2_uniprot", "database"]



########### Creation of tables


### Seed Genes Interactome

sgi_bio = biogrid.loc[biogrid["interactor_1"].isin(genes) & biogrid["interactor_2"].isin(genes)]
sgi_iid = iid.loc[iid["interactor_1"].isin(genes) & iid["interactor_2"].isin(genes)]

sgi = pd.concat([sgi_bio, sgi_iid])


### Union Interactome

ui_bio = biogrid.loc[biogrid["interactor_1"].isin(genes) | biogrid["interactor_2"].isin(genes)]
ui_iid = iid.loc[iid["interactor_1"].isin(genes) | iid["interactor_2"].isin(genes)]

ui = pd.concat([ui_bio, ui_iid])


### Intersection Interactome

biogrid["set_genes"] = biogrid.apply(lambda row: frozenset([row.interactor_1, row.interactor_2]), axis=1)
iid["set_genes"] = iid.apply(lambda row: frozenset([row.interactor_1, row.interactor_2]), axis=1)

ii = pd.merge(biogrid, iid, how='inner', on=["set_genes"])
