import utils as ut


# Initialize the gene list
with open("genes_list.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


#### Official Gene Symbol - HGNC  
    
with open('hgnc_list.tsv', 'w') as results:
    results.write("Gene\tApproved Symbol\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes, map(ut.query_hgnc, genes))) 


#### Uniprot AC + Protein Name

with open("uniprot.tsv","w") as results:
    results.write("gene\tuniprot_ac\t\tprotein_name\tfunction\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes,map(ut.query_uniprot, genes)))
        
      
#### Entrez Gene ID

with open("ncbi.tsv","w") as results:
    results.write("Gene\tID\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes,map(ut.query_ncbi, genes)))
    


# TODO: Check how to print protein names
# TODO: check if function can be taken from elsewhere