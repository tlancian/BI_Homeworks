import pandas as pd

#Seed Genes List

sg = pd.read_csv("../part_2/df_final.tsv", sep = "\t")

sg_genes = list(set(sg['uniprot_ac']))

with open("sg_genes.txt","w") as f:
    for gene in sg_genes:
        f.write(gene+"\n")
    f.close()


# Union Interactome List

ui = pd.read_csv("../part_4/ui.tsv", sep = "\t")

ui_genes = list(set(ui['interactor_1_uniprot']).union(set(ui['interactor_2_uniprot'])))

with open("ui_genes.txt","w") as f:
    for gene in ui_genes:
        f.write(gene+"\n")
    f.close()
 
# Intersection interactome list

ii = pd.read_csv("../part_4/ii.tsv", sep = "\t")

ii_genes = list(set(ii['interactor_1_uniprot']).union(set(ii['interactor_2_uniprot'])))

with open("ii_genes.txt","w") as f:
    for gene in ii_genes:
        f.write(gene+"\n")
    f.close()