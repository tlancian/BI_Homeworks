import utils as ut

# Initialize the gene list
with open("../seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


#### Official Gene Symbol - HGNC   
with open('dataframes/hgnc.tsv', 'w') as results:
    results.write("gene\tapproved_symbol\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes, map(ut.query_hgnc, genes))) 



#### Uniprot AC + Protein Name
with open("dataframes/uniprot.tsv","w") as results:
    results.write("gene\tuniprot_ac\tprotein_name\tfunction\n")
    results.writelines("%s\t%s\n" % line for line in zip(genes,map(ut.query_uniprot, genes)))     



#### Entrez Gene ID

# Query to NCBI site
ncbi_results = dict(zip(genes,map(ut.query_ncbi, genes)))

# Looking at results, we note that some queries retrieve more than a single ID, since queries are not based on an exact match on gene name,
# but also on the aliases, thus we need to check manually on the site which IDs correspond to the given gene.

# Retrieving discrepancies
discrepancies = [k for k,v in ncbi_results.items() if len(v) != 1]

# After a visit to NCBI site, we can correct this results!

ncbi_results["PCDH11Y"] = ["83259"]
ncbi_results["RBMY1A1"] = ["5940"]
ncbi_results["RBMY1D"] = ["378949"]
ncbi_results["TSPY1"] = ["7258"]
ncbi_results["TSPY10"] = ["100289087"]
ncbi_results["TSPY3"] = ["728137"]
ncbi_results["TSPY1"] = ["728403"]

with open("dataframes/ncbi.tsv","w") as results:
    results.write("gene\tid\n")
    results.writelines("%s\t%s\n" % line for line in {k:v[0] for k,v in ncbi_results.items()}.items())

    
### Merging all the dataframes
df_name_list = ['dataframes/uniprot.tsv', 'dataframes/hgnc.tsv', 'dataframes/ncbi.tsv']
df_final = ut.merge_dfs(df_name_list)











