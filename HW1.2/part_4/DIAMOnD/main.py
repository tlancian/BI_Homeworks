import pandas as pd

data = pd.read_csv("biogrid_all.txt", sep = "\t", usecols = ["Official Symbol Interactor A","Official Symbol Interactor B"])

data.to_csv("biogrid.txt", sep = ",")
