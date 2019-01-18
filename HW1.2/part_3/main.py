import utils as ut

for file in ut.mod_files("putative_disease_modules/"):
    ut.translate(file)


for file in ut.mod_files("results/innate/"):
        ut.top_ten(file)