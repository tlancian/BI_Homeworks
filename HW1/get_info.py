import utils as ut


# Initialize the gene list
with open("genes_list.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


#### Official Gene Symbol  

# Created with HGNC site tool.


#### Uniprot AC + Protein Name
# TODO: Check whether two genes can have same Uniprot AC, ask whether Protein Name is the one in bold in the Uniprot DB
# TODO: Modify columns needed in results.write


# For each gene query in the Uniprot DB, and return a tsv with all the results
with open("uniprot.tsv","w") as results:
    results.write("Entry\tEntry name\tStatus\tProtein names\tGene names\tOrganism\tLength\n")
    for elem in map(ut.get_info, genes):
        results.writelines("%s\t%s\n" % line for line in elem[1:])
        
      
   
#### Entrez Gene ID

with open("ncbi.tsv","w") as results:
    results.write("Gene\tID\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes,map(ut.query_ncbi, genes)))
    
    
#### Description
#TODO: Understand what they want
