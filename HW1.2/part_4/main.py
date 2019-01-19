import utils as ut

ut.create_network()

ut.translate("seed_genes", "sg_entrez")

ut.join_files("sg_entrez", "diamond", "intersection_list")

ut.top_ten("go_ora")
ut.top_ten("path_ora")