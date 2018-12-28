import utils as ut

#TODO: ALL - choose more meaningful names for variables
#TODO: 3.2 - make a clear visualization
#TODO: 3.3 - create a functiont that makes the xls
#TODO: 3.3 - understanding enumeration of the graph.


# Creates the txt files needed for launching mfinder
ut.create_network_file("eo_pdc_20")
ut.create_network_file("ec_pdc_20")


######### Part 3.1

# Done with mfinder

#Parameters used:

# pval <0.01
# mfactor = 1.1
# U = 4
# random graphs = 1000


#Create a xls file with mfinder results - useful for the report
ut.parse_mfinder_output("eo_pdc_20_OUT_size3")
ut.parse_mfinder_output("ec_pdc_20_OUT_size3")



######### Part 3.2

# The motif id in mfinder for A->B<-C is 36
motif_id = 36

#Get all the triplets that form a motif with pattern A->B<-C directly from the Mfinder output
# and save a png of the subgraph composed by these triplets

ut.subgraph_by_motif("eo_pdc_20_MEMBERS_size3",motif_id)
ut.subgraph_by_motif("ec_pdc_20_MEMBERS_size3",motif_id)



######### Part 3.3

# Selecting the Parieto-Occipital central Channel, taht correpond to the number 57 in our data
channel = 57

# Selecting the motifs ids found by Mfinder, that were the same for both networks (EO and EC).
motifs = [38,46,108,110]

#Get triplets that contains the node 57 and save the subgraph induced by those motifs.
ut.get_involved_motifs("eo_pdc_20_MEMBERS_size3", channel, motifs)
ut.get_involved_motifs("ec_pdc_20_MEMBERS_size3", channel, motifs)


######### Part 3.4

# Done with Mfinder

# Same parameters

ut.parse_mfinder_output("eo_pdc_20_OUT_size4")
ut.parse_mfinder_output("ec_pdc_20_OUT_size4")
