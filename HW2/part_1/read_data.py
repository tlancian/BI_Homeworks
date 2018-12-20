import utils as ut

# Read the files
eo = ut.read_file("../data/S072R01.edf")
ec = ut.read_file("../data/S072R01.edf")

######## 1.1

fs = 160 # Frequency of sampling, given by data
resolution = 100 # Resolution of model (s.t. each bin has 1Hz of width)
freq = 10 # Frequency of interest
density = 0.2 # Density of the graph desired


###PDC

# Fitting models
eo_pdc = ut.fit_model(eo, fs, resolution, "pdc", freq)
ec_pdc = ut.fit_model(ec, fs, resolution, "pdc", freq)

# Adjacency Matrices
ut.adjacency_matrix(eo_pdc, ut.find_threshold(eo_pdc,density), "networks/eo_pdc_20.npy")
ut.adjacency_matrix(ec_pdc, ut.find_threshold(ec_pdc,density), "networks/ec_pdc_20.npy")


#TODO: Graphical representation of the adjacency matrices

######## 1.2


# Fitting models
eo_dtf = ut.fit_model(eo, fs, resolution, "dtf", freq)
ec_dtf = ut.fit_model(ec, fs, resolution, "dtf", freq)

# Adjacency Matrices
ut.adjacency_matrix(eo_dtf, ut.find_threshold(eo_dtf,density), "networks/eo_dtf_20.npy")
ut.adjacency_matrix(ec_dtf, ut.find_threshold(ec_dtf,density), "networks/ec_dtf_20.npy")


#TODO: Graphical representation of the adjacency matrices

######## 1.3

densities = [0.01,0.05,0.1,0.3,0.5] #Different thresholds

#Names for files
eo_pdc_names = ["networks/eo_pdc_01.npy", "networks/eo_pdc_05.npy", "networks/eo_pdc_10.npy", "networks/eo_pdc_30.npy", "networks/eo_pdc_50.npy"]
ec_pdc_names = ["networks/ec_pdc_01.npy", "networks/ec_pdc_05.npy", "networks/ec_pdc_10.npy", "networks/ec_pdc_30.npy", "networks/ec_pdc_50.npy"]
eo_dtf_names = ["networks/eo_dtf_01.npy", "networks/eo_dtf_05.npy", "networks/eo_dtf_10.npy", "networks/eo_dtf_30.npy", "networks/eo_dtf_50.npy"]
ec_dtf_names = ["networks/ec_dtf_01.npy", "networks/ec_dtf_05.npy", "networks/ec_dtf_10.npy", "networks/ec_dtf_30.npy", "networks/ec_dtf_50.npy"]


###PDC

eo_pdc_networks = list(map(lambda x: ut.adjacency_matrix(eo_pdc, ut.find_threshold(eo_pdc,x[0]), x[1]), zip(densities,eo_pdc_names)))
eo_pdc_networks = list(map(lambda x: ut.adjacency_matrix(eo_pdc, ut.find_threshold(eo_pdc,x[0]), x[1]), zip(densities,ec_pdc_names)))


###DTF

eo_pdc_networks = list(map(lambda x: ut.adjacency_matrix(eo_pdc, ut.find_threshold(eo_pdc,x[0]), x[1]), zip(densities,eo_dtf_names)))
eo_pdc_networks = list(map(lambda x: ut.adjacency_matrix(eo_pdc, ut.find_threshold(eo_pdc,x[0]), x[1]), zip(densities,ec_dtf_names)))



######## 1.4


channels = ["Fp1", "Fp2", "F7", "F3", "Fz", "F4", "F8", "T7", "C3", "Cz", "C4", "T8", "P7", "P3", "Pz", "P4", "P8", "O1", "O2"]

small_eo = ut.read_file("../data/S072R01.edf", channels = channels)
small_ec = ut.read_file("../data/S072R02.edf", channels = channels)

mod = ut.fit_model(small_eo, fs, resolution, "pdc", freq)

#TODO: check bootstrap for connectivipy



######## 1.5

small_eo_pdc = ut.adjacency_matrix(mod, ut.find_threshold(mod,density))

#TODO: ask for the right channel locations!


######## 1.6

alternative_frequency = 20

###PDC

# Fitting models
alt_eo_pdc = ut.fit_model(eo, fs, resolution, "pdc", alternative_frequency)
alt_ec_pdc = ut.fit_model(ec, fs, resolution, "pdc", alternative_frequency)

# Adjacency Matrices
ut.adjacency_matrix(eo_pdc, ut.find_threshold(alt_eo_pdc,density), "networks/alt_eo_pdc_20.npy")
ut.adjacency_matrix(ec_pdc, ut.find_threshold(alt_ec_pdc,density), "networks/alt_ec_pdc_20.npy")


#TODO: CHeck if alternative frequency is correct