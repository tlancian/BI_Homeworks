import utils as ut

#TODO: 4.2 - Make a nice visualization of the network
#TODO: 4.3 - Make a nice visualization of the network


### 4.1

# Compute communities of EO network by Louvain Algo
eo_network = ut.read_graph("eo_pdc_20")
eo_communities = ut.get_communities(eo_network, "eo_pdc_20_communities")

# Compute communities of EC network by Louvain Algo
ec_network = ut.read_graph("ec_pdc_20")
ec_communities = ut.get_communities(ec_network, "ec_pdc_20_communities")

### 4.2

ut.draw_communities(eo_network, eo_communities, "eo_pdc_20_communities")
ut.draw_communities(ec_network, ec_communities, "ec_pdc_20_communities")


### 4.3

