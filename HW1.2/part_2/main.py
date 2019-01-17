# Initialize the gene list
with open("seed_genes.txt","r") as f:
    genes = [gene.rstrip() for gene in f.readlines()]


### read data

ii = ut.read_graph("ii")
ui = ut.read_graph("ui")

# get LCC
G_ii = max(nx.connected_component_subgraphs(ii), key=len)
G_ui = max(nx.connected_component_subgraphs(ui), key=len)


### LOUVAIN 

partition_ii = ut.louvain(G_ii)
partition_ui = ut.louvain(G_ui)


### MCL

cl_ii_mcl = ut.MCL(G_ii)
cl_ui_mcl = ut.MCL(G_ui)


# create table
col_lst = ['cl_algo', 'mod_id', 'n_sg', 'n_g', 'sg_id', 'g_id', 'p_value']
df_ui = pd.DataFrame(data=None, columns = col_lst)
df_ii = pd.DataFrame(data=None, columns = col_lst)


### hypergeometric test - ui, MCL
df_ui = pd.DataFrame(data=None, columns = col_lst)
r = df_ui.shape[0]
for idx, c in enumerate(cl_ui_mcl):
    df_ui.loc[r+idx, 'cl_algo'] = 'MCL'
    df_ui.loc[r+idx, 'mod_id'] = idx
    df_ui.loc[r+idx, 'n_sg'] = ut.hypergeom_test(c, genes, G_ui)[1]
    df_ui.loc[r+idx, 'n_g'] = ut.hypergeom_test(c, genes, G_ui)[4]
    df_ui.loc[r+idx, 'sg_id'] = list(set(genes).intersection(set(c)))
    df_ui.loc[r+idx, 'g_id'] = list(set(c))
    df_ui.loc[r+idx, 'p_value'] = ut.hypergeom_test(c, genes, G_ui)[0]

       
        

### hypergeometric test - ii, MCL

df_ii = pd.DataFrame(data=None, columns = col_lst)
r = df_ii.shape[0]
for idx, c in enumerate(cl_ii_mcl):
    df_ii.loc[r+idx, 'cl_algo'] = 'MCL'
    df_ii.loc[r+idx, 'mod_id'] = idx
    df_ii.loc[r+idx, 'n_sg'] = ut.hypergeom_test(c, genes, G_ii)[1]
    df_ii.loc[r+idx, 'n_g'] = ut.hypergeom_test(c, genes, G_ii)[4]
    df_ii.loc[r+idx, 'sg_id'] = list(set(genes).intersection(set(c)))
    df_ii.loc[r+idx, 'g_id'] = list(set(c))
    df_ii.loc[r+idx, 'p_value'] = ut.hypergeom_test(c, genes, G_ii)[0]


### hypergeometric test - ui, Louvain


### hypergeometric test - ii, Louvain


#save

df_ui.to_csv('df_ui.csv')
df_ii.to_csv('df_ii.csv')