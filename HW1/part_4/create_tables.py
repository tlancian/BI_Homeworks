import pandas as pd
import numpy as np
import utils as ut


# Initialize the gene list
with open("../seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


### Preprocessing Biogrid
    
# Since it is requested to report also the Uniprot AC in the table, here we look up for them.

# Load the file
biogrid = pd.read_csv("../part_3/results/biogrid.tsv", sep = "\t")

# Take the genes involved in interactions
unique_genes = list((biogrid["gene_1"].append(biogrid["gene_2"])).unique())

# Create a dictionary gene:uniprot_ac
ground_truth = dict(zip(unique_genes,map(ut.query_uniprot, unique_genes)))

#Assign the uniprot_ac according to the gene
biogrid["interactor_1_uniprot"] = biogrid["gene_1"].map(ground_truth)
biogrid["interactor_2_uniprot"] = biogrid["gene_2"].map(ground_truth)

# Retrieving uniprots where there are more than 2 occurrencies and correcting them manually after a visit at Uniprot website
ac1_unknown = biogrid["gene_1"].loc[(biogrid["interactor_1_uniprot"].apply(type) == list) & (biogrid["interactor_1_uniprot"].apply(len) > 1)].unique()
ac2_unknown = biogrid["gene_2"].loc[(biogrid["interactor_2_uniprot"].apply(type) == list) & (biogrid["interactor_2_uniprot"].apply(len) > 1)].unique()

ac_unknown = list(np.union1d(ac1_unknown,ac2_unknown))

ground_truth["LAP2"] = "Q96RT1"
ground_truth["MCM2"] = "P49736"
ground_truth["MTF1"] = "Q14872"
ground_truth["PRR3"] = "P79522"
ground_truth["SLP1"] = "Q9UBI4"
ground_truth["SP1"] = ground_truth["Sp1"] = "P08047"

#Reassign the uniprot_ac according to the gene
biogrid["interactor_1_uniprot"] = biogrid["gene_1"].map(ground_truth)
biogrid["interactor_2_uniprot"] = biogrid["gene_2"].map(ground_truth)

# Deleting interactions where no Uniprot AC were found, since they involve genes that are not realted to humans.
biogrid.drop(biogrid[(biogrid["interactor_1_uniprot"].apply(type) == list) | (biogrid["interactor_2_uniprot"].apply(type) == list)].index, inplace = True)

# Adding DB information
biogrid["database"] = ["BioGrid" for _ in range(biogrid.shape[0])]

biogrid.to_csv('../part_3/results/biogrid.tsv', sep='\t', index=False)


### Preprocessing IID

#Since Uniprot AC were reported by the website of IID, here we add just the information of the DB
iid = pd.read_csv("../part_3/iid.txt", sep = "\t", usecols = ["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"])
iid = iid[["Query Symbol", "Partner Symbol", "Query UniProt", "Partner UniProt"]]
iid["database"] = ["IID" for _ in range(iid.shape[0])]
iid.drop_duplicates(inplace = True)



# Uniforming column names
biogrid.columns = iid.columns = ["interactor_1", "interactor_2", "interactor_1_uniprot", "interactor_2_uniprot", "database"]



### Creation of tables

### Seed Genes Interactome

sgi_bio = biogrid.loc[biogrid["interactor_1"].isin(genes) & biogrid["interactor_2"].isin(genes)]
sgi_iid = iid.loc[iid["interactor_1"].isin(genes) & iid["interactor_2"].isin(genes)]

sgi = pd.concat([sgi_bio, sgi_iid])

sgi.to_csv("results/sgi.tsv", sep = "\t", index = False)


### Union Interactome

ui_bio = biogrid.loc[biogrid["interactor_1"].isin(genes) | biogrid["interactor_2"].isin(genes)]
ui_iid = iid.loc[iid["interactor_1"].isin(genes) | iid["interactor_2"].isin(genes)]

ui = pd.concat([ui_bio, ui_iid])
ui.to_csv("results/ui.tsv", sep = "\t", index = False)


### Intersection Interactome

biogrid["set_genes"] = biogrid.apply(lambda row: frozenset([row.interactor_1, row.interactor_2]), axis=1)
iid["set_genes"] = iid.apply(lambda row: frozenset([row.interactor_1, row.interactor_2]), axis=1)

ii = pd.merge(biogrid, iid, how='inner', on=["set_genes"])
ii = ii.iloc[:,:4]
ii.columns = ["interactor_1", "interactor_2", "interactor_1_uniprot", "interactor_2_uniprot"]

ii = ii.loc[ii["interactor_1"].isin(genes) | ii["interactor_2"].isin(genes)]

ii.to_csv("results/ii.tsv", sep = "\t", index = False)
