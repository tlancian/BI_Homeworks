import utils as ut

#TODO: 4.2 - Make a nice visualization of the network
#TODO: 4.3 - Make a nice visualization of the network


### 4.1

# Compute communities of EO network by Louvain Algo
#eo_communities = ut.get_communities("eo_pdc_50")

# Compute communities of EC network by Louvain Algo
#ec_communities = ut.get_communities("ec_pdc_50")

### 4.2

ut.draw_communities("eo_pdc_20", "eo_pdc_20_louvain", "louvain")
ut.draw_communities("ec_pdc_20", "ec_pdc_20_louvain", "louvain")

### 4.3



ut.draw_communities("eo_pdc_20", "eo_pdc_20_infomap", "infomap")
ut.draw_communities("ec_pdc_20", "ec_pdc_20_infomap", "infomap")


