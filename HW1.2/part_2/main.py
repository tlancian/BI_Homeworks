import utils as ut


### read data

ii = ut.read_graph("ii")
ui = ut.read_graph("ui")


### Hypergeom Test

ii_lou = map(lambda x : ut.hypergeom_test(ii,x) ,filter(ut.check_length_mod, ut.louvain(ii)))
ii_mcl = map(lambda x : ut.hypergeom_test(ii,x) ,filter(ut.check_length_mod, ut.mcl(ii)))


ui_lou = map(lambda x : ut.hypergeom_test(ui,x) ,filter(ut.check_length_mod, ut.louvain(ui)))
ui_mcl = map(lambda x : ut.hypergeom_test(ui,x) ,filter(ut.check_length_mod, ut.mcl(ui)))


# Create tables

ii_mod = ut.create_table("ii_mod", list(ii_lou), list(ii_mcl))
ui_mod = ut.create_table("ui_mod", list(ui_lou), list(ui_mcl))



# Visualize clusters 

ut.louvain(ii, 'ii', viz=True)
ut.louvain(ui, 'ui', viz=True)
ut.mcl(ii, viz=True)
ut.mcl(ui, viz=True)

