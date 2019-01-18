import networkx as nx
import pandas as pd


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

cl_ii_lou = ut.louvain(G_ii)
cl_ui_lou = ut.louvain(G_ui)


### MCL

cl_ii_mcl = ut.MCL(G_ii)
cl_ui_mcl = ut.MCL(G_ui)


# create table
col_lst = ['cl_algo', 'mod_id', 'n_sg', 'n_g', 'sg_id', 'g_id', 'p_value']
df_ui = pd.DataFrame(data=None, columns = col_lst)
df_ii = pd.DataFrame(data=None, columns = col_lst)


### hypergeometric test - ui, MCL
df_ui = pd.DataFrame(data=None, columns = col_lst)
df_ui = ut.fill_df(df_ui, cl_ui_mcl, G_ui, genes, 'MCL')
       
        

### hypergeometric test - ii, MCL

df_ii = pd.DataFrame(data=None, columns = col_lst)
df_ii = ut.fill_df(df_ii, cl_ii_mcl, G_ii, genes, 'MCL')


### hypergeometric test - ui, Louvain

df_ui = ut.fill_df(df_ui, cl_ui_lou, G_ui, genes, 'Louvain')

### hypergeometric test - ii, Louvain

df_ii = ut.fill_df(df_ii, cl_ii_lou, G_ii, genes, 'Louvain')


#save

df_ui.to_csv('results/df_ui.csv')
df_ii.to_csv('results/df_ii.csv')


# get putative disease modules
#df_ui[(df_ui.n_g >= 10) & (df_ui.p_value < 0.05)]

