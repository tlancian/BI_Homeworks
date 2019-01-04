import utils as ut
import operator
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


######## 2.1

### PDC

# Read data
adj_eo_pdc = np.load('../part_1/results/npy/eo_pdc_20.npy')
G_eo_pdc =nx.from_numpy_matrix(adj_eo_pdc, create_using=nx.DiGraph())

adj_ec_pdc = np.load('../part_1/results/npy/ec_pdc_20.npy')
G_ec_pdc =nx.from_numpy_matrix(adj_ec_pdc, create_using=nx.DiGraph())

## GLOBAL INDICES 

# Clustering Coefficient

CC_eo_pdc = nx.average_clustering(G_eo_pdc)
CC_ec_pdc = nx.average_clustering(G_ec_pdc)

# Average shortest path length

avg_path_eo_pdc = nx.average_shortest_path_length(G_eo_pdc)
avg_path_ec_pdc = nx.average_shortest_path_length(G_ec_pdc)


## LOCAL INDICES 

# degree 
degree_10_eo_pdc = sorted(list(G_eo_pdc.degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(degree_10_eo_pdc, 'degree_eo_pdc')
degree_10_ec_pdc = sorted(list(G_ec_pdc.degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(degree_10_ec_pdc, 'degree_ec_pdc')

# in_degree
in_degree_10_eo_pdc = sorted(list(G_eo_pdc.in_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(in_degree_10_eo_pdc, 'in_degree_eo_pdc')
in_degree_10_ec_pdc =sorted(list(G_ec_pdc.in_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(in_degree_10_ec_pdc, 'in_degree_ec_pdc')

# out_degree
out_degree_10_eo_pdc = sorted(list(G_eo_pdc.out_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(out_degree_10_eo_pdc, 'out_degree_eo_pdc')
out_degree_10_ec_pdc = sorted(list(G_ec_pdc.out_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(out_degree_10_ec_pdc, 'out_degree_ec_pdc')



######## 2.2

######## 2.3

### DTF

# Read data
adj_eo_dtf = np.load('../part_1/results/npy/eo_dtf_20.npy')
G_eo_dtf =nx.from_numpy_matrix(adj_eo_dtf, create_using=nx.DiGraph())

adj_ec_dtf = np.load('../part_1/results/npy/ec_dtf_20.npy')
G_ec_dtf =nx.from_numpy_matrix(adj_ec_dtf, create_using=nx.DiGraph())

## GLOBAL INDICES 

# Clustering Coefficient

CC_eo_dtf = nx.average_clustering(G_eo_dtf)
CC_ec_dtf = nx.average_clustering(G_ec_dtf)

# Average shortest path length

avg_path_eo_dtf = nx.average_shortest_path_length(G_eo_dtf)
avg_path_ec_dtf = nx.average_shortest_path_length(G_ec_dtf)

# save
cc = pd.DataFrame([[CC_eo_pdc, CC_ec_pdc], [CC_eo_dtf, CC_ec_dtf]], columns=['pdc', 'dtf'])
avg_path = pd.DataFrame([[avg_path_eo_pdc, avg_path_ec_pdc], [avg_path_eo_dtf, avg_path_ec_dtf]], columns=['pdc', 'dtf'])

cc.to_csv('results/clustering_coefficient.csv')
avg_path.to_csv('results/average_shortest_path.csv')


######## 2.4

lst_eo = ['eo_pdc_05', 'eo_pdc_10', 'eo_pdc_20', 'eo_pdc_30', 'eo_pdc_50']
lst_ec = ['ec_pdc_05', 'ec_pdc_10', 'ec_pdc_20', 'ec_pdc_30', 'ec_pdc_50']

global_cc_eo = ut.global_indeces(lst_eo)[0]
avg_path_eo = ut.global_indeces(lst_eo)[1]

global_cc_ec = ut.global_indeces(lst_ec)[0]
avg_path_ec = ut.global_indeces(lst_ec)[1]

# save
ut.global_plot(global_cc_ec, avg_path_ec, 'global_indices_ec_pdc')
ut.global_plot(global_cc_eo, avg_path_eo, 'global_indices_eo_pdc')


######## 2.5

ut.topology(G_eo_pdc, 'topology_eo_pdc')
ut.topology(G_eo_pdc, 'topology_ec_pdc')


######## 2.6

adj_ec2 = np.load('../part_1/results/npy/alt_ec_pdc_20.npy')
G_ec2 = nx.from_numpy_matrix(adj_ec2, create_using=nx.DiGraph())
adj_eo2 = np.load('../part_1/results/npy/alt_eo_pdc_20.npy')
G_eo2 = nx.from_numpy_matrix(adj_eo2, create_using=nx.DiGraph())


## GLOBAL INDICES 

CC_eo2 = nx.average_clustering(G_eo2)
CC_ec2 = nx.average_clustering(G_ec2)

avg_path_eo2 = nx.average_shortest_path_length(G_eo2)
avg_path_ec2 = nx.average_shortest_path_length(G_ec2)


df = pd.DataFrame([[CC_eo_pdc, CC_eo2, CC_ec_pdc, CC_ec2],
                      [avg_path_eo_pdc, avg_path_eo2, avg_path_ec_pdc, avg_path_ec2]], 
                     columns=['eo_pdc','alt_eo','ec_pdc','alt_ec'],
                 index = ['clustering_coefficient', 'avg_shortest_path_length'])
df.to_csv('results/graph_idx_comparison.csv')

## LOCAL INDICES 

# degree 
degree_10_eo2 = sorted(list(G_eo2.degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(degree_10_eo2, 'degree_alt_eo')
degree_10_ec2 = sorted(list(G_ec2.degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(degree_10_ec2, 'degree_alt_ec')

# in_degree
in_degree_10_eo2 = sorted(list(G_eo2.in_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(in_degree_10_eo2, 'in_degree_alt_eo')
in_degree_10_ec2 =sorted(list(G_ec2.in_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(in_degree_10_ec2, 'in_degree_alt_ec')

# out_degree
out_degree_10_eo2 = sorted(list(G_eo2.out_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(out_degree_10_eo2, 'out_degree_alt_eo')
out_degree_10_ec2 = sorted(list(G_ec2.out_degree), reverse=True, key=operator.itemgetter(1))[:10]
ut.save_highest_10(out_degree_10_ec2, 'out_degree_alt_ec')



######## 2.7


