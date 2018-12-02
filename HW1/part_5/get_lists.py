import pandas as pd

ui = pd.read_csv("../part_4/ui.tsv", sep = "\t")

ui_genes = list(set(ui['interactor_1']).union(set(ui['interactor_2'])))

with open("ui_genes.txt","w") as f:
    for gene in ui_genes:
        f.write(gene+"\n")
    f.close()
    

ii = pd.read_csv("../part_4/ii.tsv", sep = "\t")

ii_genes = list(set(ii['interactor_1']).union(set(ii['interactor_2'])))

with open("ii_genes.txt","w") as f:
    for gene in ii_genes:
        f.write(gene+"\n")
    f.close()