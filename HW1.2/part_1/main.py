import utils as ut

# Read the graphs
ii = ut.read_graph("ii")
sgi = ut.read_graph("sgi")
ui = ut.read_graph("ui")

# Compute global measures
ut.graph_global_measures(ii, "ii")
ut.graph_global_measures(sgi, "sgi")
ut.graph_global_measures(ui, "ui")


# Compute LCC global measures
ut.graph_global_measures(ii, "ii", True)
ut.graph_global_measures(sgi, "sgi", True)
ut.graph_global_measures(ui, "ui", True)
