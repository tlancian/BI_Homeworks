import utils as ut

# Read the file
signals = ut.read_file("../data/S072R01.edf")

# Fit the model

order = 10
fs = 10
resolution = 1

mod = ut.fit_model(signals, order, fs, resolution, "pdc")
mod = ut.fit_model(signals, order, fs, resolution, "dtf")

