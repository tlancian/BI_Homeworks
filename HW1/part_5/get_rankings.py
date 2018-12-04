import utils as ut

sg_cl, sg_mf, sg_bp = ut.rank_dataset_go("innate/gene_ontology/sg_ora.txt")
ui_cl, ui_mf, ui_bp = ut.rank_dataset_go("innate/gene_ontology/ui_ora.txt")
ii_cl, ii_mf, ii_bp = ut.rank_dataset_go("innate/gene_ontology/ii_ora.txt")

sg_cl.to_csv("results/ranked_results/gene_ontology/sg_cl.tsv", sep = "\t", index = False)
sg_mf.to_csv("results/ranked_results/gene_ontology/sg_mf.tsv", sep = "\t", index = False)
sg_bp.to_csv("results/ranked_results/gene_ontology/sg_bp.tsv", sep = "\t", index = False)

ui_cl.to_csv("results/ranked_results/gene_ontology/ui_cl.tsv", sep = "\t", index = False)
ui_mf.to_csv("results/ranked_results/gene_ontology/ui_mf.tsv", sep = "\t", index = False)
ui_bp.to_csv("results/ranked_results/gene_ontology/ui_bp.tsv", sep = "\t", index = False)

ii_cl.to_csv("results/ranked_results/gene_ontology/ii_cl.tsv", sep = "\t", index = False)
ii_mf.to_csv("results/ranked_results/gene_ontology/ii_mf.tsv", sep = "\t", index = False)
ii_bp.to_csv("results/ranked_results/gene_ontology/ii_bp.tsv", sep = "\t", index = False)


ui_path = ut.rank_dataset_path("innate/pathway/ui_ora.txt")
ii_path = ut.rank_dataset_path("innate/pathway/ii_ora.txt")

ui_path.to_csv("results/ranked_results/pathway/ui_path.tsv", sep = "\t", index = False)
ii_path.to_csv("results/ranked_results/pathway/ii_path.tsv", sep = "\t", index = False)